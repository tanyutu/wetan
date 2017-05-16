from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import sys, os
import glob


class RhcertHardware(object):
    def __init__(self, driver):
        self.driver = driver

    def sso_login(self, username, password):
        user = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, "username"))
        )
        user.send_keys(username)

        passw = self.driver.find_element_by_id('password')
        passw.send_keys(password)

        login_btn = self.driver.find_element_by_name('login')
        login_btn.click()

    def new_cert(self):
        new_cert_btn = WebDriverWait(self.driver, 120).until(EC.visibility_of_element_located(
            (By.XPATH, "//button[contains(text(),'New Certification')]")))
        # new_cert_btn = self.driver.find_element_by_xpath("//button[contains(text(),'New Certification')]")
        new_cert_btn.click()

    def new_product(self):
        new_product_btn = WebDriverWait(self.driver, 120).until(EC.visibility_of_element_located(
            (By.NAME, "vendorProductID")))
        new_product_btn.click()

    def hardware_product_input(self, make, model, category, pro_url, sup_url, spec_url, spec_status='preproduction'):
        make_input = self.driver.find_element_by_id('make')
        make_input.send_keys(make)

        model_input = self.driver.find_element_by_name('product_name')
        model_input.send_keys(model)

        category_select = self.driver.find_element_by_id('category')
        category_select.select_by_visible_text(category)

        pro_url_input = self.driver.find_element_by_name('product_url')
        pro_url_input.send_keys(pro_url)

        sup_url_input = self.driver.find_element_by_name('support_url')
        sup_url_input.send_keys(sup_url)

        spec_url_input = self.driver.find_element_by_name('specification_url')
        spec_url_input.send_keys(spec_url)

        if













