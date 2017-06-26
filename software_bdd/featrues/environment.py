from selenium import webdriver
from steps.config_parser import test_env_setting
def before_all(context):
    context.data = test_env_setting()

def before_scenario(context, scenario):
    context.driver = webdriver.Firefox()









