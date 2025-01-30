#!/bin/bash
cd ~/Termux-AI-Coder/web
python app.py &> ../code/runtime.log &
echo -e "\033[1;32mServer started!\033[0m"
echo -e "Access at: \033[1;36mhttp://127.0.0.1:5000\033[0m"
echo -e "Stop with: \033[1;33mkillall python\033[0m"
