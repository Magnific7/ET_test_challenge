import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from email_test import normalize_color
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

    def login_with_email_and_check_error(self, email, password, email_should_be_valid, password_should_be_valid,
                                         email_message_color_valid, password_message_color_valid):
        self.driver.find_element(By.ID, 'candidateName').send_keys(full_name)
        self.driver.find_element(By.ID, 'candidateMail').send_keys(valid_email)
        self.driver.find_element(By.ID, 'startButton').click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h3')))

        self.driver.find_element(By.ID, 'email').send_keys(email)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, 'input[type="button"][value="Login"]').click()

        try:
            email_msg_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, 'errorMsgMail'))
            )
            email_message_color = normalize_color(email_msg_element.value_of_css_property('color'))
        except TimeoutException:
            self.fail("Email error message did not appear as expected.")

        try:
            password_msg_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, 'errorMsgPwd'))
            )
            password_message_color = normalize_color(password_msg_element.value_of_css_property('color'))
        except TimeoutException:
            self.fail("Password error message did not appear as expected.")

        email_message = email_msg_element.text.strip()
        password_message = password_msg_element.text.strip()

        if email_should_be_valid:
            self.assertEqual(email_message, "Valid Email", "Expected valid email message not found.")
        if email_message_color_valid:
            self.assertEqual(email_message_color, "green", "Email message color does not indicate validity.")
        else:
            self.assertIn("Invalid", email_message, "Expected invalid email message not found.")
        if not email_message_color_valid:
            self.assertEqual(email_message_color, "rgba(255, 0, 0, 1)", "Email message color does not indicate invalidity.")

        if password_should_be_valid:
            self.assertIn("Valid", password_message, "Expected valid password message not found.")
        if password_message_color_valid:
            self.assertEqual(password_message_color, "green", "Password message color does not indicate validity.")
        else:
            self.assertIn("Invalid", password_message, "Expected invalid password message not found.")
        if not password_message_color_valid:
            self.assertEqual(password_message_color, "rgba(255, 0, 0, 1)", "Password message color does not indicate invalidity.")


    def test_short_password_valid_email_login(self):
        self.login_with_email_and_check_error(
        valid_email,
        short_password,
        email_should_be_valid=True,
        password_should_be_valid=False,
        email_message_color_valid=True,
        password_message_color_valid=False
    )
    def test_short_password_invalid_email_login(self):
        self.login_with_email_and_check_error(
        invalid_email,
        short_password,
        email_should_be_valid=False,
        password_should_be_valid=False,
        email_message_color_valid=False,
        password_message_color_valid=False
    )
    def test_no_upper_password_invalid_email_login(self):
        self.login_with_email_and_check_error(no_upper_password, invalid_email,
        email_should_be_valid=False,
        password_should_be_valid=False,
        email_message_color_valid=False,
        password_message_color_valid=False)

    def test_no_upper_password_valid_email_login(self):
        self.login_with_email_and_check_error(no_upper_password,valid_email,
        email_should_be_valid=True,
        password_should_be_valid=False,
        email_message_color_valid=True,
        password_message_color_valid=False)

    def test_no_lower_password_valid_email_login(self):
        self.login_with_email_and_check_error(no_lower_password, valid_email,
        email_should_be_valid=True,
        password_should_be_valid=False,
        email_message_color_valid=True,
        password_message_color_valid=False)

    def test_no_lower_password_invalid_email_login(self):
        self.login_with_email_and_check_error(no_lower_password, invalid_email,
        email_should_be_valid=False,
        password_should_be_valid=False,
        email_message_color_valid=False,
        password_message_color_valid=False)

    def test_no_digit_password_valid_email_login(self):
        self.login_with_email_and_check_error(no_digit_password, valid_email,
        email_should_be_valid=True,
        password_should_be_valid=False,
        email_message_color_valid=True,
        password_message_color_valid=False)
    
    def test_no_digit_password_invalid_email_login(self):
        self.login_with_email_and_check_error(no_digit_password, valid_email,
        email_should_be_valid=False,
        password_should_be_valid=False,
        email_message_color_valid=False,
        password_message_color_valid=False)

    def test_no_special_password_valid_email_login(self):
        self.login_with_email_and_check_error(no_special_password, valid_email,
        email_should_be_valid=True,
        password_should_be_valid=False,
        email_message_color_valid=True,
        password_message_color_valid=False)

    def test_no_special_password_invalid_email_login(self):
        self.login_with_email_and_check_error(no_special_password, invalid_email,
        email_should_be_valid=False,
        password_should_be_valid=False,
        email_message_color_valid=False,
        password_message_color_valid=False)

    def test_valid_email_and_password(self):
        self.login_with_email_and_check_error(valid_email, valid_password,
        email_should_be_valid=True,
        password_should_be_valid=True,
        email_message_color_valid=True,
        password_message_color_valid=True)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
