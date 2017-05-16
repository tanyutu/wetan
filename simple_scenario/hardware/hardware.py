import sys, os
sys.path.insert(0, os.path.abspath('../../common'))
from config.config import TestConfig
from func.test_initial import ParentTest
from selenium import webdriver
from func.hardware_e2e import Hardware
from func.common_func import CommonFunc
from datetime import datetime
bug_id = 0
model =''
spec_id = 0

class Create(ParentTest):
    def setUp(self):
        self.env = self.args.env
        self.test_conf = TestConfig(self.env)
        self.url = self.test_conf.get_url()
        self.user = self.test_conf.get_username()
        self.passw = self.test_conf.get_passwd()
        self.driver = webdriver.Firefox()
        self.func = CommonFunc()

    def tearDown(self):
        # self.driver.close()
        pass

    def test_hardware_create(self):
        self.driver.get(self.url)
        self.hardware = Hardware(self.driver)
        self.hardware.sso_login(self.user, self.passw)
        global model
        model = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        self.hardware.hardware_create(model)
        self.hardware.wait_summary_show()
        current_url = self.func.get_curr_url(self.driver)

        global bug_id
        bug_id = self.func.id_in_url(current_url, '=')
        print bug_id
        global spec_id
        spec_id = self.hardware.spec_id_retrive()
        print spec_id

class ComponentAndPlan(ParentTest):
    def setUp(self):
        self.env = self.args.env
        self.test_conf = TestConfig(self.env)
        self.url = self.test_conf.get_review_url()
        self.user = self.test_conf.get_review_user()
        self.passw = self.test_conf.get_review_passw()
        self.driver = webdriver.Firefox()
        self.driver.get(self.url)
        self.hardware = Hardware(self.driver)
        self.hardware.review_login(self.user, self.passw)
        self.url = self.test_conf.get_url()
    def tearDown(self):
        pass

    def test_add_component(self):
        url = '%s/show.cgi?id=%s' % (self.url, spec_id)
        self.hardware.component_add(url)

    def test_add_plan(self):
        url = '%s/show.cgi?id=%s' % (self.url, bug_id)
        self.hardware.test_plan_add(url)

    def test_frozen(self):
        url = '%s/show.cgi?id=%s' % (self.url, bug_id)
        self.hardware.test_plan_forzen(url)

class TestResult(ParentTest):
    def setUp(self):
        self.env = self.args.env
        self.test_conf = TestConfig(self.env)
        self.url = self.test_conf.get_url()
        self.user = self.test_conf.get_username()
        self.passw = self.test_conf.get_passwd()
        self.driver = webdriver.Firefox()
        self.driver.get(self.url)
        self.hardware = Hardware(self.driver)
        self.hardware.sso_login(self.user, self.passw)
        self.url = '%s/show.cgi?id=%s' % (self.url, bug_id)
        self.driver.get(self.url)
    def tearDown(self):
        pass

    def test_upload(self):
        self.hardware.test_result_upload(self.url)

    def test_leverage(self):
        self.hardware.test_leverage(self.url)




class Publish(ParentTest):
    def setUp(self):
        self.env = self.args.env
        self.test_conf = TestConfig(self.env)
        self.url = self.test_conf.get_review_url()
        self.user = self.test_conf.get_review_user()
        self.passw = self.test_conf.get_review_passw()
        self.driver = webdriver.Firefox()
        self.driver.get(self.url)
        self.hardware = Hardware(self.driver)
        self.hardware.review_login(self.user, self.passw)
        self.url = self.test_conf.get_url()
        self.url = '%s/show.cgi?id=%s' % (self.url, bug_id)
        self.driver.get(self.url)

    def tearDown(self):
        pass

    def test_confirm_leverage(self):
        self.hardware.test_confirm()

    def test_publish(self):
        self.hardware.publish_cert()




