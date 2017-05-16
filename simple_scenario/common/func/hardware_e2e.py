
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import sys, os
import glob

class Hardware(object):
    def __init__(self, driver):
        self.driver = driver

    def sso_login(self, username, passw):
        user = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.ID, "username"))
            )
        user.send_keys(username)

        passwd = self.driver.find_element_by_id('password')
        passwd.send_keys(passw)

        subumit_btn = self.driver.find_element_by_id('_eventId_submit')
        subumit_btn.click()

    def review_login(self, username, passw):

        user = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.ID, "cert-login-email"))
            )
        user.send_keys(username)

        passwd = self.driver.find_element_by_id('cert-login-password')
        passwd.send_keys(passw)

        login_btn = self.driver.find_element_by_xpath("//button[@name='GoAheadAndLogIn']")
        login_btn.click()

    def wait_summary_show(self):
        WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located((By.ID, "summary_tab"))
        )

    def specification_tab_show(self):
        spec_tab = WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located((By.ID, "specifications_tab"))
        )
        spec_tab.click()

    def review_tab_show(self):
        review_tab = WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located((By.ID, "review_tab"))
        )
        review_tab.click()


    def publish_tab_show(self):
        spec_tab = WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located((By.ID, "publish_tab"))
        )
        spec_tab.click()



    def hardware_create(self, model_name):
        create_link = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Create"))
        )
        create_link.click()
        cert_type = self.driver.find_element_by_xpath("//a[@title = 'Red Hat Enterprise Linux']")
        cert_type.click()

        time.sleep(30)

        vendor = Select(self.driver.find_element_by_id('vendor_id'))
        vendor.select_by_visible_text('Abbee')

        time.sleep(3)
        maker_radio = self.driver.find_element_by_id('use_new_make')
        maker_radio.click()
        time.sleep(3)
        new_make = self.driver.find_element_by_id('new_make')
        new_make.send_keys('ABBEE')

        model = self.driver.find_element_by_name('model')
        model.send_keys(model_name)

        catagory = Select(self.driver.find_element_by_name('category_id'))
        catagory.select_by_visible_text('Server')

        specification_status = self.driver.find_element_by_xpath("//input[@name='specification_status'][@value=0]")
        specification_status.click()

        policy = self.driver.find_element_by_id('read_policy')
        policy.click()

        contiune_btn = self.driver.find_element_by_xpath("//button[@value='Continue']")
        contiune_btn.click()

        commit_btn = self.driver.find_element_by_name('commit')
        commit_btn.click()



    def spec_id_retrive(self):
        spec_ele = self.driver.find_element_by_xpath(
            "//label[contains(text(), 'Hardware Specification')]/following-sibling::div[1]/a")
        if not spec_ele.is_displayed():
            advance_tab_ele = self.driver.find_element_by_link_text('Advanced')
            advance_tab_ele.click()
            spec_ele = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH,
                     "//label[contains(text(), 'Hardware Specification')]/following-sibling::div[1]/a")))
        spec_id = spec_ele.get_attribute('text')
        try:
            assert int(spec_id) > 0
        except AssertionError:
            sys.exit(1)
        return spec_id

    def component_add(self, url):
        component_name = 'component1'
        component_fea_name = 'CPUSCALING'

        self.driver.get(url)
        self.specification_tab_show()
        component = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, "general-1-description"))
        )
        component.send_keys(component_name)

        component_fea = self.driver.find_element_by_id('general-1-feature-1')
        component_fea.send_keys(component_fea_name)

        save_btn = self.driver.find_element_by_id('specification-submit')
        time.sleep(30)
        save_btn.click()

    def test_plan_add(self, url):
        self.driver.get(url)
        self.review_tab_show()
        self.driver.implicitly_wait(5)
        auto_generate_testplan = self.driver.find_element_by_xpath(
            "//button[@value='Automatically create test plans']")
        auto_generate_testplan.click()

    def test_plan_forzen(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        self.review_tab_show()
        change_testplan = self.driver.find_element_by_id(
            'testplanknob_change')
        if not change_testplan.is_displayed():
            change_testplan = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.ID, 'testplanknob_change')))
        change_testplan.click()

        submit = self.driver.find_element_by_xpath(
            '//div[@id="review"]//button[contains(text(), "Save Changes")]')
        submit.click()

    def test_result_upload(self, url):
        self.driver.get(url)
        self.review_tab_show()
        results_file_paths = glob.glob(os.getcwd() + '/*.gz')
        results_file_path = results_file_paths[0]
        print results_file_path
        browse_result = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "data"))
        )
        browse_result.send_keys(results_file_path)
        description = self.driver.find_element_by_id('description')
        description.send_keys('results file description')
        attach_file = self.driver.find_element_by_name('Attach')
        attach_file.click()

    def test_leverage(self, url):
        self.driver.get(url)
        self.review_tab_show()
        time.sleep(10)
        result = Select(self.driver.find_element_by_xpath(
            "//Select[contains(@name, 'testplan_result_64bits')]"))
        # result.select_by_value('328881')
        options = result.options
        for option in options:
            if option.get_attribute('value').isdigit():
                    option.click()
        submit = self.driver.find_element_by_xpath(
            '//div[@id="review"]//button[contains(text(), "Save Changes")]')
        submit.click()

    def test_confirm(self):
        self.review_tab_show()
        time.sleep(10)
        result = Select(self.driver.find_element_by_xpath(
            "//Select[contains(@class, 'testplan_confirm_option')]"))
        result.select_by_visible_text('Confirmed')
        submit = self.driver.find_element_by_xpath(
            '//div[@id="review"]//button[contains(text(), "Save Changes")]')
        submit.click()

    def publish_cert(self):
        self.publish_tab_show()
        spec_tab = WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located((By.ID, "make_public"))
        )
        spec_tab.click()

        certified_radio = self.driver.find_element_by_id('knob-resolve')
        certified_radio.click()

        tam_ack = self.driver.find_element_by_id('tam_ack')
        tam_ack.click()

        pub_btn = self.driver.find_element_by_id('publish_submit')
        pub_btn.click()


