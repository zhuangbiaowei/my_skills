# agent-browser - Browser Automation Skill

**Description:** 自动化浏览器操作，用于网页浏览、表单填写、截图保存等。适用于需要交互式操作的场景（如登录网站、搜索信息、下载文件）。  
**Location:** `~/skills/agent-browser/SKILL.md`  
**Prerequisites:** Chrome/Chromium-based browser (Chrome, Brave, Edge)

---

## 🚀 快速开始

```bash
# 打开网页
agent-browser open https://www.baidu.com

# 点击元素（支持 CSS selector 或 @ref）
agent-browser click "@e1"

# 填写表单
agent-browser fill '[name="wd"]' "搜索关键词"

# 按键盘键
agent-browser press Enter
```

---

## 📋 核心命令分类

### **导航与交互**
| 命令 | 说明 | 示例 |
|------|------|------|
| `open <url>` / `goto` / `navigate` | 打开网页 | `agent-browser open https://example.com` |
| `click <sel>` | 点击元素（支持 `--new-tab`） | `agent-browser click "@e1" --new-tab` |
| `dblclick <sel>` | 双击元素 | - |
| `fill <sel> <text>` | **清空并填充**表单字段 | `agent-browser fill '#email' 'test@test.com'` |
| `type <sel> <text>` | 逐字输入（模拟打字） | `agent-browser type '.input' 'Hello'` |
| `press <key>` / `key` | 按键盘键 | `agent-browser press Enter`<br/>`agent-browser press Control+a` |
| `hover <sel>` | 鼠标悬停 | - |
| `focus <sel>` | 聚焦元素 | - |
| `select <sel> <val...>` | 下拉框选择选项 | - |
| `check <sel>` / `uncheck <sel>` | 勾选/取消复选框 | - |
| `scroll <dir> [px]` | 滚动页面（up/down/left/right）<br/>支持 `--selector <sel>` 指定元素内滚动 | - |
| `scrollintoview <sel>` | 将元素滚动到可视区域 | - |
| `drag <src> <dst>` | 拖放操作 | - |
| `upload <sel> <files>` | 上传文件 | - |

---

### **信息获取**
| 命令 | 说明 | 示例 |
|------|------|------|
| `screenshot [path]` / `-f` | 截图（默认当前页，`--full` 全页面） | `agent-browser screenshot page.png --full` |
| `pdf <path>` | 保存为 PDF | - |
| `snapshot` | **生成无障碍树**（带 refs，如 @e1, @e2）<br/>→ 用于发现元素引用 | `agent-browser snapshot -i` |
| `eval <js>` | 执行 JavaScript | `agent-browser eval "document.title"` |
| `get text/html/value/title/url <sel>` | 获取内容/属性值 | `agent-browser get title`<br/>`agent-browser get url`<br/>`agent-browser get value '#username'` |
| `count <sel>` / `box <sel>` / `styles <sel>` | 元素计数、坐标框、样式信息 | - |

---

### **智能查找（最强大！）**  
**语义化定位，无需手写 CSS selector！**

```bash
# 按角色 + 名称查找并操作
agent-browser find role button click --name "Submit"

# 按标签文本查找并填充表单
agent-browser find label "Email" fill "test@test.com"

# 按图片 ALT 属性点击
agent-browser find alt "Logo" click

# 其他查找方式：
find text <text> <action>          # 按可见文字
find placeholder <ph> <action>     # 按占位符文本
find testid <id> <action> [value]  # 按 data-testid 属性
find first/last/nth <sel> <action> # 取第 N 个匹配元素

# 示例：点击第二个卡片上的按钮
agent-browser find nth 2 ".card" click --name "详情"
```

**支持的 `role`：** button, textbox, link, checkbox, radio, combobox, listbox, option, heading (h1-h6), image, table, grid, dialog...  
（参考：[WAI-ARIA roles](https://www.w3.org/TR/wai-aria-1.2/#roles)）

---

### **等待策略**
```bash
# 等元素出现
agent-browser wait ".loading-spinner"

# 等特定文字显示
agent-browser wait --text "Welcome to your account!"

# 等 URL 匹配模式（支持通配符）
agent-browser wait --url "**/dashboard/**"

# 等页面加载完成（networkidle = 网络空闲，即所有资源加载完毕）
agent-browser wait --load networkidle

# 等待 JS 条件满足
agent-browser wait --fn "() => document.querySelector('.data-loaded')"

# 等下载完成
agent-browser wait --download ~/downloads/report.pdf
```

---

### **高级功能**

#### 📥 **下载管理**
```bash
# 点击元素触发下载
agent-browser download ".download-btn" "~/Downloads/file.zip"

# 设置默认下载目录（环境变量）
export AGENT_BROWSER_DOWNLOAD_PATH=~/Downloads

# 等待任意文件下载完成
agent-browser wait --download
```

#### 🍪 **Cookies & Storage**
```bash
cookies                          # 查看所有 cookies
cookies set <name> <val>         # 设置 cookie
cookies clear                    # 清空所有

storage local [key]              # localStorage（不传 key = 全部）
storage local set <k> <v>        # 设置值
storage session                  # sessionStorage 同上
```

#### 🌐 **网络拦截**
```bash
network route "https://api.example.com/**" --body '{"status":"mocked"}'   # Mock 响应
network route "https://ads.example.com/**" --abort                         # 阻止请求
network requests                                                         # 查看已追踪的请求
network unroute "..."                                                    # 移除拦截规则
```

#### 📑 **多标签/窗口**
```bash
tab                   # 列出所有标签页
tab new [url]         # 新建标签（可选 URL）
tab <n>               # 切换到第 N 个标签（0-indexed）
tab close [<n>]       # 关闭指定标签，不传 = 当前

window new            # 新开浏览器窗口
```

#### 🖼️ **媒体录制**
```bash
trace start [path]           # 开始录制 trace（调试用）
trace stop [path]            # 停止并保存

profiler start / stop        # Chrome DevTools 性能分析

record start <path.webm>     # 录屏（WebM 格式）
record stop                  # 停止录制
```

#### 🔐 **Auth Vault**（凭证管理）
```bash
# 保存登录配置
echo "mypassword" | agent-browser auth save github \
  --url https://github.com/login \
  --username myuser \
  --password-stdin
  
agent-browser auth login github    # 一键恢复登录状态

auth list                          # 列出所有凭证 profile
auth show <name>                   # 查看详情（不含密码）
auth delete <name>                 # 删除配置
```

**可选参数：** `--username-selector`, `--password-selector`, `--submit-selector`  
→ 自定义表单字段和提交按钮的 CSS selector。

---

### **全局选项**
```bash
# 会话管理（隔离运行环境）
agent-browser --session my-session open https://example.com

# 状态持久化（cookies + localStorage）
agent-browser --session-name "my-login" open https://app.example.com

# 浏览器配置
--profile <path>           # 自定义用户数据目录
--user-agent <ua-string>   # 伪装 User-Agent
--proxy http://xxx:port    # 代理服务器（支持 @host）
--color-scheme dark/light  # 强制深色/浅色模式

# 安全设置
--ignore-https-errors      # 忽略 HTTPS 证书错误
--allowed-domains a.com,b.com  # 限制可访问域名

# 输出控制
--json                     # JSON 格式输出（适合脚本解析）
--max-output <chars>       # 截断页面内容长度
```

---

## 🎯 典型用例

### **1. 搜索并截图**
```bash
agent-browser open baidu.com && \
fill '[name="wd"]' "最新 AI 新闻" && \
press Enter && \
wait --text "AI 技术发展趋势" && \
screenshot search-results.png --full
```

### **2. 登录并获取状态**
```bash
agent-browser open https://github.com/login && \
fill '[name="login"]' "$GITHUB_USER" && \
press Tab && \
type "[name='password']" "$GITHUB_PASSWORD" && \
click 'input[type=submit]' && \
wait --url "**/settings**" && \
get title  # 验证登录成功
```

### **3. 下载文件并等待完成**
```bash
agent-browser open https://example.com/download && \
download '.btn-download' ~/Downloads/report.pdf && \
wait --download ~/Downloads/report.pdf
```

### **4. 表单自动化（智能查找）**
```bash
# 语义化操作，无需知道具体 CSS selector！
agent-browser find label "用户名" fill "$USERNAME" && \
agent-browser find placeholder "请输入密码" type "$PASSWORD" && \
agent-browser find role button click --name "登录" && \
wait --text "欢迎回来"
```

---

## ⚠️ 注意事项

1. **浏览器要求**：必须安装 Chrome/Chromium（不支持 Firefox/Safari）  
   → `sudo apt install chromium-browser` (Ubuntu) / `brew install chromium` (macOS)

2. **Ref 引用机制**：使用 `snapshot --annotate -i` 生成元素列表，后续用 `@e1`, `@e2`... 引用

3. **等待策略很重要**：网页加载速度不一，务必加 `wait` 避免操作未就绪的元素

4. **命令行参数格式**：  
   ❌ `agent-browser open https://example.com` (错误)  
   ✅ `agent-browser open "https://example.com"` (正确 - URL 需引号包裹)

5. **命令链式执行**：用 `&&` 连接多个操作，浏览器后台守护进程会保持运行状态

---

## 📚 参考资源
- 官方文档：https://agent-browser.dev/commands  
- Playwright 选择器语法：https://playwright.dev/docs/selectors  
- WAI-ARIA roles: https://www.w3.org/TR/wai-aria-1.2/#roles  

---

*最后更新：2026-03-03* 🦐