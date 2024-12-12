
from Logger import Logger
from WebDriverManager import WebDriverManager
from NewsScraper import NewsScraper
from NewsPostProcessing import NewsPostProcessing
from BigQueryConector import BigQueryConector
import pandas as pd
def main():

    # Crear el Logger
    logger = Logger.create_logger("app_new_extractor")
    
    # Crear el WebDriver
    web_driver_manager = WebDriverManager(logger)
    web_driver_manager.create_driver()
    
    # Crear el scraper
    scraper = NewsScraper(logger, web_driver_manager.driver)
    
    # URL de noticias
    url = "https://www.yogonet.com/international/"
    
    # Extraer Noticias
    df_news = scraper.extract_news_to_pandas(url)

    # Cerrar driver
    web_driver_manager.close_driver()

    
    # Post-Processing
    df_news = NewsPostProcessing.add_metrics(df_news)

    # Save data in csv for control
    df_news.to_csv('data.csv')
    
    # Load data to bigquery
    db_conector = BigQueryConector(logger)
    db_conector.df_to_sql(df_news)    
    



if __name__ == "__main__":
    main()
