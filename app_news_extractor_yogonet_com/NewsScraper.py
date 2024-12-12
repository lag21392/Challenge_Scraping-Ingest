from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from concurrent.futures import ThreadPoolExecutor

import pandas as pd
class NewsScraper:
    def __init__(self, logger, driver):
        self.logger = logger
        self.driver = driver

    def extract_news_to_pandas(self, url):
        def extract_news(news):
                try:                    
                    xpath_title = ".//div[@class='volanta_titulo']/div[@class='volanta fuente_roboto_slab']"
                    title = news.find_element(By.XPATH, xpath_title).text

                    xpath_kicker  = ".//div[@class='volanta_titulo']/h2[@class='titulo fuente_roboto_slab']/a"
                    kicker = news.find_element(By.XPATH, xpath_kicker).text

                    xpath_url = ".//div[contains(@class, 'imagen')]/a"
                    href = news.find_element(By.XPATH, xpath_url)
                    url = href.get_attribute('href')

                    xpath_url = ".//div[contains(@class, 'imagen')]/a/img"
                    imagen = news.find_element(By.XPATH, xpath_url)
                    img_url = imagen.get_attribute('src')

                    #self.logger.info(f"Title: {title} - Kicker: {kicker} - URL: {url} - Image_URL: {img_url}")
                    return (title, kicker, url, img_url)

                except Exception as e:
                    self.logger.info(f"Error: {str(e)}")
                    return ("", "", "", "")
                
        def list_of_news_to_pandas(news_data):
            columns = ['Title', 'Kicker', 'URL', 'Image_URL']
            df = pd.DataFrame(news_data, columns=columns)
            return df

        try:
            self.logger.info(f"Abriendo la página: {url}")
            self.driver.get(url)
            
            # Wait for news to appear
            xpath_news = "//div/div/div/div[contains(@class, 'contenedor_dato_modulo') and .//div[@class='volanta_titulo']]"
            WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, xpath_news)))

            # Parallel news extract 
            news = self.driver.find_elements(By.XPATH, xpath_news)
            self.logger.info(f"{len(news)} news were found:")         
            
            with ThreadPoolExecutor() as executor:
                news_data = list(executor.map(extract_news, news))

            # Convert news list to pandas 
            news_data_df = list_of_news_to_pandas(news_data)
            return news_data_df
        
        except Exception as e:
            self.logger.error(f"Error: {str(e)}")
            raise Exception(f'Failure in extract_news_to_pandas: {str(e)}')

