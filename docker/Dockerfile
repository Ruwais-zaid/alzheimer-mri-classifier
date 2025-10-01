# Base image
FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl wget git && rm -rf /var/lib/apt/lists/*


COPY alzheimer-mri-classifier/app/requriments.txt .
RUN pip install --no-cache-dir  --default-timeout=1000 -r requriments.txt

COPY alzheimer-mri-classifier/app/ .

COPY alzheimer-mri-classifier/app/models/ ./models/

EXPOSE 8501


CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
