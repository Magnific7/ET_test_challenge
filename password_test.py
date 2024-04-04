import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import time

# Load environment variables
load_dotenv()

valid_email = os.getenv('VALID_EMAIL')
full_name = os.getenv('FULL_NAMES')

short_password = os.getenv('SHORT_PASSWORD')
no_upper_password = os.getenv('NO_UPPER_PASSWORD')
no_lower_password = os.getenv('NO_LOWER_PASSWORD')
no_digit_password = os.getenv('NO_DIGIT_PASSWORD')
no_special_password = os.getenv('NO_SPECIAL_PASSWORD')


valid_password = os.getenv('VALID_PASSWORD')
browser_choice = os.getenv('BROWSER')
invalid_password = os.getenv('SHORT_PASSWORD')  

LOGIN_URL = 'https://magnific7.github.io/ET_test_challenge/'

class PageLogin(unittest.TestCase):
    def setUp(self):
        self.browser = browser_choice
        if self.browser.lower() == 'chrome':
            self.driver = webdriver.Chrome()
        elif self.browser.lower() == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            raise ValueError("Browser not supported.")
        self.driver.get(LOGIN_URL)

    def login_with_email_and_check_error(self, email, password, should_fail=True):

        self.driver.find_element(By.ID, 'candidateName').send_keys(full_name)
        self.driver.find_element(By.ID, 'candidateMail').send_keys(valid_email)
        self.driver.find_element(By.ID, 'startButton').click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h3')))
        self.driver.find_element(By.ID, 'email').send_keys(email)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, 'input[type="button"][value="Login"]').click()

        if should_fail:
            error_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, 'errorMsgPwd'))
            ).text
            self.assertIn("Invalid Password", error_message, "Error message for invalid password not found")
        else:
            try:
                WebDriverWait(self.driver, 10).until_not(
                    EC.text_to_be_present_in_element((By.ID, 'errorMsgPwd'), "Invalid Password")
                )
                login_success = True
            except TimeoutException:
                login_success = False

            self.assertTrue(login_success, "Expected absence of 'Invalid Password' error message, but it was found.")

    def test_short_password_login(self):
        self.login_with_email_and_check_error(short_password, valid_email)

    def test_no_upper_password_login(self):
        self.login_with_email_and_check_error(no_upper_password, valid_email)

    def test_no_lower_password_login(self):
        self.login_with_email_and_check_error(no_lower_password, valid_email)

    def test_no_digit_password_login(self):
        self.login_with_email_and_check_error(no_digit_password, valid_email)

    def test_no_special_password_login(self):
        self.login_with_email_and_check_error(no_special_password, valid_email)

    def test_valid_email_and_password(self):
        self.login_with_email_and_check_error(valid_email, valid_password, should_fail=False)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
