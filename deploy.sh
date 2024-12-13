#!/bin/bash

PROJECT_ID="brave-embassy-444520-s7"         

# Authenticate with Google Cloud
#gcloud auth login
gcloud config set project $PROJECT_ID

# Build the Docker image
docker-compose build --no-cache

# Upload the image to Google Container Registry
docker tag challenge_scraping-ingest-app_news_extractor_yogonet_com \
  us-central1-docker.pkg.dev/$PROJECT_ID/challenge-scraping-ingest/app_news_extractor_yogonet_com:latest
docker tag selenium/standalone-firefox \
  us-central1-docker.pkg.dev/$PROJECT_ID/challenge-scraping-ingest/selenium:latest
docker push us-central1-docker.pkg.dev/$PROJECT_ID/challenge-scraping-ingest/app_news_extractor_yogonet_com:latest
docker push us-central1-docker.pkg.dev/$PROJECT_ID/challenge-scraping-ingest/selenium:latest

# VPC is created
gcloud services enable vpcaccess.googleapis.com --project=$PROJECT_ID
#gcloud compute networks vpc-access connectors create vpc-net \
#  --network=vpc-net \
#  --region=us-central1 \
#  --range=10.8.0.0/28

# Deploy the application in Cloud Run
gcloud run deploy selenium-service \
  --image=us-central1-docker.pkg.dev/$PROJECT_ID/challenge-scraping-ingest/selenium:latest \
  --region=us-central1 \
  --platform=managed \
  --allow-unauthenticated \
  --port=4444 \
  --vpc-connector=my-vpc-connector
gcloud run deploy app-news-extractor-service \
  --image=us-central1-docker.pkg.dev/$PROJECT_ID/challenge-scraping-ingest/app_news_extractor_yogonet_com:latest \
  --region=us-central1 \
  --platform=managed \
  --allow-unauthenticated \
  --vpc-connector=my-vpc-connector \
  --set-env-vars="SELENIUM_URL=https://selenium-service-1042102319427.us-central1.run.app:4444/wd/hub"
