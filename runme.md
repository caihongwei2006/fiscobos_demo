# 🚀 FiscoBOS农产品溯源系统 - 快速安装指南

欢迎使用FiscoBOS农产品溯源系统！本指南将帮助您快速搭建和运行项目。

## 📋 系统要求

### 必需环境
- **操作系统**: Linux (Ubuntu 20.04+) / macOS / Windows 10+
- **Python**: 3.8 或更高版本
- **Git**: 用于代码管理
- **网络**: 稳定的互联网连接

### 推荐配置
- **内存**: 4GB RAM 或更多
- **存储**: 至少 2GB 可用空间
- **处理器**: 双核 2.0GHz 或更高

## 🛠️ 安装步骤

### 第一步：环境检查

首先检查您的系统是否满足要求：

```bash
# 检查Python版本 (需要3.8+)
python3 --version

# 检查Git是否安装
git --version

# 检查pip是否可用
pip3 --version
```

如果缺少任何工具，请先安装：

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install python3 python3-pip git sqlite3
```

**macOS:**
```bash
# 安装Homebrew (如果没有)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 安装依赖
brew install python3 git sqlite3
```

**Windows:**
- 从 [Python官网](https://www.python.org/downloads/) 下载并安装Python 3.8+
- 从 [Git官网](https://git-scm.com/download/win) 下载并安装Git

### 第二步：获取项目代码

```bash
# 克隆项目到本地
git clone <repository-url>
cd fiscobos_demo

# 查看项目结构
ls -la
```

### 第三步：创建虚拟环境

**强烈推荐使用虚拟环境以避免依赖冲突！**

```bash
# 创建虚拟环境
python3 -m venv myenv

# 激活虚拟环境
# Linux/macOS:
source myenv/bin/activate

# Windows:
# myenv\Scripts\activate

# 确认虚拟环境已激活 (命令行前应显示 (myenv))
which python
```

### 第四步：安装项目依赖

```bash
# 升级pip到最新版本
pip install --upgrade pip

# 安装项目依赖
pip install -r requirements.txt

# 验证关键包是否安装成功
python -c "import flask, web3, sqlite3; print('✅ 核心依赖安装成功')"
```

### 第五步：配置项目

#### 5.1 检查配置文件

```bash
# 查看配置文件
ls config/
cat config/app_config.py
```

#### 5.2 更新配置（如需要）

编辑 `config/app_config.py`：
```python
DATABASE_URI = 'sqlite:///database/products.db'  # 数据库路径
DEBUG = True                                      # 开发模式
SECRET_KEY = 'your_secret_key_here'              # 请更改为随机字符串
```

### 第六步：初始化数据库

```bash
# 运行数据库初始化脚本
python3 scripts/init_database.py

# 验证数据库是否创建成功
ls -la database/
sqlite3 database/products.db ".tables"
```

您应该看到以下输出：
```
products      suppliers     transactions
```

### 第七步：启动应用

```bash
# 启动Flask应用
python3 src/main.py
```

如果一切正常，您将看到类似输出：
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### 第八步：验证安装

打开浏览器访问：
- **主页**: http://localhost:5000
- **API测试**: http://localhost:5000/api/products

## 🧪 运行测试

确保项目正常工作：

```bash
# 运行所有测试
python -m pytest tests/ -v

# 运行特定测试
python -m pytest tests/test_database.py -v
```

## 🔧 常见问题解决

### 问题1：Python版本不兼容
```bash
# 错误：Python版本过低
# 解决：安装Python 3.8+
sudo apt install python3.8 python3.8-venv
python3.8 -m venv myenv
```

### 问题2：依赖安装失败
```bash
# 错误：某些包安装失败
# 解决：更新pip并重试
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt --no-cache-dir
```

### 问题3：数据库初始化失败
```bash
# 错误：找不到schema.sql
# 解决：确保在项目根目录运行
pwd  # 应该显示 .../fiscobos_demo
python3 scripts/init_database.py
```

### 问题4：端口被占用
```bash
# 错误：Address already in use
# 解决：更改端口或停止占用进程
# 查找占用进程
lsof -i :5000
# 或者使用不同端口启动
python3 src/main.py --port 5001
```

### 问题5：权限问题
```bash
# 错误：Permission denied
# 解决：检查文件权限
chmod +x scripts/init_database.py
# 或使用sudo (不推荐在虚拟环境中)
```

## 📚 开发指南

### 项目结构说明
```
fiscobos_demo/
├── src/                    # 源代码
│   ├── api/               # API接口
│   ├── blockchain/        # 区块链相关
│   ├── database/          # 数据库管理
│   ├── web/              # 前端文件
│   └── main.py           # 应用入口
├── config/                # 配置文件
├── scripts/               # 工具脚本
├── tests/                 # 测试文件
├── database/              # 数据库文件
└── requirements.txt       # 依赖列表
```

### 开发模式启动
```bash
# 启用调试模式
export FLASK_ENV=development
export FLASK_DEBUG=1
python3 src/main.py
```

### 添加新功能
1. 在相应模块添加代码
2. 编写测试用例
3. 运行测试确保通过
4. 更新文档

## 🚀 生产部署

### 使用Gunicorn部署
```bash
# 安装Gunicorn
pip install gunicorn

# 启动生产服务器
gunicorn -w 4 -b 0.0.0.0:5000 src.main:app
```

### 使用Docker部署
```bash
# 构建镜像
docker build -t fiscobos-app .

# 运行容器
docker run -p 5000:5000 fiscobos-app
```

## 📞 获取帮助

如果遇到问题，请：

1. **检查日志**: 查看终端输出的错误信息
2. **查看文档**: 阅读项目README.md
3. **运行测试**: 确保基础功能正常
4. **联系团队**: 向项目负责人报告问题

### 有用的命令
```bash
# 查看虚拟环境中安装的包
pip list

# 生成新的requirements.txt
pip freeze > requirements.txt

# 清理Python缓存
find . -type d -name __pycache__ -delete

# 重置数据库
rm database/products.db
python3 scripts/init_database.py
```

## ✅ 安装完成检查清单

- [ ] Python 3.8+ 已安装
- [ ] 虚拟环境已创建并激活
- [ ] 项目依赖已安装
- [ ] 数据库已初始化
- [ ] 应用可以正常启动
- [ ] 可以访问 http://localhost:5000
- [ ] 测试通过

**恭喜！您已成功安装FiscoBOS农产品溯源系统！** 🎉

---

**下一步**: 阅读项目文档了解如何使用各项功能，或开始开发新特性。

## 🔐 安全注意事项

### 开发环境
- 确保 `DEBUG = True` 仅在开发环境使用
- 定期更新依赖包以修复安全漏洞
- 不要将敏感信息提交到版本控制

### 生产环境
- 更改默认的 `SECRET_KEY`
- 使用环境变量管理敏感配置
- 启用HTTPS
- 配置防火墙规则

## 🔄 更新项目

当项目有更新时：

```bash
# 拉取最新代码
git pull origin main

# 更新依赖
pip install -r requirements.txt --upgrade

# 重新初始化数据库（如有schema变更）
python3 scripts/init_database.py

# 重启应用
python3 src/main.py
```

## 📊 性能监控

### 基础监控
```bash
# 查看应用进程
ps aux | grep python

# 监控系统资源
top
htop  # 如果已安装

# 查看数据库大小
ls -lh database/products.db
```

### 日志管理
```bash
# 查看应用日志
tail -f logs/app.log  # 如果配置了日志文件

# 清理旧日志
find logs/ -name "*.log" -mtime +7 -delete
```

## 🌐 网络配置

### 局域网访问
如需让团队其他成员访问：

```bash
# 启动时绑定到所有接口
python3 src/main.py --host 0.0.0.0 --port 5000
```

然后其他人可以通过您的IP地址访问：`http://YOUR_IP:5000`

### 防火墙设置
```bash
# Ubuntu/Debian
sudo ufw allow 5000

# CentOS/RHEL
sudo firewall-cmd --add-port=5000/tcp --permanent
sudo firewall-cmd --reload
```

## 🎯 快速验证脚本

创建一个快速验证脚本来检查安装：

```bash
# 创建验证脚本
cat > verify_installation.py << 'EOF'
#!/usr/bin/env python3
import sys
import subprocess
import sqlite3
import requests
import time

def check_python_version():
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print("✅ Python版本检查通过")
        return True
    else:
        print("❌ Python版本过低，需要3.8+")
        return False

def check_database():
    try:
        conn = sqlite3.connect('database/products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        conn.close()
        if len(tables) >= 3:
            print("✅ 数据库检查通过")
            return True
        else:
            print("❌ 数据库表不完整")
            return False
    except Exception as e:
        print(f"❌ 数据库检查失败: {e}")
        return False

def check_server():
    try:
        # 启动服务器进程
        import subprocess
        import time
        proc = subprocess.Popen([sys.executable, 'src/main.py'],
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE)
        time.sleep(3)  # 等待服务器启动

        # 测试连接
        response = requests.get('http://localhost:5000', timeout=5)
        proc.terminate()

        if response.status_code == 200:
            print("✅ 服务器检查通过")
            return True
        else:
            print("❌ 服务器响应异常")
            return False
    except Exception as e:
        print(f"❌ 服务器检查失败: {e}")
        return False

if __name__ == "__main__":
    print("🔍 开始验证安装...")
    checks = [
        check_python_version(),
        check_database(),
        # check_server()  # 可选，需要时取消注释
    ]

    if all(checks):
        print("🎉 所有检查通过！安装成功！")
    else:
        print("⚠️  部分检查失败，请检查安装步骤")
EOF

# 运行验证
python3 verify_installation.py
```

## 📱 移动端测试

如需在移动设备上测试：

1. 确保设备连接到同一WiFi网络
2. 启动应用时使用 `--host 0.0.0.0`
3. 在移动浏览器中访问：`http://YOUR_COMPUTER_IP:5000`

## 🔧 IDE配置建议

### VS Code
推荐安装以下扩展：
- Python
- Flask Snippets
- SQLite Viewer
- GitLens

### PyCharm
- 配置Python解释器指向虚拟环境
- 启用Flask支持
- 配置代码格式化

---

**技术支持**: 如有问题请联系项目维护者或查看项目文档。
