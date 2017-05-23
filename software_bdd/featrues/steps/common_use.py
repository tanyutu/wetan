from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@given('sso_login cwe')
def ste_impl(context):
    cwe_url = context.data['common']['cwe']['url']
    cwe_username = context.data['common']['cwe']['sso_username']
    cwe_passw = context.data['common']['cwe']['sso_password']
    context.driver.get(cwe_url)
    username = context.driver.find_element_by_id('username')
    username.send_keys(cwe_username)
    passw = context.driver.find_element_by_id('password')
    passw.send_keys(cwe_passw)
    submit_btn = context.driver.find_element_by_id('_eventId_submit')
    submit_btn.click()

@then('create cert type show')
def step_impl(context):
    create_btn = WebDriverWait(context.driver, 100).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Create")))
    create_btn.click()
    WebDriverWait(context.driver, 100).until(
        EC.presence_of_element_located((By.XPATH, "//a[@title = 'Red Hat Enterprise Linux']")))
