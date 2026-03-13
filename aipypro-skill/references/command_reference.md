# AipyPro Command Reference
*Last Updated: 2026-03-13 12:05:30*
## 📖 简介
本文档提供了AipyPro命令的完整参考，包括基本命令格式、参数说明、使用示例和最佳实践。
## 🚀 快速导航
- [基本命令格式](#基本命令格式)
- [命令参数详解](#命令参数详解)
- [使用示例](#使用示例)
- [高级功能](#高级功能)
- [故障排除](#故障排除)
- [最佳实践](#最佳实践)
## ⚙️ 基本命令格式
### 最简单的命令格式
```bash
aipypro run "instruction"
```
**参数说明:**
- `instruction`: 必需参数，自然语言指令，描述要执行的任务
### 完整命令格式
```bash
aipypro run [-h] [--style STYLE] [--role ROLE] [--task TASK] [instruction]
```
## 🔧 命令参数详解
### 必需参数
#### `instruction`
- **描述**: 自然语言指令，描述要执行的任务
- **格式**: 字符串，用双引号包围
- **示例**: `"print Hello World"`, `"calculate 7 * 8"`
- **最佳实践**: 提供清晰、具体的描述，避免歧义
### 可选参数
#### `-h, --help`
- **描述**: 显示帮助信息
- **用法**: `aipypro run -h` 或 `aipypro run --help`
- **输出**: 显示命令帮助和参数说明
#### `--style STYLE`
- **描述**: 指定代码生成风格
- **可选值**: 
  - `professional`: 专业风格（默认）
  - `simple`: 简洁风格
  - `debug`: 调试风格，包含额外注释
  - `concise`: 简洁风格，省略非必要代码
- **示例**: `aipypro run --style professional "create function"`
#### `--role ROLE`
- **描述**: 指定执行角色，影响代码风格和复杂度
- **可选值**:
  - `developer`: 开发者角色（默认）
  - `data_scientist`: 数据科学家角色
  - `system_admin`: 系统管理员角色
  - `student`: 学生角色，代码更易理解
  - `senior_developer`: 高级开发者角色，代码更优化
- **示例**: `aipypro run --role data_scientist "analyze data"`
#### `--task TASK`
- **描述**: 指定任务类型，优化代码生成
- **可选值**:
  - `data_analysis`: 数据分析任务
  - `system_admin`: 系统管理任务
  - `web_development`: Web开发任务
  - `machine_learning`: 机器学习任务
  - `automation`: 自动化任务
- **示例**: `aipypro run --task data_analysis "clean dataset"`
#### `--verbose`
- **描述**: 启用详细输出模式
- **用法**: `aipypro run --verbose "instruction"`
- **效果**: 显示更多执行细节和调试信息
#### `--timeout SECONDS`
- **描述**: 设置命令执行超时时间（秒）
- **默认值**: 300（5分钟）
- **示例**: `aipypro run --timeout 600 "long running task"`
## 📚 使用示例
### 基础示例
#### 示例1: Hello World
```bash
aipypro run "print Hello World"
```
**输出**: 生成并执行打印"Hello World"的Python脚本
#### 示例2: 简单计算
```bash
aipypro run "calculate 7 * 8"
```
**输出**: 计算7乘以8的结果
#### 示例3: 文件操作
```bash
aipypro run "list files in current directory"
```
**输出**: 列出当前目录下的文件
### 带参数示例
#### 示例4: 使用特定风格
```bash
aipypro run --style debug "implement binary search"
```
**特点**: 生成的代码包含详细注释和调试信息
#### 示例5: 指定角色
```bash
aipypro run --role data_scientist "analyze time series data"
```
**特点**: 代码针对数据分析优化，包含统计函数和可视化
#### 示例6: 指定任务类型
```bash
aipypro run --task system_admin "monitor system resources"
```
**特点**: 代码针对系统管理优化，包含资源监控功能
### 组合参数示例
#### 示例7: 完整参数组合
```bash
aipypro run --style professional --role senior_developer --task web_development "create REST API"
```
**特点**: 生成专业级、优化过的Web API代码
## 🛠️ 高级功能
### 文件生成模式
AipyPro会自动生成以下类型的文件：
1. **Python脚本 (.py)**: 主要代码文件
2. **配置文件 (.json, .yaml)**: 任务配置
3. **数据文件 (.csv, .txt)**: 处理的数据
4. **报告文件 (.md, .html)**: 分析报告
5. **可视化文件 (.png, .jpg)**: 图表和图形
### 输出文件命名规则
生成的输出文件遵循以下命名规则：
```
{task_name}_{timestamp}.{extension}
```
**示例**: `data_analysis_20240313_143022.py`
### 执行环境
AipyPro在以下环境中执行代码：
1. **Python版本**: 自动检测并使用系统Python
2. **依赖管理**: 自动安装所需的Python包
3. **工作目录**: 在当前目录执行
4. **权限**: 需要适当的文件系统权限
## 🔍 故障排除
### 常见问题及解决方案
#### 问题1: 命令执行无响应
**可能原因**:
- AipyPro未正确安装
- Python环境问题
- 网络连接问题
**解决方案**:
```bash
# 检查AipyPro安装
aipypro --version
# 检查Python环境
python --version
# 使用verbose模式查看详细输出
aipypro run --verbose "test command"
```
#### 问题2: 生成的代码有错误
**可能原因**:
- 指令描述不清晰
- 依赖包缺失
- 环境配置问题
**解决方案**:
```bash
# 提供更详细的指令
aipypro run "create a Python function to calculate factorial with error handling"
# 使用debug风格
aipypro run --style debug "your instruction"
# 分步执行复杂任务
```
#### 问题3: 依赖包安装失败
**可能原因**:
- 网络问题
- 包名错误
- 权限不足
**解决方案**:
```bash
# 在指令中指定依赖
aipypro run "using pandas and matplotlib, analyze the data"
# 手动安装依赖
pip install package_name
# 使用helper脚本
python scripts/aipypro_helper.py --install-packages pandas
```
#### 问题4: 执行超时
**可能原因**:
- 任务过于复杂
- 系统资源不足
- 无限循环
**解决方案**:
```bash
# 增加超时时间
aipypro run --timeout 600 "complex task"
# 简化任务，分步执行
aipypro run "step 1: load data"
aipypro run "step 2: process data"
# 检查系统资源
```
## 💡 最佳实践
### 指令编写最佳实践
#### 实践1: 清晰具体
- **推荐**: `"create a function to calculate the average of a list of numbers"`
- **不推荐**: `"calculate average"`
#### 实践2: 包含上下文
- **推荐**: `"analyze sales data from CSV file and create bar chart"`
- **不推荐**: `"analyze data"`
#### 实践3: 指定依赖
- **推荐**: `"using pandas, read CSV file and calculate statistics"`
- **不推荐**: `"read CSV file"`
### 参数使用最佳实践
#### 实践1: 根据任务选择角色
- **数据分析**: `--role data_scientist`
- **系统管理**: `--role system_admin`
- **学习目的**: `--role student`
#### 实践2: 根据需求选择风格
- **生产环境**: `--style professional`
- **调试目的**: `--style debug`
- **快速原型**: `--style simple`
#### 实践3: 指定任务类型
- **机器学习**: `--task machine_learning`
- **Web开发**: `--task web_development`
- **自动化**: `--task automation`
### 工作流最佳实践
#### 实践1: 分步执行复杂任务
```bash
# 步骤1: 数据加载
aipypro run "load data from CSV file"
# 步骤2: 数据清洗
aipypro run "clean data: remove duplicates, fill missing values"
# 步骤3: 数据分析
aipypro run "analyze data and generate statistics"
# 步骤4: 可视化
aipypro run "create visualization charts"
```
#### 实践2: 使用配置文件
```bash
# 生成任务配置
python scripts/aipypro_helper.py --generate-config my_task "Task description"
# 使用配置执行任务
# (根据配置执行相应命令)
```
#### 实践3: 定期清理
```bash
# 清理30天前的旧文件
python scripts/aipypro_helper.py --clean-old-files --days 30
```
## 📊 命令执行流程
### 执行步骤
1. **解析指令**: AipyPro解析自然语言指令
2. **生成代码**: 根据指令生成Python代码
3. **安装依赖**: 自动安装所需的Python包
4. **执行代码**: 在安全环境中执行生成的代码
5. **输出结果**: 显示执行结果和生成的文件
### 执行结果
命令执行后返回以下信息：
1. **执行状态**: 成功或失败
2. **输出内容**: 标准输出和错误输出
3. **生成文件**: 创建的文件列表
4. **执行时间**: 命令执行耗时
## 🔗 相关资源
### 辅助工具
- **aipypro_helper.py**: Python辅助脚本，提供额外功能
- **使用方式**: `python scripts/aipypro_helper.py --help`
### 文档资源
- **SKILL.md**: 完整技能描述和使用指南
- **examples.md**: 丰富的使用示例
- **README.md**: 项目概述和快速开始指南
### 社区支持
- **GitHub仓库**: [AipyPro项目地址]
- **问题反馈**: [GitHub Issues]
- **讨论区**: [社区论坛]
## 📝 版本历史
### v1.0.0 (2024-03-13)
- 初始版本发布
- 包含基本命令参考
- 提供使用示例和最佳实践
### v1.1.0 (计划中)
- 增加更多高级命令
- 优化参数说明
- 添加更多故障排除指南
## 👥 贡献指南
欢迎贡献改进建议：
1. 在GitHub仓库提交Issue
2. 创建Pull Request
3. 参与社区讨论
## 📄 许可证
本文档采用MIT许可证。
---
*文档维护: AipyPro技能包团队*
*如有问题，请参考详细文档或联系支持*
