import conftest
from MainPage import MainPage

###Тест на авторизацию и поиск игры
def test_login_and_find_a_game(browser):
    page = MainPage(browser)
    page.click_login_button()
    page.authorization('john', 'poker')
    page.verify_log_in()
    page.find_a_game()

###Тест на создание аккаунта
def test_sign_up(browser):
    page = MainPage(browser)
    page.click_signup_button()
    page.create_account('MyShinyTest', 'fake@mail.com', 'test12345')
    page.verify_log_in()

