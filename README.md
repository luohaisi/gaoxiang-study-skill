# 软考高项学习助手 (Gaoxiang Study)

一个基于 OpenClaw 的 Agent Skill，帮助备考软考高项（信息系统项目管理师）。

## 📚 功能特性

### 1. 智能教材查询
- 完整加载 24 章软考高项教材
- 根据问题关键词自动定位章节
- 引用原文并给出总结答案

### 2. 问题归档系统
- 自动记录每个问题到档案
- 重复提问时提示历史答案
- 追踪复习次数，识别薄弱环节

### 3. 每日定时复习
- 每天早上 8 点自动推送 3-5 个问题
- 基于艾宾浩斯遗忘曲线安排复习
- 通过飞书/钉钉直接接收

### 4. 对话总结存档
- 每次学习对话自动总结
- 形成个人专属复习笔记

## 📁 文件结构

```
gaoxiang-study/
├── SKILL.md                      # 技能定义和使用说明
├── README.md                     # 本文件
├── references/                   # 教材内容
│   ├── index.md                 # 章节索引和关键词映射
│   ├── 第1章_信息化发展.md
│   ├── 第2章_信息技术发展.md
│   ├── ... (共24章)
│   └── 第24章_法律法规与标准规范.md
├── scripts/
│   └── daily_review.py          # 定时推送脚本
└── assets/
    ├── questions/
    │   └── archive.json         # 问题档案
    └── summaries/
        └── conversations.json   # 对话总结
```

## 📖 章节列表

| 章节 | 内容 |
|------|------|
| 第1-5章 | 信息化基础（信息化发展、信息技术、系统治理、管理、工程）|
| 第6-7章 | 项目管理基础（概论、立项管理）|
| 第8-17章 | 十大知识领域（整合、范围、进度、成本、质量、资源、沟通、风险、采购、干系人）|
| 第18-24章 | 高级主题（绩效域、配置变更、高级项目管理、管理科学、组织治理、组织管理、法律法规）|

## 🚀 安装方法

### 1. 解压到 OpenClaw 技能目录

```bash
# 下载技能包
wget https://github.com/yourusername/gaoxiang-study/releases/download/v1.0.0/gaoxiang-study.tar.gz

# 解压到 OpenClaw 工作目录
tar -xzf gaoxiang-study.tar.gz -C ~/.openclaw/workspace/
```

### 2. 配置定时任务

```bash
# 查看定时任务
openclaw cron list

# 添加每日复习任务（已内置，如需修改）
openclaw cron add --name gaoxiang-daily-review \
  --schedule "0 8 * * *" \
  --payload "执行高项每日复习推送任务" \
  --delivery channel=feishu,to=<你的用户ID>
```

### 3. 测试定时任务

⚠️ **重要**：安装后务必测试定时任务是否正常工作！

```bash
# 手动触发测试
openclaw cron run <任务ID>

# 检查是否收到飞书消息
```

**常见问题**：
- 如果收不到推送，可能是 `channel` 或 `target` 配置错误
- 检查 `scripts/daily_review.py` 中的飞书用户 ID
- 参考 Issue #1 修复方法

## 💬 使用方法

### 基本提问

直接问任何高项相关问题：

```
用户：什么是WBS？怎么分解？
AI：【第9章 项目范围管理】WBS是工作分解结构...
    分解步骤：1.识别可交付成果 2.确定结构...
    （已记录到问题档案）
```

### 复习推送

每天早上 8 点自动收到：

```
📚 高项复习提醒

早上好！今天来复习几个问题：

1. 【第9章】什么是WBS？怎么分解？
   💡 答案要点：WBS是工作分解结构...

2. 【第9章】WBS如何与控制账户结合使用
   💡 答案要点：工作包是WBS最低层...

回复题号查看详细答案，或者直接告诉我你的答案来检验学习效果！
```

### 命令行查询

```bash
# 查看定时任务
openclaw cron list

# 查看任务运行历史
openclaw cron runs <jobId>

# 手动触发推送
openclaw cron run <jobId>
```

## 🛠️ 技术架构

- **OpenClaw AgentSkill** - 技能框架
- **Cron 调度** - 定时任务
- **飞书/钉钉集成** - 消息推送
- **Markdown 教材** - 24章完整内容

## ⚠️ 注意事项

1. **定时任务测试**：安装后务必测试早上8点推送是否正常
2. **飞书配置**：需要正确配置飞书用户 ID 才能收到推送
3. **复习计数**：每个问题默认复习3次后不再推送
4. **依赖工具**：可选安装 `obsidian-cli` 用于 Obsidian 同步

## 🔧 故障排查

### 定时任务不推送

检查 `scripts/daily_review.py` 中的配置：
- `USER_ID` 是否为你的飞书用户 ID
- `openclaw message send` 命令参数是否正确

### 问题档案为空

需要先提问几个问题，档案才有内容推送。

## 📄 许可证

MIT License - 自由使用、修改和分发

## 🙏 致谢

- 软考高项教材内容源自官方考试大纲
- 基于 OpenClaw 平台构建
- 感谢 Kimi AI 提供的文档处理能力

## 📞 联系

如有问题，请在 GitHub Issues 中反馈，或联系维护者。

---

**备考不是一个人的战斗，让 AI 成为你的记忆外挂。** ❤️‍🔥