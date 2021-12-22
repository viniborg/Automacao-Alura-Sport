from page_objects.page_objects_base import AppiumElement
from appium.webdriver.common.appiumby import AppiumBy
from page_objects.login import Login


class RegisterNewUser(AppiumElement):

    def __init__(self, driver):
        super().__init__(driver)
        self.open_register_page = Login(driver)
        self.open_register_page.find_element(self.open_register_page.btn_register_id).click()
        self.input_user_id = (AppiumBy.ID, 'br.com.alura.aluraesporte:id/input_nome')
        self.input_password_id = (AppiumBy.ID, 'br.com.alura.aluraesporte:id/input_senha')
        self.input_confirm_password_id = (AppiumBy.ID, 'br.com.alura.aluraesporte:id/input_confirmar_senha')
        self.btn_register_user_id = (AppiumBy.ID, 'br.com.alura.aluraesporte:id/cadastro_usuario_botao_cadastrar')

    def find_screen_elements(self):
        self.input_user = self.find_element(self.input_user_id)
        self.input_password = self.find_element(self.input_password_id)
        self.input_confirm_password = self.find_element(self.input_confirm_password_id)
        self.btn_register_user = self.find_element(self.btn_register_user_id)

    def register_user(self, user, password, confirm_password):
        self.input_user.send_keys(user)
        self.input_password.send_keys(password)
        self.input_confirm_password.send_keys(confirm_password)
        self.btn_register_user.click()

