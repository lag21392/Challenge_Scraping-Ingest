from selenium import webdriver
import os
import time

class WebDriverManager:

    def __init__(self, logger):
        self.logger = logger
        self.driver = None
    def create_driver(self):
        time.sleep(5) 
        while not self.driver:            
            try:
                selenium_url = os.getenv("SELENIUM_URL", "http://localhost:4444/wd/hub")
                options = webdriver.FirefoxOptions()
                options.headless = True
                options.add_argument("--window-size=1920x1080")
                self.driver = webdriver.Remote(command_executor=selenium_url, options=options)
                self.logger.info('Driver is started')
                return self.driver
            except:
                time.sleep(3) 
                self.logger.info('Waiting for selenium to start')

    def close_driver(self):
        self.driver.close()
        self.driver.quit()
        self.logger.info('Driver is close')