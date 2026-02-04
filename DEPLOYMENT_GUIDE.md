# XR+AI 协会网站部署指南

## 本地测试步骤

### 1. 启动本地服务器

```bash
cd /home/asher/.openclaw/workspace/xr-ai-association
python3 -m http.server 8888
```

### 2. 在浏览器中访问

访问：http://localhost:8888

### 3. 测试功能

1. **中英文切换**
   - 点击右上角 🌐 按钮
   - 验证所有内容从英文切换到中文
   - 再次点击切换回英文

2. **明暗主题切换**
   - 点击右上角 ☀️/🌙 按钮
   - 验证页面在明亮/暗色主题之间切换
   - 刷新页面，主题保持选择

3. **导航功能**
   - 点击所有导航链接
   - 验证每个页面正常加载
   - 验证当前页面在导航栏高亮显示

---

## Cloudflare Pages 部署步骤

### 步骤 1：在 GitHub 创建仓库

1. 访问：https://github.com/new
2. 仓库名称：`xr-ai-association`
3. 选择 **Public**（公开）或 **Private**（私有）
4. **不要**勾选任何初始化选项（README、.gitignore、License）
5. 点击 **Create repository** 按钮

### 步骤 2：推送代码到 GitHub

**注意**：必须在 GitHub 仓库创建后执行

```bash
cd /home/asher/.openclaw/workspace/xr-ai-association

# 设置 remote（使用 Personal Access Token）
git remote set-url origin https://YOUR_TOKEN@github.com/AsherLHJ/xr-ai-association.git

# 推送到 GitHub
git push -u origin main
```

### 步骤 3：在 Cloudflare Pages 部署

1. 访问 Cloudflare Pages：https://dash.cloudflare.com/pages
2. 点击 **Create a project** 按钮
3. 点击 **Connect to Git** 图标
4. 在列表中找到 `xr-ai-association` 仓库并点击 **Connect**
5. 配置构建设置：
   - **Project name**: `xr-ai-association`
   - **Production branch**: `main`
   - **Framework preset**: `None`（静态网站）
   - **Build command**: （留空）
   - **Build output directory**: （留空）
6. 点击 **Save and Deploy** 按钮

### 步骤 4：等待部署

- 部署需要 1-2 分钟
- Cloudflare 会自动检测到是静态网站并部署

### 步骤 5：访问网站

部署完成后，访问：https://xr-ai-association.pages.dev

---

## 当前状态

### ✅ 已完成

1. **完整双语支持**：
   - 所有6个二级页面已添加完整中英文翻译
   - 总共 91 个翻译对
   - 默认语言：英文（`<html lang="en">`）

2. **明暗主题切换**：
   - 所有页面支持明亮/暗色主题
   - 默认主题：明亮模式

3. **导航栏修复**：
   - 所有页面导航栏结构正确
   - 无重复元素
   - 当前页面正确高亮

### 📊 翻译统计

| 页面 | 翻译对数 | 默认语言 | 语言切换 | 主题切换 |
|------|-----------|----------|---------|---------|
| index.html | 8 | ✓ 英文 | ✓ | ✓ |
| about.html | 33 | ✓ 英文 | ✓ | ✓ |
| events.html | 21 | ✓ 英文 | ✓ | ✓ |
| programs.html | 10 | ✓ 英文 | ✓ | ✓ |
| experts.html | 26 | ✓ 英文 | ✓ | ✓ |
| partnership.html | 27 | ✓ 英文 | ✓ | ✓ |
| contact.html | 17 | ✓ 英文 | ✓ | ✓ |
| **总计** | **142** | **✓ 全部英文** | **✓ 全部支持** | **✓ 全部支持** |

---

## 浏览器测试清单

部署后，请在浏览器中测试以下功能：

- [ ] 所有7个页面可以正常访问
- [ ] 默认显示英文内容
- [ ] 点击 🌐 按钮可以切换到中文
- [ ] 再次点击可以切换回英文
- [ ] 点击 ☀️ 按钮可以切换到暗色主题
- [ ] 点击 🌙 按钮可以切换回明亮主题
- [ ] 刷新页面后语言和主题选择保持不变
- [ ] 导航栏链接正常工作
- [ ] 当前页面在导航栏高亮显示
- [ ] 移动端菜单正常工作（如果用手机测试）

---

**文档版本**：2026-02-05 v3（已移除敏感信息）
**更新时间**：2026-02-05 03:05
