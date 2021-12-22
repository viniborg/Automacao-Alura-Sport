from abc import ABC


class Capabilities(ABC):

    capabilities = dict(
        platformName='Android',
        platformVersion='11',
        automationName='uiautomator2',
        deviceName='Appium_test',
        app=('C:\\Users\\vinic\\Desktop\\AutomacaoApp\\resources\\alura_esporte.apk')
    )
