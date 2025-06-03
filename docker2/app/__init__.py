from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello():
    env = os.getenv('APP_ENV', 'development')
    return jsonify({
        'message': f'Hello from {env} environment!',
        'status': 'success'
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})
