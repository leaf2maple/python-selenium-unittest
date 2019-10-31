from selenium import webdriver
import os
import configparser
from framework.logger import Logger

logger = Logger('browserengine').get_log()


class BrowserEngine(object):

    def __init__(self, driver):
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + r'/config/config.ini'
        config.read(file_path)

        self.browser = config.get('browsertype', 'browsername')
        self.url = config.get('testserver', 'url')
        # print(browser, self.url)

        dir_path = os.path.dirname(os.path.abspath('.')) + r'/tools/'
        self.firefox_path = dir_path + 'geckodriver.exe'

        self.driver = driver

    def open_browser(self, driver):
        if self.browser == "Firefox":
            driver = webdriver.Firefox(executable_path=self.firefox_path)
        elif self.browser == "Chrome":
            driver = webdriver.Chrome()
        elif self.browser == "IE":
            driver = webdriver.Ie()

        driver.get(self.url)
        logger.info('打开浏览器')

        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver

    def quit_browser(self):
        logger.info('退出浏览器')
        self.driver.quit()

