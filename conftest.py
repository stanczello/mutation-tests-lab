from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import json

@pytest.fixture
def config():
    config_file = open('config.json')
    return json.load(config_file)

@pytest.fixture()
def driver(config):
    if config['browser']['browser'] == "Chrome":
        opts = Options()
        opts.add_argument("start-maximized")
        if config['browser']['headless']:
            opts.add_argument('headless')
        b =  webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]["browser"]}" is not supported')

    b.implicitly_wait(config['browser']['implicit_wait'])
    yield b
    b.quit()
