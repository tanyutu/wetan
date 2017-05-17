from behave import *

@Given('before features usage')
def step_impl(context):
    pass
@Then('check first_output value')
def step_impl(context):
    print('the first_output value is ' + str(context.first_output))
    print()

@When('set new value')
def step_impl(context):
    context.first_output = 2
    print('the new first_output value is ' + str(context.first_output))
    print()


