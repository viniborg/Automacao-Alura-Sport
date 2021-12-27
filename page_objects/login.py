from page_objects.page_objects_base import AppiumElement
from appium.webdriver.common.appiumby import AppiumBy


class Login(AppiumElement):

    def __init__(self, driver):
        super().__init__(driver)
        self.input_user_id = (AppiumBy.ID, 'br.com.alura.aluraesporte:id/input_usuario')
        self.input_password_id = (AppiumBy.ID, 'br.com.alura.aluraesporte:id/input_senha')
        self.btn_login_id = (AppiumBy.ID, 'br.com.alura.aluraesporte:id/login_botao_logar')
        self.btn_register_id = (AppiumBy.ID, 'br.com.alura.aluraesporte:id/login_botao_cadastrar_usuario')
        self.error_login_id = (AppiumBy.ID, 'br.com.alura.aluraesporte:id/mensagem_erro_login')
        self.element_action_bar = (AppiumBy.ID, 'br.com.alura.aluraesporte:id/action_bar')

    def find_screen_elements(self):
        self.input_user = self.find_element(self.input_user_id)
        self.input_password = self.find_element(self.input_password_id)
        self.btn_login = self.find_element(self.btn_login_id)
        self.btn_register = self.find_element(self.btn_register_id)

    def login(self, user, password):
        self.input_user.send_keys(user)
        self.input_password.send_keys(password)
        self.btn_login.click()
        self.element_is_visible(self.element_action_bar)

    def error_login_is_visible(self):
        return self.element_is_visible(self.error_login_id)
