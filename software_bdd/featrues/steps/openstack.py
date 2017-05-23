from behave import *
from config_parser import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select

@given('The evnironment is {env}')
def step_impl(context, env):
    context.data = env_setting(env)

@when('create osp "{product}" "{plugin_type}" "{osp_version}" "{RHEL_version}"')
def step_impl(context, product, plugin_type, osp_version, RHEL_version):
    cert_type = context.driver.find_element_by_xpath(
        "//a[@title = 'Red Hat Enterprise Linux Openstack Platform']")
    cert_type.click()
    WebDriverWait(context.driver, 100).until(
        EC.presence_of_element_located((By.ID, "vendor")))
    vendor = Select(context.driver.find_element_by_id('vendor'))
    vendor.select_by_visible_text('Abbee')
    product_list = Select(context.driver.find_element_by_name('product_name'))
    product_list.select_by_visible_text(product)
    policy = context.driver.find_element_by_id('readPolicy')
    policy.click()
    continue_btn = context.driver.find_element_by_id('button')
    continue_btn.click()














