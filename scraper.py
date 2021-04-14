import os
import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

if not os.path.isdir('actas_json/'): os.mkdir('actas_json/')


DEBUG=0 # 0 to dont render image


def scraper(numero_acta):
    # Main code taken from https://thinkdiff.net/how-to-run-javascript-in-python-web-scraping-web-testing-16bd04894360
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1024x1400")

    # download Chrome Webdriver  
    # https://sites.google.com/a/chromium.org/chromedriver/download
    # put driver executable file in the script directory
    chrome_driver = os.path.join(os.getcwd(),  "headers/chromedriver")

    driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)

    driver.get(f"https://www.resultados.eleccionesgenerales2021.pe/EG2021/Actas/Numero/{numero_acta}")

    time.sleep(2+random.uniform(0, 1))

    driver.find_element_by_xpath('//*[@id="pdf"]/div[3]/div[1]/ul/li[2]/a').click() # Botón congresales

    time.sleep(2+random.uniform(0, 1))

    html=driver.page_source

    # screenshot capture
    if DEBUG==1: driver.get_screenshot_as_file("python-scrap.png")
    driver.close()

