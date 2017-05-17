from behave import *

@Given('before features usage')
def step_impl(context):
    pass
@Then('check the original value')
def step_impl(context):
    print(context.first_output)
    print()
    assert context.first_output == 1
    assert context.second_output == 2

@When('set new value')
def step_impl(context):
    context.first_output = 2
    assert context.first_output == 2
    context.second_output = 3
    assert context.second_output == 3

