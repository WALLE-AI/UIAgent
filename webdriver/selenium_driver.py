import time

import selenium
from selenium import webdriver


class SeleniumDrvier():
    def __init__(self):
        self.decs = "selenium drvier "
        self.driver = webdriver.Chrome()

    @classmethod
    def get_driver(cls):
        return cls().driver



