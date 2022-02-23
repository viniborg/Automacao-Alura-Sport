from page_objects.page_objects_base import AppiumElement
from appium.webdriver.common.appiumby import AppiumBy


class Login(AppiumElement):

    locators = {
        'input_user' : (AppiumBy.ID, 'br.com.alura.aluraesporte:id/input_usuario'),
        'input_password' : (AppiumBy.ID, 'br.com.alura.aluraesporte:id/input_senha'),
        'btn_login' : (AppiumBy.ID, 'br.com.alura.aluraesporte:id/login_botao_logar'),
        'btn_register' : (AppiumBy.ID, 'br.com.alura.aluraesporte:id/login_botao_cadastrar_usuario'),
        'error_login_id' : (AppiumBy.ID, 'br.com.alura.aluraesporte:id/mensagem_erro_login'),
        'element_action_bar' : (AppiumBy.ID, 'br.com.alura.aluraesporte:id/action_bar')
    }

    def __init__(self, driver):
        super().__init__(driver)
        
    def login(self, user, password):
        self.find_element(Login.locators['input_user']).send_keys(user)
        self.find_element(Login.locators['input_password']).send_keys(password)
        self.find_element(Login.locators['btn_login']).click()
        self.element_is_visible(Login.locators['element_action_bar'])

    def error_login_is_visible(self):
        return self.element_is_visible(self.error_login_id)
