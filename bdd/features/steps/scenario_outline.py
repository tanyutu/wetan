from behave import *

@Given('I have a letter')
def step_impl(context):
    pass

@when('I input a letter {letter}')
def step_impl(context, letter):
    context.letter = letter

@Then('the input letter is Equal to {target_letter}')
def step_impl(context,target_letter):
    context.target_letter = target_letter
    assert context.target_letter is context.target_letter




