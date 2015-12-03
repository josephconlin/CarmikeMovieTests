__author__ = 'Joseph Conlin'
"""Base class to represent possible browsers to be used in tests.
"""


from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import Settings


class TestBrowser:
    @staticmethod
    def get_browser():
        testDriver = webdriver.Remote(
            command_executor=Settings.seleniumHubURL,
            desired_capabilities=getattr(DesiredCapabilities, Settings.browserType).copy())
        testDriver.maximize_window()
        testDriver.get(Settings.baseURL)
        return testDriver
