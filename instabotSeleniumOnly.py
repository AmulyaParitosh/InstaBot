from time import sleep
from selenium import webdriver

browser=webdriver.Firefox(executable_path=r'C:/geckodriver-v0.29.0-win64/geckodriver.exe')
browser.implicitly_wait(5)

class Home_Page:
    def __init__(self, browser):
        self.browser = browser
        

    def get_page(self):
        self.browser.get("https://www.instagram.com/")
        sleep(3)
        return Login_Page(self.browser)
    
class Login_Page:
    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        username_input = self.browser.find_element_by_css_selector("input[name='username']")
        password_input = self.browser.find_element_by_css_selector("input[name='password']")

        username_input.send_keys(username)
        password_input.send_keys(password)

        login = self.browser.find_element_by_css_selector("button[type='submit']")
        login.click()

def test_login():
    home_page = Home_Page(browser)
    login = home_page.get_page()
    login.login("mr_a.paritosh", "MR@p@R1+0&h")

    sleep(15)
    browser.close()

test_login()

