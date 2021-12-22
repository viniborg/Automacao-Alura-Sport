from page_objects.page_objects_base import Driver
from page_objects.login import Login
from page_objects.register import RegisterNewUser
import unittest


class FeatureRegister(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()

    def test_register_sucess(self):
        register_page = RegisterNewUser(self.driver)
        register_page.find_screen_elements()
        register_page.register_user('user', '123', '123')

    def test_sucess_login(self):
        self.test_register_sucess()
        login_page = Login(self.driver)
        login_page.find_screen_elements()
        login_page.login('user', '123')

    def tearDown(self):
        self.driver.instance.quit()
