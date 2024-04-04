
# ET Test Automation Challenge

Welcome to the ET Test Challenge Automation Suite. 
This project automates testing for a web application hosted at 
https://magnific7.github.io/ET_test_challenge/. 

The suite includes two main test scripts: 
- Validating email inputs (email_test.py)
- Password validation (password_test.py).

## Getting Started
### Prerequisites
Ensure you have Python 3.6+ installed on your machine. 
This project uses Selenium WebDriver for browser automation, 
so you will also need the appropriate WebDriver for your browser 
(ChromeDriver for Google Chrome, geckodriver for Firefox, etc.).

## Installation
#### Clone the Repository

`git clone https://github.com/Magnific7/ET_test_challenge.git`

#### Navigate the eteacher folder 
`cd eteacher`

#### Set Up a Virtual Environment

It's recommended to use a virtual environment for Python projects to manage dependencies efficiently.

Install virtualenv if you haven't already:

`pip install virtualenv`

Create a virtual envirronment for the project 
`virtualenv venv`

Activate the virtual environment:

- On Windows:
`venv\Scripts\activate`

- On macOS and Linux:
`source venv/bin/activate`

#### Install Dependencies
`pip install -r requirements.txt`

### Run the tests 

`python exec.py`

This will launch the browser multiple times to test different scenarios as specified in the challenge requirements. Ensure your browser driver (ChromeDriver or geckodriver) is correctly installed and accessible in your system's PATH to avoid any issues with launching the browser.


  
