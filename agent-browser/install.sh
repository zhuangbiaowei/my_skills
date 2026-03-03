#!/bin/bash
# ============================================================
# agent-browser 安装脚本
# Description: 自动化检查并安装 agent-browser 浏览器自动化工具
# Author: zbw
# Date: 2026-03-03
# ============================================================

set -e  # Exit on error

echo "🦐 ====== Agent-Browser Installation Script ======"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Helper functions
log_info() { echo -e "${BLUE}[INFO]${NC} $1"; }
log_success() { echo -e "${GREEN}[SUCCESS]${NC} $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }

# Check command existence
command_exists() {
    command -v "$1" &> /dev/null
}

echo "📋 Step 1: Checking prerequisites..."
echo ""

# ✅ Check Node.js (required for npm)
if ! command_exists node; then
    log_error "Node.js is not installed. Please install Node.js first."
    echo "   → See https://nodejs.org/ or use nvm"
    exit 1
fi
NODE_VERSION=$(node -v | sed 's/v//')
log_success "✓ Node.js v$NODE_VERSION detected"

# ✅ Check npm
if ! command_exists npm; then
    log_error "npm is not installed. Please install it first."
    exit 1
fi
NPM_VERSION=$(npm -v)
log_success "✓ npm v$NPM_VERSION detected"

echo ""
echo "🌐 Step 2: Checking for existing agent-browser installation..."
echo ""

# Check if agent-browser is already installed globally
if command_exists agent-browser; then
    INSTALLED_VERSION=$(agent-browser --version 2>&1 | head -n1)
    log_warn "Agent-Browser v$INSTALLED_VERSION is already installed."
    
    read -p "Do you want to reinstall? (y/n): " REINSTALL
    if [[ "$REINSTALL" =~ ^[Yy]$ ]]; then
        npm uninstall -g agent-browser || true
    else
        log_success "Skipping reinstallation. Exiting..."
        exit 0
    fi
else
    log_info "Agent-Browser is not installed yet."
fi

echo ""
echo "🔧 Step 3: Installing agent-browser via npm..."
echo ""

npm install -g agent-browser || {
    log_error "Failed to install agent-browser. Please check your network connection and try again."
    
    # Try alternative installation method (if npm fails)
    if command_exists yarn; then
        log_info "Trying with Yarn instead..."
        yarn global add agent-browser || {
            log_error "Yarn installation also failed. Exiting..."
            exit 1
        }
    else
        exit 1
    fi
}

INSTALLED_VERSION=$(agent-browser --version 2>&1 | head -n1)
log_success "✓ Agent-Browser v$INSTALLED_VERSION installed successfully!"

echo ""
echo "🦄 Step 4: Checking for browser (required for operation)..."
echo ""

# Check for supported browsers
BROWSER_FOUND=false
declare -A BROWSERS=(
    ["chrome"]="Google Chrome"
    ["brave"]="Brave Browser"
    ["edge"]="Microsoft Edge"
    ["chromium"]="Chromium"
    ["google-chrome"]="Chrome (Ubuntu)"
)

for browser in "${!BROWSERS[@]}"; do
    if command_exists "$browser"; then
        log_success "✓ ${BROWSERS[$browser]} detected: $(command -v $browser)"
        BROWSER_FOUND=true
        break
    fi
done

if ! $BROWSER_FOUND; then
    log_warn "No supported browser found! Agent-Browser needs Chrome/Chromium-based browsers."
    
    echo ""
    echo "📌 Please install one of the following:"
    echo ""
    echo "   Ubuntu/Debian:"
    echo "     sudo apt update && sudo apt install -y chromium-browser"
    echo ""
    echo "   macOS (Homebrew):"
    echo "     brew install --cask google-chrome  # or brave, edge, chromium"
    echo ""
    echo "   Windows:"
    echo "     Download from https://www.google.com/chrome/ or Microsoft Edge website"
    echo ""
    
    read -p "Install Chromium now? (y/n): " INSTALL_CHROMIUM
    if [[ "$INSTALL_CHROMIUM" =~ ^[Yy]$ ]]; then
        sudo apt update && sudo apt install -y chromium-browser || {
            log_error "Failed to install Chromium. You'll need to install it manually."
        }
    fi
fi

echo ""
echo "🎉 Step 5: Verifying installation..."
echo ""

# Run basic verification test
if agent-browser --help > /dev/null 2>&1; then
    log_success "✓ Installation verified successfully!"
else
    log_error "Verification failed. Please check the error messages above."
fi

echo ""
echo "📚 Step 6: Quick start guide..."
echo ""
cat << 'EOF'
✅ Agent-Browser is ready to use!

Quick Start Examples:
---------------------
1. Open a website:
   $ agent-browser open https://www.baidu.com

2. Search and screenshot:
   $ agent-browser fill '[name="wd"]' "搜索关键词" && press Enter && snapshot --annotate -i

3. Smart element finding (no CSS selector needed!):
   $ find role button click --name "登录"

4. Wait for page to load completely:
   $ wait --load networkidle

Documentation:
- Full command reference: https://agent-browser.dev/commands
- This skill doc: ~/skills/agent-browser/SKILL.md

Need help? Check the SKILL.md file in this directory! 🦐
EOF

echo ""
echo "🚀 Installation complete!"
log_success "Run 'agent-browser --help' to get started."
echo ""
