import unittest
from selenium import webdriver
from pages.base_page_object import BasePage
from locators import LoginPageLocators
from TestData import TestData

#Base Class for the tests
class Test_Base(unittest.TestCase):

    def setUp(self):
        # Setting up how we want Chrome to run
        self.driver = self.startBrowser('chrome')
        self.driver.maximize_window()

    def tearDown(self):
        # To do the cleanup after test has executed.
        self.driver.close()
        self.driver.quit()

    def startBrowser(self, name = 'chrome'):
        """
        browsers，"firefox"、"chrome"、"ie"、"phantomjs"
        """
        try:
            if name == "firefox" or name == "Firefox" or name == "ff":
                print("start browser name :Firefox")
                return webdriver.Firefox()
            elif name == "chrome" or name == "Chrome":
                print("start browser name :Chrome")
                return webdriver.Chrome()
            elif name == "ie" or name == "Ie":
                print("start browser name :Ie")
                return webdriver.Ie()
            elif name == "phantomjs" or name == "Phantomjs":
                print("start browser name :phantomjs")
                return webdriver.PhantomJS()
            else:
                print("Not found this browser,You can use ‘firefox‘, ‘chrome‘, ‘ie‘ or ‘phantomjs‘")
        except Exception as msg:
            print("message: %s" % str(msg))
        