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
no_username_email = os.getenv('NO_USERNAME_EMAIL')
no_dot_email = os.getenv('NO_DOT_EMAIL')
short_domain_email = os.getenv('SHORT_DOMAIN')
short_tdl_email = os.getenv('SHORT_TLD')


valid_password = os.getenv('VALID_PASSWORD')
browser_choice = os.getenv('BROWSER')
invalid_password = os.getenv('SHORT_PASSWORD')  # Make sure this is set in your .env

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

    def test_no_username_email_login(self):
        # Enter username and email then click on start
        self.driver.find_element(By.ID, 'candidateName').send_keys(full_name)
        self.driver.find_element(By.ID, 'candidateMail').send_keys(valid_email)
        self.driver.find_element(By.ID, 'startButton').click()

        # Wait a few seconds for navigation and User Story title to appear
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h3')))

        # Insert the no_username_email and invalid password
        self.driver.find_element(By.ID, 'email').send_keys(no_username_email)
        self.driver.find_element(By.ID, 'password').send_keys(invalid_password)

        # Click the login button
        self.driver.find_element(By.CSS_SELECTOR, 'input[type="button"][value="Login"]').click()

        # Check for the error message
        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'errorMsgMail'))
        ).text
        self.assertIn("Invalid email", error_message, "Error message for invalid email not found")

    def test_no_dot_email_login(self):
        # Enter username and email then click on start
        self.driver.find_element(By.ID, 'candidateName').send_keys(full_name)
        self.driver.find_element(By.ID, 'candidateMail').send_keys(valid_email)
        self.driver.find_element(By.ID, 'startButton').click()

        # Wait a few seconds for navigation and User Story title to appear
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h3')))

        # Insert the no_username_email and invalid password
        self.driver.find_element(By.ID, 'email').send_keys(no_dot_email)
        self.driver.find_element(By.ID, 'password').send_keys(invalid_password)

        # Click the login button
        self.driver.find_element(By.CSS_SELECTOR, 'input[type="button"][value="Login"]').click()

        # Check for the error message
        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'errorMsgMail'))
        ).text
        self.assertIn("Invalid email", error_message, "Error message for invalid email not found")

    def test_short_domain_email_login(self):
        # Enter username and email then click on start
        self.driver.find_element(By.ID, 'candidateName').send_keys(full_name)
        self.driver.find_element(By.ID, 'candidateMail').send_keys(valid_email)
        self.driver.find_element(By.ID, 'startButton').click()

        # Wait a few seconds for navigation and User Story title to appear
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h3')))

        # Insert the no_username_email and invalid password
        self.driver.find_element(By.ID, 'email').send_keys(short_domain_email)
        self.driver.find_element(By.ID, 'password').send_keys(invalid_password)

        # Click the login button
        self.driver.find_element(By.CSS_SELECTOR, 'input[type="button"][value="Login"]').click()

        # Check for the error message
        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'errorMsgMail'))
        ).text
        self.assertIn("Invalid email", error_message, "Error message for invalid email not found")

    def test_short_tdl_email_login(self):
        # Enter username and email then click on start
        self.driver.find_element(By.ID, 'candidateName').send_keys(full_name)
        self.driver.find_element(By.ID, 'candidateMail').send_keys(valid_email)
        self.driver.find_element(By.ID, 'startButton').click()

        # Wait a few seconds for navigation and User Story title to appear
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h3')))

        # Insert the no_username_email and invalid password
        self.driver.find_element(By.ID, 'email').send_keys(short_tdl_email)
        self.driver.find_element(By.ID, 'password').send_keys(invalid_password)

        # Click the login button
        self.driver.find_element(By.CSS_SELECTOR, 'input[type="button"][value="Login"]').click()

        # Check for the error message
        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'errorMsgMail'))
        ).text
        self.assertIn("Invalid email", error_message, "Error message for invalid email not found")

    

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
