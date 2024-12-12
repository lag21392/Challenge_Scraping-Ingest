from selenium import webdriver
import os


class WebDriverManager:

    def __init__(self, logger):
        self.logger = logger

    def create_driver(self):
        try:
            selenium_url = os.getenv("SELENIUM_URL", "http://localhost:4444/wd/hub")
            options = webdriver.FirefoxOptions()
            self.driver = webdriver.Remote(command_executor=selenium_url, options=options)
            self.logger.info('Driver is started')
            return self.driver
        except:
            self.logger.info('Driver startup failure')

    def close_driver(self):
        self.driver.quit()
        self.logger.info('Driver is close')