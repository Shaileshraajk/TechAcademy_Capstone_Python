import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def driver_init(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    driver.quit()