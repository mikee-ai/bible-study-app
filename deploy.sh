#!/bin/bash

# AI-Powered Bible Study App - Quick Deployment Script
# For Hostinger VPS at sonship.ai/study

set -e

echo "=========================================="
echo "Bible Study App - Deployment Script"
echo "=========================================="
echo ""

# Check if running as root
if [ "$EUID" -ne 0 ]; then 
    echo "Please run as root (use sudo)"
    exit 1
fi

# Update system
echo "Step 1: Updating system packages..."
apt update && apt upgrade -y

# Install dependencies
echo "Step 2: Installing dependencies..."
apt install -y python3 python3-venv python3-pip nginx git curl

# Clone repository
echo "Step 3: Cloning application repository..."
cd /var/www
if [ -d "bible-study-app" ]; then
    echo "Directory already exists. Pulling latest changes..."
    cd bible-study-app
    git pull origin master
else
    git clone https://github.com/mikee-ai/bible-study-app.git
    cd bible-study-app
fi

# Set up virtual environment
echo "Step 4: Setting up Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install Python packages
echo "Step 5: Installing Python dependencies..."
pip install -r requirements.txt
pip install gunicorn python-dotenv

# Create .env file
echo "Step 6: Configuring environment variables..."
if [ ! -f ".env" ]; then
    read -p "Enter your OpenAI API key: " api_key
    echo "OPENAI_API_KEY=$api_key" > .env
    echo ".env file created"
else
    echo ".env file already exists"
fi

# Create wsgi.py
echo "Step 7: Creating WSGI entry point..."
cat > wsgi.py << 'EOF'
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from src.main import app

if __name__ == "__main__":
    app.run()
EOF

# Create systemd service
echo "Step 8: Creating systemd service..."
cat > /etc/systemd/system/bible-study.service << 'EOF'
[Unit]
Description=Gunicorn instance for AI Bible Study App
After=network.target

[Service]
User=root
Group=www-data
WorkingDirectory=/var/www/bible-study-app
Environment="PATH=/var/www/bible-study-app/venv/bin"
EnvironmentFile=/var/www/bible-study-app/.env
ExecStart=/var/www/bible-study-app/venv/bin/gunicorn --workers 3 --bind unix:bible-study.sock -m 007 wsgi:app

[Install]
WantedBy=multi-user.target
EOF

# Start and enable service
echo "Step 9: Starting application service..."
systemctl daemon-reload
systemctl start bible-study
systemctl enable bible-study

# Configure Nginx
echo "Step 10: Configuring Nginx..."
cat > /etc/nginx/sites-available/bible-study << 'EOF'
server {
    listen 80;
    server_name sonship.ai www.sonship.ai;

    location /study {
        rewrite ^/study(/.*)$ $1 break;
        rewrite ^/study$ / break;
        
        include proxy_params;
        proxy_pass http://unix:/var/www/bible-study-app/bible-study.sock;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /study/static {
        alias /var/www/bible-study-app/src/static;
    }
}
EOF

# Enable site
ln -sf /etc/nginx/sites-available/bible-study /etc/nginx/sites-enabled/
nginx -t
systemctl restart nginx

# Configure firewall
echo "Step 11: Configuring firewall..."
ufw allow 'Nginx Full'
ufw --force enable

echo ""
echo "=========================================="
echo "Deployment Complete!"
echo "=========================================="
echo ""
echo "Your Bible study app is now running at:"
echo "http://sonship.ai/study"
echo ""
echo "To check service status:"
echo "  systemctl status bible-study"
echo ""
echo "To view logs:"
echo "  journalctl -u bible-study -f"
echo ""
echo "To install SSL certificate (recommended):"
echo "  apt install -y certbot python3-certbot-nginx"
echo "  certbot --nginx -d sonship.ai -d www.sonship.ai"
echo ""
echo "=========================================="
