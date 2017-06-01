from behave import *

@given('background print')
def step_impl(context):
    print('this is background ########')
    print()

@given('scenario 1')
def step_impl(context):
    print ('first scenario print ^^^^^^^^^^^^^^^')
    print()

@given('scenario 2')
def step_impl(context):
    print ('second scenario print ***************')
    print()

@given('scenario 3')
def step_impl(context):
    print('third scenario print $$$$$$$$$$$$$$')
    print()

@given('Appendix')
def ste_impl(context):
    pass

@when('context attribute')
def step_impl(context):
    print (context.feature)
    print(context.scenario)
    print()

