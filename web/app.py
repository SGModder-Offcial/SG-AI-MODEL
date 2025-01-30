from flask import Flask, render_template, request, jsonify, send_file
from llama_cpp import Llama
import os
import time

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.expanduser('~/Termux-AI-Coder/code')

# Initialize model
model_path = os.path.expanduser('~/Termux-AI-Coder/models/deepseek-coder-1.3b-instruct.Q4_K_M.gguf')

llm = Llama(
    model_path=model_path,
    n_ctx=2048,
    n_threads=4,
    n_gpu_layers=0,
    verbose=False
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        prompt = f"System: You are an expert coding assistant. Respond only with code.\nUser: {request.json['prompt']}\nAssistant:"
        response = llm(
            prompt,
            max_tokens=512,
            temperature=0.7,
            top_p=0.95,
            stop=["</s>", "System:"]
        )["choices"][0]["text"]
        return jsonify({'response': response.strip()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download', methods=['POST'])
def download():
    try:
        filename = f"code_{int(time.time())}.py"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        with open(filepath, 'w') as f:
            f.write(request.json['content'])
        return send_file(filepath, as_attachment=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(host='127.0.0.1', port=5000, debug=False)
