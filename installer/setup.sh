#!/bin/bash
   # Termux AI Setup Script
   echo "[+] Installing dependencies..."
   pkg update -y && pkg upgrade -y
   pkg install python clang git cmake libandroid-spawn -y
   pip install flask llama-cpp-python pywebview --no-cache-dir

   echo "[+] Cloning repository..."
   git clone https://github.com/YOUR_USERNAME/REPO_NAME ~/MyAI

   echo "[+] Downloading model..."
   mkdir -p ~/MyAI/models
   cd ~/MyAI/models
   wget https://huggingface.co/TheBloke/deepseek-coder-1.3b-instruct-GGUF/resolve/main/deepseek-coder-1.3b-instruct.Q4_K_M.gguf

   echo "[+] Setting permissions..."
   chmod +x ~/MyAI/web/start.sh

   echo "[+] Installation complete!"
   echo "Run: bash ~/MyAI/web/start.sh"
