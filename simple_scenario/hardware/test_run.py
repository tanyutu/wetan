import sys, os
sys.path.insert(0, os.path.abspath('../../common'))
from func.test_runner import TestArg, TestSuit, TestRunner
from hardware import  Create, ComponentAndPlan, TestResult, Publish
from test_result_generator import test_result_generate

# generate a test result
test_result_generate()

# get the parameters from terminal
test_arg = TestArg()
args = test_arg.args()

# get test suit
test1 = TestSuit()
class_names = [Create, ComponentAndPlan, TestResult, Publish]
suit1 = test1.make_suit(class_names, args)

# test run
run1 = TestRunner()
run1.clean()
run1.runner(suit1, 'hardware')
