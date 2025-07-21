# 项目说明

## 项目名称
webhostmost_auto_refresh

## 项目简介
webhostmost_auto_refresh 是一个用于自动刷新 Web 主机状态的 Python 项目，适合需要定时检测和刷新主机服务状态的场景。该项目通过脚本实现自动化操作，提升了运维效率，减少了人工干预。

## 功能特性
- 定时自动刷新主机状态
- 支持自定义刷新频率
- 支持 GitHub Actions 直接运行，支持通过 Secrets 设置用户名和密码
- 代码结构简单，易于扩展和维护

## 文件结构
```
.
├── .github/workflows/      # GitHub Actions 工作流配置
├── README.md               # 项目说明文档
├── live.py                 # 主程序脚本
├── requirements.txt        # 依赖库列表
```

## 安装与运行

### 1. 克隆项目
```bash
git clone https://github.com/wlzh/webhostmost_auto_refresh.git
cd webhostmost_auto_refresh
```

### 2. 安装依赖
请确保已安装 Python 3.7 及以上版本。
```bash
pip install -r requirements.txt
```

### 3. 运行脚本
```bash
python live.py
```

### 4. 使用 GitHub Actions 自动运行

本项目支持通过 GitHub Actions 自动运行。你可以在 `.github/workflows` 目录下找到相关工作流配置。  
请在你的仓库 Settings -> Secrets and variables -> Actions 下添加如下 Secrets：

- `MY_USERNAME_1`
- `MY_PASSWORD_1`
- `MY_USERNAME_2`
- `MY_PASSWORD_2`

在 workflow 文件中会自动读取这些变量，例如：

```yaml
env:
  MY_USERNAME_1: ${{ secrets.MY_USERNAME_1 }}
  MY_PASSWORD_1: ${{ secrets.MY_PASSWORD_1 }}
  MY_USERNAME_2: ${{ secrets.MY_USERNAME_2 }}
  MY_PASSWORD_2: ${{ secrets.MY_PASSWORD_2 }}
```

### 5. 配置自动化（本地/服务器）
如需在本地或服务器定时运行，可使用 crontab 或 Windows 任务计划程序设置定时任务。

## 致谢

本项目部分代码和思路参考自 [https://github.com/lukuichina/youtube/blob/main/2025/733/live.py](https://github.com/lukuichina/youtube/blob/main/2025/733/live.py)，感谢原作者的开源贡献！

## 贡献方式
欢迎提交 issue 和 pull request，完善项目功能。
