from selenium.webdriver.common.by import By

class LoginPage:
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.XPATH, "//button")
    MESSAGE = (By.ID, "flash")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://the-internet.herokuapp.com/login")

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BTN).click()

    def get_message(self):
        return self.driver.find_element(*self.MESSAGE).text
