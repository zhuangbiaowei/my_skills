---
name: aipypro
description: This skill should be used when working with AipyPro AI agent to execute Python code via natural language commands. AipyPro is an AI-powered Python execution tool that can generate and run Python code based on natural language instructions.
---
# AipyPro Skill
## 技能概述
### 技能名称
**AipyPro技能包**
### 技能描述
AipyPro技能包是一个专门为AipyPro AI代理设计的综合技能套件，支持通过自然语言命令执行Python代码生成和运行。该技能包提供了完整的命令行参考、实用示例、辅助脚本和最佳实践指南。
### 核心功能
1. **智能代码生成**: 根据自然语言描述自动生成Python代码
2. **文件操作**: 支持文件系统操作、数据处理和分析
3. **系统管理**: 提供系统监控、日志分析等系统管理功能
4. **工作流自动化**: 支持复杂工作流和自动化任务
5. **机器学习支持**: 提供数据预处理、模型训练等ML功能
## 使用场景
### 场景1: 快速原型开发
- **需求**: 快速验证想法或概念
- **示例命令**: `aipypro run "create a function to calculate fibonacci sequence"`
- **适用对象**: 开发者、研究人员、学生
### 场景2: 数据处理与分析
- **需求**: 处理和分析数据集
- **示例命令**: `aipypro run "analyze CSV file and create visualization"`
- **适用对象**: 数据分析师、业务分析师
### 场景3: 系统管理自动化
- **需求**: 自动化系统管理任务
- **示例命令**: `aipypro run "monitor system resources and generate report"`
- **适用对象**: 系统管理员、DevOps工程师
### 场景4: 学习与教育
- **需求**: 学习Python编程和算法
- **示例命令**: `aipypro run "explain binary search algorithm with example"`
- **适用对象**: 学生、编程初学者
## 输入参数
### 基本参数
```yaml
instruction: "自然语言指令"  # 必需参数，描述要执行的任务
```
### 高级参数
```yaml
--style: "代码风格"          # 可选，如"professional", "simple"
--role: "执行角色"          # 可选，如"developer", "analyst"
--task: "任务类型"          # 可选，如"data_analysis", "system_admin"
```
### 参数示例
```bash
# 基本用法
aipypro run "create a function to calculate factorial"
# 带样式参数
aipypro run --style professional "implement binary search algorithm"
# 带角色参数
aipypro run --role data_scientist "analyze time series data"
```
## 输出结果
### 输出类型
1. **代码文件**: 生成的Python脚本文件（.py）
2. **执行结果**: 代码执行的输出结果
3. **报告文件**: 数据分析报告、系统报告等
4. **可视化文件**: 图表、图形等可视化输出
### 输出位置
- 代码文件通常保存在当前工作目录
- 输出文件命名遵循模式: `task_name_timestamp.extension`
- 执行结果直接在终端输出
## 使用示例
### 基础示例
```bash
# 示例1: Hello World
aipypro run "print Hello World"
# 示例2: 简单计算
aipypro run "calculate 7 * 8"
# 示例3: 文件操作
aipypro run "list files in current directory"
```
### 进阶示例
```bash
# 示例4: 数据可视化
aipypro run "create bar chart for sales data"
# 示例5: 系统监控
aipypro run "check disk usage and memory"
# 示例6: 机器学习
aipypro run "train classification model on dataset"
```
### 完整工作流示例
```bash
# 完整的数据分析管道
aipypro run "create complete data pipeline: load data, clean, analyze, visualize"
```
## 安装与配置
### 环境要求
- **Python版本**: 3.8 或更高版本
- **操作系统**: Windows, macOS, Linux
- **依赖包**: 根据任务需要自动安装
### 安装步骤
1. **验证AipyPro安装**
```bash
aipypro --version
```
2. **安装技能包依赖**
```bash
# 使用helper脚本安装依赖
python scripts/aipypro_helper.py --install-deps
```
3. **测试技能包**
```bash
# 运行测试命令
aipypro run "test basic functionality"
```
### 配置选项
```yaml
# 配置文件位置: ~/.aipypro/config.yaml
settings:
  default_style: "professional"
  auto_save: true
  output_dir: "./aipypro_output"
  log_level: "INFO"
```
## 最佳实践
### 实践1: 清晰的指令描述
- **推荐**: "create a function to calculate the average of a list of numbers"
- **不推荐**: "calculate average"
### 实践2: 分步执行复杂任务
```bash
# 步骤1: 数据加载
aipypro run "load CSV file and inspect structure"
# 步骤2: 数据清洗
aipypro run "clean data by removing duplicates and filling missing values"
# 步骤3: 分析
aipypro run "analyze data and generate statistics"
```
### 实践3: 使用适当的参数
```bash
# 使用角色参数提高代码质量
aipypro run --role senior_developer "implement production-ready API"
# 使用样式参数控制输出格式
aipypro run --style concise "create summary report"
```
### 实践4: 结果验证
```bash
# 生成测试代码
aipypro run "create unit tests for the generated function"
# 验证输出
aipypro run "validate the analysis results"
```
## 故障排除
### 常见问题1: 命令执行失败
**症状**: 命令执行无响应或报错
**解决方案**:
1. 检查AipyPro安装: `aipypro --version`
2. 验证Python环境: `python --version`
3. 查看详细错误: `aipypro run --verbose "your command"`
### 常见问题2: 生成的代码有错误
**症状**: 生成的Python代码无法运行
**解决方案**:
1. 提供更详细的指令描述
2. 使用`--style debug`参数生成调试信息
3. 分步执行复杂任务
### 常见问题3: 依赖包缺失
**症状**: 导入错误或模块未找到
**解决方案**:
1. 使用helper脚本安装依赖
```bash
python scripts/aipypro_helper.py --install-packages pandas matplotlib
```
2. 在指令中指定依赖
```bash
aipypro run "using pandas, analyze the data"
```
### 常见问题4: 性能问题
**症状**: 执行缓慢或内存占用高
**解决方案**:
1. 简化指令，分步执行
2. 使用`--task optimize`参数
3. 检查系统资源使用情况
## 技能包结构
### 目录结构
```
aipypro-skill/
├── SKILL.md                    # 主技能文档（本文件）
├── README.md                   # 项目README
├── scripts/
│   └── aipypro_helper.py      # Python辅助脚本
├── references/
│   ├── command_reference.md   # 完整命令参考
│   └── examples.md           # 使用示例
└── assets/
    └── task_template.json     # 任务配置模板
```
### 文件说明
1. **SKILL.md**: 完整的技能描述和使用指南
2. **aipypro_helper.py**: 辅助脚本，提供额外功能
3. **command_reference.md**: 详细的命令参考文档
4. **examples.md**: 丰富的使用示例
5. **task_template.json**: 任务配置模板
## 版本历史
### v1.0.0 (2024-03-13)
- 初始版本发布
- 包含基础技能文档
- 提供基本示例和命令参考
### v1.1.0 (计划中)
- 增加更多高级示例
- 优化helper脚本功能
- 添加性能优化指南
## 贡献指南
### 如何贡献
1. Fork项目仓库
2. 创建功能分支
3. 提交更改
4. 创建Pull Request
### 代码规范
- 遵循PEP 8代码风格
- 添加适当的注释和文档
- 包含单元测试
### 文档要求
- 使用Markdown格式
- 包含使用示例
- 提供清晰的说明
## 许可证
本项目采用MIT许可证。详细信息请查看LICENSE文件。
## 支持与反馈
### 获取帮助
- 查看详细文档: `references/`目录
- 运行示例: 参考`examples.md`
- 使用helper脚本: `python scripts/aipypro_helper.py --help`
### 报告问题
- GitHub Issues: [项目Issues页面]
- 邮件支持: support@example.com
- 社区论坛: [社区链接]
### 提供反馈
我们欢迎任何形式的反馈，包括:
- 功能建议
- 错误报告
- 使用体验分享
- 改进建议
---
*最后更新: 2024年3月13日*
*维护者: AipyPro技能包团队*
