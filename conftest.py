from selenium import webdriver
import pytest
import json

@pytest.fixture
def config():
    config_file = open('config.json')
    return json.load(config_file)

@pytest.fixture()
def driver(config):
    return webdriver.Chrome(config['chromedriverPath'])
