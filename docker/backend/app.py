
from flask import Flask, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import os
import time

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "backend_http_requests_total",
    "Total HTTP requests received by the backend",
    ["method", "endpoint", "status"]
)

REQUEST_DURATION = Histogram(
    "backend_http_request_duration_seconds",
    "Time taken to process backend requests",
    ["endpoint"]
)

@app.before_request
def start_timer():
    from flask import request, g
    g.start_time = time.time()

@app.after_request
def record_metrics(response):
    from flask import request, g

    endpoint = request.endpoint or "unknown"
    REQUEST_COUNT.labels(
        request.method, endpoint, response.status_code
    ).inc()

    if hasattr(g, "start_time"):
        REQUEST_DURATION.labels(endpoint).observe(
            time.time() - g.start_time
        )

    return response

@app.route("/")
def home():
    return {
        "application": "DEVOPS FA1 Backend",
        "environment": os.getenv("ENVIRONMENT", "unknown"),
        "status": "running"
    }

@app.route("/health")
def health():
    return {"status": "healthy"}

@app.route("/metrics")
def metrics():
    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
