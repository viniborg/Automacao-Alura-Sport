from page_objects.page_objects_base import Driver
from resources.fake_user import FakeUser
from page_objects.register import RegisterNewUser
from page_objects.login import Login
import unittest


class FeatureRegister(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.fake = FakeUser()

    def test_register_sucess(self):
        register_page = RegisterNewUser(self.driver)
        register_page.find_screen_elements()
        register_page.register_user(self.fake.name, self.fake.password)

    def test_sucess_login(self):
        self.test_register_sucess()
        login_page = Login(self.driver)
        login_page.find_screen_elements()
        login_page.login(self.fake.name, self.fake.password)

    def tearDown(self):
        self.driver.instance.quit()
