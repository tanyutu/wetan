from behave import *

@given('How to use the and but')
def step_impl(context):
    pass

@when('when I input a when')
def step_impl(context):
    assert True is not False

@when('this when can be replaced by but')
def step_impl(context):
    pass

@then('when i input a then')
def step_impl(context):
    assert context.failed is False

@then('this then can be replaced by and')
def step_impl(context):
    pass


@when('Do a duplicate thing')
def step_impl(context):
    context.execute_steps(u"""
        When when I input a when
        Then this then can be replaced by and
    """)
