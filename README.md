# 🦐 OpenClaw Skills - My Custom Toolkit

个人化的技能集合，用于增强 OpenClaw 的功能。每个 skill 都是一个独立的模块，包含实现代码、文档和工具说明。

---

## 📁 目录结构

```
~/skills/
├── README.md                    # ← 你正在看的这个文件
└── {skill-name}/
    ├── SKILL.md                 # ← OpenClaw 会读取此文件作为技能描述
    └── [可选] scripts/, assets/ # 相关的脚本、配置文件等
```

---

## 🎯 如何使用 Skills？

### **方式一：OpenClaw 自动识别**（推荐）

当你在对话中提到某个功能时，OpenClaw 会自动扫描 `skills/*.md` 文件并匹配相关技能。例如：

> "帮我配置 SSH" → OpenClaw 会读取 `~/skills/ssh/SKILL.md`  
> "使用 agent-browser" → OpenClaw 会读取 `~/skills/agent-browser/SKILL.md`

### **方式二：手动指定**（高级）

```bash
openclaw skills list              # 列出所有可用技能
openclaw skills read <name>       # 查看某个技能的文档内容
```

---

## 📚 现有 Skills

| Skill | 功能描述 | SKILL.md 路径 |
|-------|----------|---------------|
| **agent-browser** | 浏览器自动化操作（搜索、截图、表单填写） | `skills/agent-browser/SKILL.md` |
| *(添加更多...)* | *待创建* | - |

---

## 🛠️ 创建一个新 Skill

### **步骤一：目录结构**
```bash
mkdir -p ~/skills/{skill-name}
cd ~/skills/{skill-name}
```

### **步骤二：编写 SKILL.md**（必须！）

OpenClaw 会读取此文件作为技能描述。参考 [agent-browser/SKILL.md](./agent-browser/SKILL.md) 的格式。

#### ✅ **核心要素：**

1. **Description** - 一句话说明这个技能是做什么的
2. **Location** - SKILL.md 所在路径（相对或绝对）
3. **Prerequisites** - 依赖条件（如"需要 Chrome 浏览器"、"需安装 curl"）
4. **Usage Examples** - 典型使用场景和命令示例

#### ❌ **不要写：**
- 个人笔记风格（过于随意或缺乏结构）
- 与技能无关的内容（保持专注在工具/功能上）
- 过时的信息（定期更新文档）

### **步骤三：添加可选资源**

```bash
# 脚本文件
mkdir scripts && touch scripts/setup.sh

# 配置文件模板
touch config.example.json

# 其他辅助材料
README.md (详细教程，SKILL.md 放核心参考)
examples/ (示例代码、用例)
assets/ (图片、图表等)
```

---

## 📖 SKILL.md 最佳实践

### **1. 清晰的标题和描述**
```markdown
# {skill-name} - {功能说明}

**Description:** 一句话概括技能用途  
**Location:** `{path}/SKILL.md`  
**Prerequisites:** 前置条件（如"需要 SSH 密钥配置完成"）
```

### **2. 分类清晰的命令/用法**
使用表格或列表组织：

| 类型 | 说明 | 示例 |
|------|------|------|
| `command1` | ... | `example` |
| `command2` | ... | `--flag value` |

### **3. 典型用例（Use Cases）**
```bash
# 场景一：基础操作
agent-browser open https://... && fill '#input' 'value'

# 场景二：高级功能
auth save profile --url ... --username user --password-stdin
```

### **4. 注意事项和边界条件**
> ⚠️ **注意：** 
> - 某些命令需要 root 权限
> - macOS/Linux 语法差异
> - API key 配置要求

---

## 🔄 维护和更新

1. **定期审查**：每季度检查一次 SKILL.md，删除过时信息
2. **版本记录**：在文件末尾添加更新日志
   ```markdown
   ## Changelog
   - [2026-03-03] 初始创建
   - [2026-03-15] 新增高级用法示例
   ```

3. **测试验证**：确保文档中的命令能实际运行（如果可能）

---

## 🎨 贡献指南（可选）

如果你希望分享自己的 skills，可以：

1. Fork [OpenClaw Skills Hub](https://github.com/openclaw/skills)
2. 创建你的技能模块
3. Submit Pull Request 到官方仓库

或者保留为个人私有库（如本目录），按需使用。

---

## 🤔 FAQ

**Q: OpenClaw 什么时候会读取 SKILL.md？**  
A: 当对话内容匹配技能的描述关键词时，系统会自动加载并应用相关技能的知识。

**Q: 如何确认某个 skill 是否被识别？**  
A: 运行 `openclaw skills list` 查看所有已注册的技能和它们的描述摘要。

**Q: SKILL.md 有什么格式要求吗？**  
A: Markdown 即可！推荐使用清晰的标题、列表和代码块，避免复杂的表格（某些显示环境可能不支持）。

---

## 📞 联系与维护者

- **维护者:** 庄表伟
- **创建时间:** 2026-03-03
- **版本:** v1.0

*最后更新：2026-03-03* 🦐
