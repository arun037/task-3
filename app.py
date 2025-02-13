from flask import Flask
from prometheus_client import generate_latest, REGISTRY, Counter

app = Flask(__name__)

# Define a Prometheus Counter to track requests
request_count = Counter('python_app_requests', 'Total number of requests')

@app.route('/')
def home():
    request_count.inc()
    return "Hello, Kubernetes! This is a Flask app."

@app.route('/metrics')
def metrics():
    return generate_latest(REGISTRY)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
