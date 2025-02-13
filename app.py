from flask import Flask, Response
from prometheus_client import generate_latest, Counter

app = Flask(__name__)

# Define a Prometheus Counter
REQUEST_COUNT = Counter("request_count", "Total number of requests")

@app.route("/")
def hello():
    REQUEST_COUNT.inc()  # Increment the counter
    return "Hello, World!"

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype="text/plain")  # Ensure metrics are generated

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
