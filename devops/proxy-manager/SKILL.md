---
name: proxy-manager
description: 智能网络代理管理器，支持自动路由、GFWList 分流与自动学习。
version: 1.1.0
author: huangwc21
license: MIT
platforms: [linux, wsl]
metadata:
  hermes:
    tags: [devops, proxy, network, automation, wsl]
    related_skills: []
---

# Proxy Manager (增强版)

该技能提供了一套智能化的网络代理管理方案，专门针对 WSL 和开发者环境优化。通过区分手动规则与自动学习规则，确保网络访问既高效又稳定。

## 主要特性

- **智能分流**：内置 gfwlist 路由机制，自动判断是否通过代理访问。
- **动态学习**：系统直连访问失败且通过代理成功时，自动将该目标域名记录到 `auto_rules.txt`，实现“越用越好用”。
- **规则隔离**：
    - `user_rules.txt`：存放你固定的私有域名规则（高优先级）。
    - `auto_rules.txt`：存放系统自动学习的动态规则。
- **无缝集成**：封装了请求包装器，无需每次手动 `export https_proxy`。

## 快速开始

### 1. 初始化数据
首次使用前，确保数据目录存在并初始化规则：
```bash
# 确保数据目录已创建
mkdir -p ~/.hermes/skills/devops/proxy-manager/data
# 运行初始化脚本
python3 ~/.hermes/skills/devops/proxy-manager/scripts/init_proxy.py
```

### 2. 使用方式
在 Hermes 的终端环境或任务中，调用代理引擎：
```bash
# 自动检测并获取当前请求的代理设置
source ~/.hermes/skills/devops/proxy-manager/scripts/proxy_env.sh
```

## 规则维护

- **添加私有规则**：
  直接编辑 `~/.hermes/skills/devops/proxy-manager/data/user_rules.txt`，每行一个域名。
  
- **查看自动学习记录**：
  查看 `~/.hermes/skills/devops/proxy-manager/data/auto_rules.txt`。

## 故障排除 (Pitfalls)

- **代理地址失效**：若代理服务器地址变更，请通过 `hermes config set devops.proxy_url http://172.x.x.x:port` 更新全局配置。
- **自动学习冲突**：若发现某个域名被错误记录为代理，请在 `user_rules.txt` 中添加 `!` 前缀（如 `!github.com`）以强制直连。
- **权限问题**：如果脚本无法写入 `data/` 目录，请检查文件系统权限 `chmod -R 755 ~/.hermes/skills/devops/proxy-manager/data`。

## 验证
运行以下命令检查当前代理状态：
```bash
python3 ~/.hermes/skills/devops/proxy-manager/scripts/check_proxy.py
```
