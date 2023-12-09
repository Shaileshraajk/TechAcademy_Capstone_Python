import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import openpyxl


def get_test_data():
    workbook = openpyxl.load_workbook("Capstone_TestData.xlsx")
    sheet = workbook["LoginData"]

    test_data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        test_data.append(row)

    workbook.close()
    return test_data

@pytest.mark.usefixtures("driver_init")
class TestScript:

    @pytest.mark.parametrize("username, password, success",get_test_data())
    def test_login(self, username, password, success):
        self.driver.get("https://www.saucedemo.com/")
        assert "Swag Labs" in self.driver.title

        username_field = self.driver.find_element(By.ID, "user-name")
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

        time.sleep(2)

        if success==True:
            assert "Swag Labs" in self.driver.title
        else:
            error_message = self.driver.find_element(By.XPATH,"//h3[@data-test='error']")
            assert error_message.is_displayed()


