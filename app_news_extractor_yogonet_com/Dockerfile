FROM python:3.9-slim

WORKDIR /app_news_extractor_yogonet_com
COPY . .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

ENV GOOGLE_APPLICATION_CREDENTIALS="credentials/BigQuery_credentials.json"

CMD ["python", "main.py"]
