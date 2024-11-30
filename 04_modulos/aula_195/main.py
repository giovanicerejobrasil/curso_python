"""
Chrome Options
https://peter.sh/experiments/chromium-command-line-switches/

Selenium Docs
https://selenium-python.readthedocs.io/
"""

from time import sleep
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Caminho da pasta raíz
ROOT_FOLDER = Path(__file__).parent
# Caminho para o chromedriver
CHROME_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'chromedriver'


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(
        executable_path=CHROME_DRIVER_PATH
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options,
    )

    return browser


if __name__ == '__main__':
    TIME_TO_WAIT = 10

    # Examples
    options = ('--disable-gpu', '--no-sandbox')
    browser = make_chrome_browser(*options)

    # Abrir o site
    browser.get('https://www.google.com')

    # Esperar pelo campo desejado ser carregado
    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.NAME, 'q')
        )
    )

    try:
        # Digita no campo desejado e "aperta" a tecla enter
        search_input.send_keys('Hello World!')
        search_input.send_keys(Keys.ENTER)
    except Exception as error:
        print(error)

    results = browser.find_element(By.ID, 'search')
    links = results.find_elements(By.TAG_NAME, 'a')
    links[0].click()

    sleep(TIME_TO_WAIT)
