import unittest
from password_test import PageLogin as PasswordLoginTest
from email_test import PageLogin as EmailLoginTest

if __name__ == '__main__':
    # Load test cases from each test class
    password_tests = unittest.TestLoader().loadTestsFromTestCase(PasswordLoginTest)
    email_tests = unittest.TestLoader().loadTestsFromTestCase(EmailLoginTest)

    # Create test suite
    suite = unittest.TestSuite([password_tests, email_tests])

    # Run the test suite
    unittest.TextTestRunner().run(suite)
