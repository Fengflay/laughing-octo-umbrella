#!/bin/bash
# ecom-image-gen 一鍵部署腳本
# 用法: ./deploy.sh [setup|start|stop|restart|logs|status]

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

print_status() { echo -e "${GREEN}[✓]${NC} $1"; }
print_warning() { echo -e "${YELLOW}[!]${NC} $1"; }
print_error() { echo -e "${RED}[✗]${NC} $1"; }

case "${1:-start}" in
  setup)
    echo "══════════════════════════════════════"
    echo "  ecom-image-gen 初始設定"
    echo "══════════════════════════════════════"
    echo ""

    # Check Docker
    if ! command -v docker &> /dev/null; then
      print_warning "正在安裝 Docker..."
      curl -fsSL https://get.docker.com | sh
      print_status "Docker 安裝完成"
    else
      print_status "Docker 已安裝: $(docker --version)"
    fi

    # Create .env if not exists
    if [ ! -f .env ]; then
      cp .env.example .env
      # Generate JWT_SECRET
      JWT=$(python3 -c "import secrets; print(secrets.token_urlsafe(32))" 2>/dev/null || openssl rand -base64 32)
      sed -i "s/your_strong_random_secret_here/$JWT/" .env
      print_warning "已建立 .env 檔案，請編輯填入你的 API Key："
      echo "    nano .env"
    else
      print_status ".env 已存在"
    fi

    echo ""
    print_status "設定完成！填好 .env 後執行: ./deploy.sh start"
    ;;

  start)
    echo "正在啟動服務..."
    docker compose up -d --build
    echo ""
    print_status "服務已啟動！"
    echo ""
    echo "  前端: http://localhost"
    echo "  API:  http://localhost/api/health"
    echo ""
    echo "查看日誌: ./deploy.sh logs"
    ;;

  stop)
    echo "正在停止服務..."
    docker compose down
    print_status "服務已停止"
    ;;

  restart)
    echo "正在重啟服務..."
    docker compose down
    docker compose up -d --build
    print_status "服務已重啟"
    ;;

  logs)
    docker compose logs -f --tail=100 ${2:-}
    ;;

  status)
    docker compose ps
    echo ""
    echo "健康檢查:"
    curl -s http://localhost/api/health 2>/dev/null && echo "" || print_error "API 無回應"
    ;;

  *)
    echo "用法: ./deploy.sh [setup|start|stop|restart|logs|status]"
    echo ""
    echo "  setup    - 初始設定（安裝 Docker、建立 .env）"
    echo "  start    - 啟動所有服務"
    echo "  stop     - 停止所有服務"
    echo "  restart  - 重啟所有服務"
    echo "  logs     - 查看日誌（可選: logs backend/frontend/nginx）"
    echo "  status   - 查看服務狀態"
    ;;
esac
