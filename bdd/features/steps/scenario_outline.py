from behave import *

@Given('I have a letter')
def step_impl(context):
    pass

@when('I input a letter {letter}')
def step_impl(context, letter):
    context.letter = letter
    print("the letter " + context.letter)
    print()

@Then('the input letter is Equal to {target_letter}')
def step_impl(context,target_letter):
    context.target_letter = target_letter
    print (context.target_letter)
    assert context.letter == context.target_letter





