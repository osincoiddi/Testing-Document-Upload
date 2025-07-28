import os.path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from datetime import datetime

@pytest.fixture
def setup(browser):
    if browser=="edge":
        driver=webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        print("Launching edge browser--")
        return driver
    elif browser=="firefox":
        driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        print("Launching firefox browser--")
        return driver
    else:
        driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print("Launching chrome browser--")
        return driver



def pytest_addoption(parser):
    parser.addoption("--browser") #This gets the value from hooks


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

def pytest_configure(config):
    config._metadata["Project Name"]="Upload"
    config._metadata["Module Name"]="Examples"

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA HOME",None)
    metadata.pop("Plugins",None)

@pytest.hookimpl(optionalhook=True)
def pytest_configure(config):
    config.option.htmlpath=os.path.abspath(os.curdir)+"\\report\\"+datetime.now().strftime("%Y%m%d-%H%M%S")+".html"
