
# News Extractor Service

This job is part of a challenge for the position of Data Engineer. This project provides a Python-based web scraping application that uses Selenium with Firefox to extract news. It supports running both locally and on Google Cloud Run.

## Prerequisites

Before using this project, ensure the following tools are installed on your system:

- **Docker**: To containerize and run the application and its dependencies.
- **Docker Compose**: To orchestrate multiple services, such as Selenium and the Python app.
- **gcloud CLI**: To deploy and manage the application on Google Cloud Run.

## Running Locally

To run the application locally, execute the `start.sh` script included in the repository. This script will:
1. Start the Selenium service using Docker Compose.
2. Run the Python application.
3. Stop the Selenium service after the application completes.

### Notes for Local Execution
- The Selenium service runs as a standalone container with Firefox.
- The script ensures proper cleanup of resources after execution.

## Running on Google Cloud Run

You can deploy the application to Google Cloud Run for serverless execution. Follow the steps below to prepare and deploy:

### Prerequisites
1. **BigQuery Service Account**: 
   - Ensure you have a service account with BigQuery table edit permissions.
   - Download the service account credentials as a `.json` file and include it in the deployment process. Include the file in the 'app_news_extractor_yogonet_com/credentials' folder.

2. **VPC Setup**:
   Before deploying, create a Virtual Private Cloud (VPC) with the following parameters:
   - **Network Name**: `vpc-net`
   - **Region**: `us-central1`
   - **IP Range**: `10.8.0.0/28`

   This VPC is required to isolate the application securely in the cloud environment.

### Deployment
Use the `deploy.sh` script to deploy the application to Google Cloud Run. This script:
1. Logs you into your Google Cloud account.
2. Configures the application with the necessary environment variables and dependencies.
3. Deploys the application to Cloud Run.

### Troubleshooting Cloud Run Deployment
- If the **`app-news-extractor-service`** process encounters issues, check the `SELENIUM_URL` in the `deploy.sh` script (line 41 by default). Ensure it matches the correct service endpoint.
- Confirm that the VPC is properly configured and attached to the Cloud Run instance.

## Notes

- The application uses Selenium to handle browser-based web scraping tasks. Selenium is packaged into a Docker container running Firefox for consistent behavior.
- Environment-specific configurations, such as the Selenium URL and BigQuery credentials, are managed via environment variables passed during deployment.

For further details or issues, consult the relevant scripts (`start.sh` or `deploy.sh`) or open an issue in the project repository.


Challenge: https://mia-platform.notion.site/Python-Code-Challenge-Scraping-and-Ingest-c5ea18abca8c4bb59eb1265b7f46a83c
ChatGPT Link: https://chatgpt.com/share/67598c29-8438-8001-95e4-34d86192bc8a