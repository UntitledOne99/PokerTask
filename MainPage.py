from BasePage import BasePage
from selenium.webdriver.common.by import By

###Локаторы оставил в таком виде для удобства и скорости, в работе вынес бы в отдельный документ и выбрал бы относительный путь вместо абсолютного

class MainPage(BasePage):

###Метод для того чтобы найти кнопку логина
    def click_login_button(self):
        self.find_element((By.XPATH,
                           '//div[@class="panel button SimpleButton SimpleButton_v_flat SimpleButton_c_gradient_primary SimpleButton_use_text_use_icon MiniUserInfo__login_button SimpleButton_interactive"]')).click()

###Метод для того чтобы найти кнопку регистрации
    def click_signup_button(self):
        self.find_element((By.XPATH,
                           '/html/body/div/div/div[1]/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]')).click()

###Метод на создание аккаунта
    def create_account(self,login,email,password):
        base_input = '/html/body/div/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[1]'
        self.find_element((By.XPATH,f'{base_input}//input[@type="email"]')).send_keys(email)
        self.find_elements((By.XPATH,f'{base_input}//input[@type="text"]'))[0].send_keys(login)
        password_inputs = self.find_elements((By.XPATH,f'{base_input}//input[@type="password"]' ))
        [line.send_keys(password) for line in password_inputs]
        self.find_element((By.XPATH,'/html/body/div/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[3]/div[2]')).click()

###Метод для авторизации
    def authorization(self, login, password):
        self.find_element((By.XPATH,'/html/body/div/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/input')).send_keys(login)
        self.find_element((By.XPATH,'/html/body/div/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div[2]/div/div/div[1]/input')).send_keys(password)
        self.find_element((By.XPATH,'/html/body/div/div/div[1]/div/div[2]/div[2]/div/div[3]/div[1]')).click()
        profile_name = self.find_element((By.XPATH,'/html/body/div/div/div[1]/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div[1]/div/span')).text

###Проверка успешности авторизации
    def verify_log_in(self):
        self.find_element((By.XPATH,'/html/body/div/div/div[1]/div/div[1]/div/div/div/div[2]/div/div/div[1]/div')).click()
        self.find_element((By.XPATH,'/html/body/div/div/div[1]/div/div[1]/div/div/div/div[6]/div/div[2]/div/div/div[1]/div/div/div[2]')).click()
        self.find_element((By.XPATH,'/html/body/div/div/div[1]/div/div[1]/div/div/div/div[6]/div/div[2]/div/div/div[1]/div/div/div[3]')).click()
        account_tab = self.find_element((By.XPATH,'/html/body/div/div/div[1]/div/div[2]/div[2]/div'))
        assert account_tab
        self.find_element((By.XPATH,'/html/body/div/div/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div')).click()

###Метод для поиска доступной игры
    def find_a_game(self):
        self.find_element((By.XPATH,'/html/body/div/div/div[1]/div/div[1]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[6]/div/div[2]/div/div')).click()
        self.find_element((By.XPATH,'/html/body/div/div/div[1]/div/div[1]/div/div/div/div[4]/div[2]/div/div/div[3]/div[1]')).click()