# coding:utf-8

import pytest
from selenium import webdriver


@pytest.fixture
def init_driver():

    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
    # init_driver 接收 driver

def login():
    pass

