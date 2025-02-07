import conftest
from MainPage import MainPage

def test_login_and_find_a_game(browser):
    page = MainPage(browser)
    page.click_login_button()
    page.send_credentials('john','poker')
    page.verify_log_in()
    page.find_a_game()

def test_sign_up(browser):
    page = MainPage(browser)
    page.click_signup_button()
    page.create_account('MyShinyTest', 'fake@mail.com', 'test12345')
    page.verify_log_in()

