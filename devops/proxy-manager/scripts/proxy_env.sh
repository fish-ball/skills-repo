#!/bin/bash
# 设置代理环境变量 (假设从 Hermes config 获取)
PROXY_URL=$(hermes config get devops.proxy_url 2>/dev/null || echo "http://172.28.80.1:1080")
export http_proxy=$PROXY_URL
export https_proxy=$PROXY_URL
echo "Proxy set to $PROXY_URL"
