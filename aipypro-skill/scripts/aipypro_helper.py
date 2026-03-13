#!/usr/bin/env python3
"""
AipyPro Helper Script - Enhanced Version
This script provides enhanced helper functions for working with AipyPro agent.
It includes functions to execute commands, parse results, manage tasks, and more.
Features:
1. Command execution with error handling
2. File management and analysis
3. Task configuration management
4. Dependency installation
5. Code generation assistance
Usage:
    python aipypro_helper.py --help
    python aipypro_helper.py --install-packages pandas numpy
    python aipypro_helper.py --analyze-dir .
    python aipypro_helper.py --generate-config
"""
import subprocess
import json
import os
import re
import time
import sys
import argparse
import logging
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union, Any
from datetime import datetime
# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
class AipyProHelper:
    """Enhanced helper class for AipyPro operations."""
    
    def __init__(self, work_dir: str = None):
        """
        Initialize AipyPro helper.
        
        Args:
            work_dir: Working directory (default: current directory)
        """
        self.work_dir = Path(work_dir) if work_dir else Path.cwd()
        self.aipypro_path = self._find_aipypro()
        self.config = self._load_config()
        
    def _find_aipypro(self) -> Optional[Path]:
        """
        Find AipyPro executable.
        
        Returns:
            Path to AipyPro executable or None if not found
        """
        # Check common locations
        common_paths = [
            Path("/usr/local/bin/aipypro"),
            Path("/usr/bin/aipypro"),
            Path.cwd() / "aipypro",
            Path.home() / ".local/bin/aipypro",
        ]
        
        for path in common_paths:
            if path.exists():
                logger.info(f"Found AipyPro at: {path}")
                return path
        
        # Try which/where command
        try:
            if sys.platform == "win32":
                result = subprocess.run(["where", "aipypro"], 
                                      capture_output=True, text=True)
            else:
                result = subprocess.run(["which", "aipypro"], 
                                      capture_output=True, text=True)
            
            if result.returncode == 0:
                path = Path(result.stdout.strip())
                if path.exists():
                    logger.info(f"Found AipyPro at: {path}")
                    return path
        except Exception as e:
            logger.warning(f"Error finding AipyPro: {e}")
        
        logger.warning("AipyPro not found. Please ensure it's installed and in PATH.")
        return None
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from file."""
        config_path = self.work_dir / ".aipypro_config.json"
        default_config = {
            "output_dir": str(self.work_dir / "aipypro_output"),
            "max_files": 100,
            "cleanup_days": 30,
            "auto_install_deps": True,
            "log_level": "INFO"
        }
        
        if config_path.exists():
            try:
                with open(config_path, 'r') as f:
                    user_config = json.load(f)
                    default_config.update(user_config)
                    logger.info(f"Loaded config from: {config_path}")
            except Exception as e:
                logger.error(f"Error loading config: {e}")
        
        return default_config
    
    def save_config(self) -> bool:
        """Save current configuration to file."""
        config_path = self.work_dir / ".aipypro_config.json"
        try:
            with open(config_path, 'w') as f:
                json.dump(self.config, f, indent=2)
            logger.info(f"Config saved to: {config_path}")
            return True
        except Exception as e:
            logger.error(f"Error saving config: {e}")
            return False
    
    def run_command(self, instruction: str, style: str = None, 
                   role: str = None, task: str = None) -> Dict[str, Any]:
        """
        Run AipyPro command with enhanced error handling.
        
        Args:
            instruction: Natural language instruction
            style: Code style (professional, simple, debug)
            role: Execution role (developer, analyst, etc.)
            task: Task type (data_analysis, system_admin, etc.)
        
        Returns:
            Dictionary with execution results
        """
        if not self.aipypro_path:
            return {"success": False, "error": "AipyPro not found"}
        
        # Build command
        cmd = [str(self.aipypro_path), "run"]
        
        if style:
            cmd.extend(["--style", style])
        if role:
            cmd.extend(["--role", role])
        if task:
            cmd.extend(["--task", task])
        
        cmd.append(f'"{instruction}"')
        
        logger.info(f"Executing command: {' '.join(cmd)}")
        
        try:
            # Execute command
            start_time = time.time()
            result = subprocess.run(
                ' '.join(cmd),
                shell=True,
                capture_output=True,
                text=True,
                cwd=str(self.work_dir),
                timeout=300  # 5 minute timeout
            )
            end_time = time.time()
            
            execution_time = end_time - start_time
            
            # Parse output
            output = {
                "success": result.returncode == 0,
                "returncode": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "execution_time": execution_time,
                "command": ' '.join(cmd)
            }
            
            if result.returncode == 0:
                logger.info(f"Command executed successfully in {execution_time:.2f}s")
                output["generated_files"] = self._find_generated_files()
            else:
                logger.error(f"Command failed with return code {result.returncode}")
                logger.error(f"Stderr: {result.stderr}")
            
            return output
            
        except subprocess.TimeoutExpired:
            logger.error("Command execution timed out after 5 minutes")
            return {"success": False, "error": "Execution timeout"}
        except Exception as e:
            logger.error(f"Error executing command: {e}")
            return {"success": False, "error": str(e)}
    
    def _find_generated_files(self) -> List[str]:
        """Find files generated by AipyPro."""
        generated_files = []
        
        # Look for common patterns
        patterns = [
            "*.py",
            "*.txt",
            "*.json",
            "*.md",
            "*.csv",
            "*.png",
            "*.jpg",
            "*.jpeg"
        ]
        
        for pattern in patterns:
            for file in self.work_dir.glob(pattern):
                # Skip common system files
                if file.name in ["__pycache__", ".git", ".vscode"]:
                    continue
                generated_files.append(str(file))
        
        return generated_files
    
    def list_generated_files(self, detailed: bool = False) -> List[Dict[str, Any]]:
        """
        List all generated files with details.
        
        Args:
            detailed: Include file size and modification time
        
        Returns:
            List of file information dictionaries
        """
        files_info = []
        
        for file_path in self._find_generated_files():
            path = Path(file_path)
            info = {
                "name": path.name,
                "path": str(path),
                "extension": path.suffix.lower(),
                "exists": path.exists()
            }
            
            if detailed and path.exists():
                try:
                    stat = path.stat()
                    info.update({
                        "size": stat.st_size,
                        "size_human": self._format_bytes(stat.st_size),
                        "modified": datetime.fromtimestamp(stat.st_mtime),
                        "created": datetime.fromtimestamp(stat.st_ctime)
                    })
                except Exception as e:
                    logger.warning(f"Error getting file info for {path}: {e}")
            
            files_info.append(info)
        
        return files_info
    
    def clean_old_files(self, days: int = 30, dry_run: bool = False) -> Dict[str, Any]:
        """
        Clean old generated files.
        
        Args:
            days: Delete files older than this many days
            dry_run: Only show what would be deleted
        
        Returns:
            Cleanup summary
        """
        cutoff_time = time.time() - (days * 24 * 60 * 60)
        files_to_delete = []
        total_size = 0
        
        for file_info in self.list_generated_files(detailed=True):
            if "modified" in file_info:
                if file_info["modified"].timestamp() < cutoff_time:
                    files_to_delete.append(file_info)
                    total_size += file_info.get("size", 0)
        
        result = {
            "total_found": len(files_to_delete),
            "total_size": total_size,
            "total_size_human": self._format_bytes(total_size),
            "files": files_to_delete,
            "dry_run": dry_run
        }
        
        if not dry_run and files_to_delete:
            logger.info(f"Deleting {len(files_to_delete)} old files...")
            deleted_count = 0
            for file_info in files_to_delete:
                try:
                    Path(file_info["path"]).unlink()
                    deleted_count += 1
                    logger.info(f"Deleted: {file_info['path']}")
                except Exception as e:
                    logger.error(f"Error deleting {file_info['path']}: {e}")
            
            result["deleted_count"] = deleted_count
        
        return result
    
    def install_packages(self, packages: List[str], upgrade: bool = False) -> Dict[str, Any]:
        """
        Install Python packages.
        
        Args:
            packages: List of package names
            upgrade: Upgrade existing packages
        
        Returns:
            Installation results
        """
        if not packages:
            return {"success": False, "error": "No packages specified"}
        
        cmd = [sys.executable, "-m", "pip", "install"]
        
        if upgrade:
            cmd.append("--upgrade")
        
        cmd.extend(packages)
        
        logger.info(f"Installing packages: {', '.join(packages)}")
        
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=300
            )
            
            output = {
                "success": result.returncode == 0,
                "returncode": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "packages": packages
            }
            
            if result.returncode == 0:
                logger.info(f"Successfully installed {len(packages)} packages")
            else:
                logger.error(f"Package installation failed: {result.stderr}")
            
            return output
            
        except Exception as e:
            logger.error(f"Error installing packages: {e}")
            return {"success": False, "error": str(e), "packages": packages}
    
    def analyze_directory(self, directory: str = None) -> Dict[str, Any]:
        """
        Analyze directory structure and contents.
        
        Args:
            directory: Directory to analyze (default: work directory)
        
        Returns:
            Directory analysis results
        """
        target_dir = Path(directory) if directory else self.work_dir
        
        if not target_dir.exists():
            return {"success": False, "error": f"Directory not found: {target_dir}"}
        
        logger.info(f"Analyzing directory: {target_dir}")
        
        try:
            file_types = {}
            total_size = 0
            file_count = 0
            dir_count = 0
            
            for root, dirs, files in os.walk(target_dir):
                dir_count += len(dirs)
                file_count += len(files)
                
                for file in files:
                    file_path = Path(root) / file
                    
                    # Get file size
                    try:
                        size = file_path.stat().st_size
                        total_size += size
                    except:
                        pass
                    
                    # Count by extension
                    ext = file_path.suffix.lower()
                    if not ext:
                        ext = "no_extension"
                    
                    file_types[ext] = file_types.get(ext, 0) + 1
            
            # Get largest files
            large_files = []
            for root, _, files in os.walk(target_dir):
                for file in files:
                    file_path = Path(root) / file
                    try:
                        size = file_path.stat().st_size
                        large_files.append({
                            "path": str(file_path),
                            "size": size,
                            "size_human": self._format_bytes(size)
                        })
                    except:
                        pass
            
            # Sort by size
            large_files.sort(key=lambda x: x["size"], reverse=True)
            
            result = {
                "success": True,
                "directory": str(target_dir),
                "total_directories": dir_count,
                "total_files": file_count,
                "total_size": total_size,
                "total_size_human": self._format_bytes(total_size),
                "file_types": file_types,
                "largest_files": large_files[:10]  # Top 10 largest
            }
            
            logger.info(f"Analysis complete: {file_count} files, {self._format_bytes(total_size)}")
            return result
            
        except Exception as e:
            logger.error(f"Error analyzing directory: {e}")
            return {"success": False, "error": str(e)}
    
    def generate_task_config(self, task_name: str, description: str = "", 
                           dependencies: List[str] = None) -> Dict[str, Any]:
        """
        Generate task configuration template.
        
        Args:
            task_name: Name of the task
            description: Task description
            dependencies: List of required packages
        
        Returns:
            Generated configuration
        """
        config = {
            "task_name": task_name,
            "description": description,
            "created": datetime.now().isoformat(),
            "dependencies": dependencies or [],
            "parameters": {
                "style": "professional",
                "role": "developer",
                "timeout": 300
            },
            "output": {
                "files": [],
                "reports": []
            }
        }
        
        # Save to file
        config_file = self.work_dir / f"{task_name}_config.json"
        try:
            with open(config_file, 'w') as f:
                json.dump(config, f, indent=2)
            
            logger.info(f"Task config saved to: {config_file}")
            return {"success": True, "config_file": str(config_file), "config": config}
            
        except Exception as e:
            logger.error(f"Error saving task config: {e}")
            return {"success": False, "error": str(e)}
    
    def _format_bytes(self, bytes_val: int) -> str:
        """Format bytes to human-readable format."""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes_val < 1024:
                return f"{bytes_val:.1f} {unit}"
            bytes_val /= 1024
        return f"{bytes_val:.1f} PB"
def main():
    """Main function for command-line interface."""
    parser = argparse.ArgumentParser(
        description="AipyPro Helper Script - Enhanced Version",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python aipypro_helper.py --install-packages pandas numpy
  python aipypro_helper.py --analyze-dir .
  python aipypro_helper.py --clean-old-files --days 30
  python aipypro_helper.py --generate-config my_task "Task description"
        """
    )
    
    # Command groups
    command_group = parser.add_mutually_exclusive_group()
    
    # Installation commands
    command_group.add_argument(
        "--install-packages",
        nargs="+",
        metavar="PACKAGE",
        help="Install Python packages"
    )
    
    command_group.add_argument(
        "--install-deps",
        action="store_true",
        help="Install common dependencies"
    )
    
    # File management commands
    command_group.add_argument(
        "--analyze-dir",
        metavar="DIRECTORY",
        nargs="?",
        const=".",
        help="Analyze directory structure"
    )
    
    command_group.add_argument(
        "--list-files",
        action="store_true",
        help="List generated files"
    )
    
    command_group.add_argument(
        "--clean-old-files",
        action="store_true",
        help="Clean old generated files"
    )
    
    command_group.add_argument(
        "--dry-run",
        action="store_true",
        help="Dry run for cleanup (show what would be deleted)"
    )
    
    # Configuration commands
    command_group.add_argument(
        "--generate-config",
        nargs=2,
        metavar=("TASK_NAME", "DESCRIPTION"),
        help="Generate task configuration"
    )
    
    # Additional options
    parser.add_argument(
        "--days",
        type=int,
        default=30,
        help="Days threshold for cleaning old files (default: 30)"
    )
    
    parser.add_argument(
        "--upgrade",
        action="store_true",
        help="Upgrade packages when installing"
    )
    
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )
    
    parser.add_argument(
        "--work-dir",
        default=".",
        help="Working directory (default: current directory)"
    )
    
    args = parser.parse_args()
    
    # Set logging level
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Initialize helper
    helper = AipyProHelper(work_dir=args.work_dir)
    
    # Execute command based on arguments
    if args.install_packages:
        result = helper.install_packages(args.install_packages, args.upgrade)
        print(json.dumps(result, indent=2, default=str))
    
    elif args.install_deps:
        common_deps = ["pandas", "numpy", "matplotlib", "seaborn", "scikit-learn"]
        result = helper.install_packages(common_deps, args.upgrade)
        print(json.dumps(result, indent=2, default=str))
    
    elif args.analyze_dir:
        result = helper.analyze_directory(args.analyze_dir)
        print(json.dumps(result, indent=2, default=str))
    
    elif args.list_files:
        files = helper.list_generated_files(detailed=True)
        print(json.dumps(files, indent=2, default=str))
    
    elif args.clean_old_files:
        result = helper.clean_old_files(days=args.days, dry_run=args.dry_run)
        print(json.dumps(result, indent=2, default=str))
    
    elif args.generate_config:
        task_name, description = args.generate_config
        result = helper.generate_task_config(task_name, description)
        print(json.dumps(result, indent=2, default=str))
    
    else:
        parser.print_help()
if __name__ == "__main__":
    main()
