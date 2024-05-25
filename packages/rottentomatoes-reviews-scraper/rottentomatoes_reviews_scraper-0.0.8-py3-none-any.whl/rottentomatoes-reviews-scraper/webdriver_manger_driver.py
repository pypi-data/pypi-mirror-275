# webdriver_manager.py

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def webdriver_manager():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    return driver
