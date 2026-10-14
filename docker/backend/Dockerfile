
FROM python:3.11-alpine
WORKDIR /app
RUN pip install --no-cache-dir flask prometheus-client
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]
