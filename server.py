from flask import Flask, send_from_directory, request, jsonify
import os
import tiktoken

app = Flask(__name__, static_folder='public')

@app.route('/')
def home():
    with open('public/index.html', 'r') as f:
        content = f.read()
    
    # Count tokens
    encoding = tiktoken.get_encoding("cl100k_base")
    token_count = len(encoding.encode(content))
    token_display = f'<p id="token-count" style="color: #666; font-size: 0.9em;">{token_count} tokens</p>'
    content = content.replace('<p id="token-count" style="color: #666; font-size: 0.9em;">Calculating tokens...</p>', token_display)
    
    return content

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('public', path)

@app.route('/save', methods=['POST'])
def save():
    content = request.get_data(as_text=True)
    with open('public/index.html', 'w') as f:
        f.write(content)
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True, port=8000)
