# -*- coding: utf-8 -*-

from selenium.webdriver.chrome.webdriver import WebDriver
import unittest
class test_login(unittest.TestCase):
    def setUp(self):
        self.driver = WebDriver()
        self.driver.implicitly_wait(10)

    def test_login_atlassian_account(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, user = 'rochman.elena@gmail.com', password = '12345.com')

    def open_home_page(self, driver):
        driver.get("https://trello.com/")

    def login(self, driver, user, password):
        driver.find_element_by_css_selector("[href='/login']").click()
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(user)
        driver.find_element_by_id("login").click()
        driver.find_element_by_css_selector("#password").click()
        driver.find_element_by_css_selector("#password").clear()
        driver.find_element_by_css_selector("#password").send_keys(password)
        driver.find_element_by_css_selector("#login-submit").click()


