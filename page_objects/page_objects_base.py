from capabilities_config.capabilities import Capabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from abc import ABC, abstractmethod
from appium import webdriver


class Driver:

    def __init__(self):
        self.instance = webdriver.Remote('http://localhost:4723/wd/hub', Capabilities.capabilities)


class AppiumElement(ABC):

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.instance.find_element(*locator)

    def element_is_visible(self, locator):
        condition = EC.presence_of_element_located(locator)
        return bool(WebDriverWait(self.driver.instance, 10).until(condition))

    @abstractmethod
    def find_screen_elements(self):
        pass
