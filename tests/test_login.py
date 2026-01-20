def test_login_invalid(driver):
    from pages.login_page import LoginPage

    login = LoginPage(driver)
    login.open()
    login.login("tomsmith", "wrongpassword")

    assert "invalid" in login.get_message().lower()

def test_login_empty_password(driver):
    from pages.login_page import LoginPage

    login = LoginPage(driver)
    login.open()
    login.login("tomsmith", "")

    assert "invalid" in login.get_message().lower()

def test_login_empty_username(driver):
    from pages.login_page import LoginPage

    login = LoginPage(driver)
    login.open()
    login.login("", "SuperSecretPassword!")

    assert "invalid" in login.get_message().lower()

def test_login_valid(driver):
    from pages.login_page import LoginPage

    login = LoginPage(driver)
    login.open()
    login.login("tomsmith", "SuperSecretPassword!")

    assert "secure area" in login.get_message().lower()
