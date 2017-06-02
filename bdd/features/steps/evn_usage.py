import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.realpath('%s/../../../../log' % __file__))
sys.path.insert(0, PROJECT_ROOT)



from definition import create_logger
from behave import *

logger = create_logger('bdd')

@Given('before features usage')
def step_impl(context):
    pass
@Then('check first_output value')
def step_impl(context):
    logger.debug('debug: the first_output value is ' + str(context.first_output))
    logger.info('info testing')
    logger.warning('warning testing')
    logger.critical('critical testing')

    logger.error('error testing: this is the first log')

@When('set new value')
def step_impl(context):
    context.first_output = 2
    print('the new first_output value is ' + str(context.first_output))
    print()


