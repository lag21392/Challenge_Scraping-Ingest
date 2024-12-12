
from untils.Logger import Logger
from untils.WebDriverManager import WebDriverManager
from NewsScraper import NewsScraper
from NewsPostProcessing import NewsPostProcessing
from untils.BigQueryConector import BigQueryConector
import json

def main():

    # Create Logger
    logger = Logger.create_logger("app_new_extractor")
    logger.info('--------------------- INIT ---------------------')
    # Configuration is loaded from a JSON file
    logger.info('Configuration is loaded from a JSON file')
    json_file_path = "config.json"
    with open(json_file_path, 'r') as file:
        config = json.load(file)

    url_to_scraping = config.get("URL_to_scraping")
    project_id = config.get("project_id")
    dataset_id = config.get("dataset_id")
    table = config.get("table")


    # Create the WebDriver
    logger.info('Connecting to the WebDriver')
    web_driver_manager = WebDriverManager(logger)
    web_driver_manager.create_driver()
    
    # Extract News
    logger.info('Extract News')
    scraper = NewsScraper(logger, web_driver_manager.driver)    
    df_news = scraper.extract_news_to_pandas(url_to_scraping)

    # Post-processing news
    logger.info('Post-processing news')
    df_news = NewsPostProcessing.add_metrics(df_news)
    

    # Save data to bigquery
    logger.info('Save data to bigquery')
    db_conector = BigQueryConector(logger)    
    db_conector.df_to_sql(project_id, dataset_id, table, df_news)      

    # Close driver
    logger.info('Close driver')
    logger.info('--------------------- FINISH ---------------------')
    web_driver_manager.close_driver()
    

if __name__ == "__main__":
    main()
