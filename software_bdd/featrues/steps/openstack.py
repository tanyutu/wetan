from behave import *
from config_parser import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select

@given('The evnironment is {env}')
# we can use this in background to setup the test_env
def step_impl(context, env):
    context.data = env_setting(env)

@when('create osp "{product}" "{plugin_type}" "{osp_version}" "{RHEL_version}"')
# on osp first entry page (common usage for every plugin)
def step_impl(context, product, plugin_type, osp_version, RHEL_version):
    vendor_product_page(context, product)
    paramenter_fill(context, osp_version, RHEL_version, plugin_type)
    common_fields(context)
    continue_btn = context.driver.find_element_by_id('button_next')
    continue_btn.click()
@When('feature-based manila {protocol-features}')
# for cinder/manila certs
def step_impl(context, protocol_features):
    pass

def vendor_product_page(context, product):
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

def paramenter_fill(context, osp_version, RHEL_version, plugin_type):
    WebDriverWait(context.driver, 1000).until(
        EC.element_to_be_clickable((By.ID, "base_rhel_version")))
    redhat_product = Select(context.driver.find_element_by_id('rh_product_version'))
    redhat_product.select_by_visible_text(osp_version)
    rhel_versoin = Select(context.driver.find_element_by_id('base_rhel_version'))
    rhel_versoin.select_by_visible_text(RHEL_version)
    component = Select(context.driver.find_element_by_id('component'))
    component.select_by_visible_text(plugin_type)

def common_fields(context):
    product_version = context.driver.find_element_by_name('cert_version')
    product_version.send_keys('1.1')
    source_code_url = context.driver.find_element_by_name('source_url')
    source_code_url.send_keys('http://source.code.com')
    blueprint_url = context.driver.find_element_by_name('blueprint_url')
    blueprint_url.send_keys('http://bluepirnt.com')
    install_guide_url = context.driver.find_element_by_name('install_guide')
    install_guide_url.send_keys('http://install.guide.com')
    user_guide_url = context.driver.find_element_by_name('user_guide')
    user_guide_url.send_keys('http://user.guide.com')
    configuration_url = context.driver.find_element_by_name('configuration')
    configuration_url.send_keys('http://configuration.com')
    # urls = context.driver.find_elements_by_xpath("//input[contains(@name,'url')]")
    # for url in urls:
    #     url.send_keys('http://testing.com')
    hostname = context.driver.find_element_by_name('hostname')
    hostname.send_keys('OSP testing')
    radios = context.driver.find_elements_by_xpath("//input[@type='radio']")
    for radio in radios:
        if radio.get_attribute('value') == '1':
            radio.click()
    year = Select(context.driver.find_element_by_id('release_year'))
    month = Select(context.driver.find_element_by_id('release_month'))
    day = Select(context.driver.find_element_by_id('release_day'))
    year.select_by_visible_text('2018')
    month.select_by_visible_text('11')
    day.select_by_visible_text('13')
















