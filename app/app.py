from flask import Flask, jsonify, request
from prometheus_client import Counter, Summary, generate_latest
import random
import time

app = Flask(__name__)

# Métricas
REQUEST_COUNT = Counter('request_count', 'Total de requisições', ['method', 'endpoint'])
REQUEST_LATENCY = Summary('request_latency_seconds', 'Tempo de resposta das requisições', ['endpoint'])
RESPONSE_STATUS = Counter('response_status', 'Contagem de códigos de resposta HTTP', ['method', 'endpoint', 'status_code'])


@app.route('/')
@REQUEST_LATENCY.labels('/').time()
def home():
    REQUEST_COUNT.labels('GET', '/').inc()
    return "API Online!"

@app.route('/login')
@REQUEST_LATENCY.labels('/login').time()
def login():
    REQUEST_COUNT.labels('GET', '/login').inc()
    return "Tela de Login"

@app.route('/status')
@REQUEST_LATENCY.labels('/status').time()
def status():
    REQUEST_COUNT.labels('GET', '/status').inc()
    return jsonify({"status": "ok", "uptime": "100%"})

@app.route('/users')
@REQUEST_LATENCY.labels('/users').time()
def users():
    REQUEST_COUNT.labels('GET', '/users').inc()
    time.sleep(random.uniform(0.2, 0.7))  # simula latência
    return jsonify(["Ana", "Bruno", "Carlos"])

@app.route('/crash')
@REQUEST_LATENCY.labels('/crash').time()
def crash():
    REQUEST_COUNT.labels('GET', '/crash').inc()
    raise Exception("Erro forçado para testes")

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain; charset=utf-8'}

@app.after_request
def after_request(response):
    method = request.method
    endpoint = request.path
    status = response.status_code
    RESPONSE_STATUS.labels(method, endpoint, status).inc()
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
