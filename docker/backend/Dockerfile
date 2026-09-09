FROM python:3.11-alpine

WORKDIR /app

RUN pip install --no-cache-dir flask

RUN cat <<'EOF' > app.py
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "application": "DEVOPS FA1 Backend",
        "environment": os.getenv("ENVIRONMENT", "unknown"),
        "status": "running"
    }

@app.route("/health")
def health():
    return {
        "status": "healthy"
    }

app.run(host="0.0.0.0", port=5000)
EOF

EXPOSE 5000

CMD ["python", "app.py"]