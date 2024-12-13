#!/bin/bash

# Build services
docker-compose build 

# Starts services
docker-compose up selenium -d

# Run the extraction process and wait for it to finish
docker-compose up app_news_extractor_yogonet_com 

# Stops containers
docker-compose down
