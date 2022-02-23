from page_objects.page_objects_base import AppiumElement
from appium.webdriver.common.appiumby import AppiumBy
from page_objects.login import Login


class RegisterNewUser(AppiumElement):
    
    locators = {
        'input_user': (AppiumBy.ID, 'br.com.alura.aluraesporte:id/input_nome'),
        'input_password': (AppiumBy.ID, 'br.com.alura.aluraesporte:id/input_senha'),
        'input_confirm_password': (AppiumBy.ID, 'br.com.alura.aluraesporte:id/input_confirmar_senha'),
        'btn_register_user': (AppiumBy.ID, 'br.com.alura.aluraesporte:id/cadastro_usuario_botao_cadastrar')
    }
    
    def __init__(self, driver):
        super().__init__(driver)
        self.register_page = Login(driver)
        self.find_element(self.register_page.btn_register_id).click()
        
    def register_user(self, user, password):
        self.find_element(RegisterNewUser.locators['input_user']).send_keys(user)
        self.find_element(RegisterNewUser.locators['input_password']).send_keys(password)
        self.find_element(RegisterNewUser.locators['input_confirm_password']).send_keys(password)
        self.find_element(RegisterNewUser.locators['btn_register_user']).click()

