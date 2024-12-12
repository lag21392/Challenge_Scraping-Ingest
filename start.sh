#!/bin/bash

# Starts services
docker-compose up -d

# Run the extraction process and wait for it to finish
docker-compose exec app_news_extractor_yogonet_com python main.py

# Stops containers
docker-compose down
