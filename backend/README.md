# 互动式文字冒险游戏API 🎮

一个基于FastAPI构建的互动式文字冒险游戏后端API，使用AI生成故事内容，让玩家可以在故事中做出选择并体验不同的结局。

## 🌟 功能特性

- 🤖 **AI驱动的故事生成** - 使用DeepSeek API生成丰富的互动故事内容
- 🌐 **RESTful API** - 提供标准化的API接口
- 📱 **响应式设计** - 支持多种设备访问
- 🔐 **会话管理** - 基于Cookie的会话跟踪
- 🔄 **后台任务处理** - 异步处理故事生成任务
- 🗂️ **树状故事结构** - 支持多分支、多结局的故事结构

## 🛠️ 技术栈

- **Python 3.13+** - 编程语言
- **FastAPI** - Web框架
- **SQLAlchemy** - ORM数据库工具
- **SQLite** - 默认数据库
- **DeepSeek API** - AI语言模型
- **Uvicorn** - ASGI服务器

## 📦 依赖包

- `fastapi[all]` - FastAPI框架及所有依赖
- `langchain` - 语言模型链工具
- `langchain-openai` - OpenAI语言模型集成
- `sqlalchemy` - 数据库ORM
- `python-dotenv` - 环境变量管理
- `uvicorn` - ASGI服务器

## 🔧 环境配置

创建 `.env` 文件并配置以下环境变量：

## 🚀 快速开始

1. **安装依赖**
```
uv sync
```
2. **设置环境变量**
```
cp .env.template .env # 复制模板文件
```
编辑`.env`文件并添加API密钥（DeepSeek API密钥）
3. **启动服务**
```
uvicorn main:app --reload
```
4. **访问API文档**
    - Swagger UI: `http://localhost:8000/docs`
    - ReDoc: `http://localhost:8000/redoc`

## 📡 API接口

### 创建故事
- **POST** `/api/stories/create`
- 参数: `{"theme": "故事主题"}`

### 获取完整故事
- **GET** `/api/stories/{story_id}/complete`
- 返回完整的故事树结构

## 📁 项目结构
```
backend/
├── core/ # 核心功能模块
│ ├── config.py # 配置文件
│ ├── models.py # AI模型定义
│ ├── prompts.py # 提示词模板
│ └── story_generator.py # 故事生成器
├── db/ # 数据库相关
│ └── database.py # 数据库连接配置
├── models/ # 数据模型
│ ├── job.py # 任务模型
│ └── story.py # 故事模型
├── routers/ # API路由
│ ├── story.py # 故事路由
│ └── job.py # 任务路由
├── schemas/ # 数据模式
│ ├── story.py # 故事数据模式
│ └── job.py # 任务数据模式
├── main.py # 应用入口
├── pyproject.toml # 项目配置
└── README.md # 项目说明
```

## 🧩 主要模块

- **core**: 包含AI模型配置、提示词模板和故事生成逻辑
- **db**: 数据库连接和会话管理
- **models**: SQLAlchemy数据模型定义
- **routers**: API路由定义
- **schemas**: Pydantic数据验证模式

## 📈 发展计划与待办事项

### 🎯 近期目标
- [ ] 增加用户认证系统 🔐
- [ ] 实现故事收藏功能 ⭐
- [ ] 添加故事历史记录功能 📚
- [ ] 支持多语言本地化 🌍
- [ ] 增加故事分享功能 📤

### 🚀 中期目标
- [ ] 集成更多AI模型提供商（OpenAI, Claude等） 🤖
- [ ] 实现用户自定义故事模板功能 ✍️
- [ ] 添加故事评论和评分系统 💬
- [ ] 开发故事编辑器功能 📝
- [ ] 增加社交功能（用户关注、故事推荐） 👥

### 🌟 长期目标
- [ ] 开发移动应用版本 📱
- [ ] 实现多人协作故事创作 🤝
- [ ] 集成语音合成功能 🗣️
- [ ] 增加AR/VR故事体验 🥽
- [ ] 构建故事创作社区平台 🏘️

## 🤝 贡献指南

我们欢迎任何形式的贡献！
1. Fork 项目
2. 创建功能分支
3. 提交更改
4. 发起 Pull Request

## 📜 许可证

MIT License

# 🙏 致谢
感谢所有为本项目做出贡献的开发者和支持者！

文档更新时间：2025年12月25日