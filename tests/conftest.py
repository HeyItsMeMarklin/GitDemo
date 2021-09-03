import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="Chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "Chrome":
        driver = webdriver.Chrome(executable_path="c:\selenium browser drivers\chromedriver.exe")
    else:
        driver = webdriver.Edge(executable_path="c:\selenium browser drivers\msedgedriver.exe")
    url = driver.get('https://rahulshettyacademy.com/angularpractice/')
    driver.maximize_window()
    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield
    driver.close()

