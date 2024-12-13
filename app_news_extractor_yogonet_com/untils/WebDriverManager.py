from selenium import webdriver
import os
import time

class WebDriverManager:

    def __init__(self, logger):
        self.logger = logger
        self.driver = None
    def create_driver(self):
        retries = 5
        while not self.driver and retries >0:            
            try:
                selenium_url = os.getenv("SELENIUM_URL", "http://0.0.0.0:4444/wd/hub")
                options = webdriver.FirefoxOptions()
                options.headless = True
                options.add_argument("--window-size=1920x1080")
                self.driver = webdriver.Remote(command_executor=selenium_url, options=options)
                self.logger.info('Driver is started')
                return self.driver
            except:
                retries = retries - 1
                if retries == 0:
                    self.logger.info('The number of retries to connect to the Web Drive has been exceeded.')
                    raise RuntimeError('The number of retries to connect to the Web Drive has been exceeded.')
                time.sleep(5) 
                self.logger.info(f'Waiting for selenium to start: {selenium_url}')
                

    def close_driver(self):
        self.driver.close()        
        self.logger.info('Driver is close')