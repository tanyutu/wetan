import unittest
import argparse
import os, glob
import HTMLTestRunner
from datetime import datetime


class TestArg(object):
    """
    return args which from terminal (env)
    """
    def __init__(self):
        self.parser = argparse.ArgumentParser()

    def args(self):
        self.parser.add_argument('-e', '--env',  choices=['qa', 'stage'], help='testing env')
        self.parser.add_argument('-v','--version')
        args = self.parser.parse_args()
        return args

class TestSuit(object):
    """
    add all test cases in required test classes in one test suit
    """
    def __init__(self):
        self.testloader = unittest.TestLoader()
        self.case_suit = unittest.TestSuite()

    def make_suit(self, class_names, args):
        suit = self.case_suit
        for class_name in class_names:
            print class_name
            testcase_names = self.testloader.getTestCaseNames(class_name)
            for name in testcase_names:
                suit.addTest(class_name(name, args))
        return suit

class TestRunner(object):
    """
    run test suit
    """
    def clean(self):
        # for item in glob.glob(os.getcwd() + '/*.gz'):
        #     os.remove(item)
        for item in glob.glob(os.getcwd() + '/*.png'):
            os.remove(item)
        for item in glob.glob(os.getcwd() + '/*.html'):
            os.remove(item)

    def runner(self, suit, report_name):
        # runner = unittest.TextTestRunner()
        report_path = os.path.abspath('../../test_report')
        fp = open(report_path +'/' + report_name+ '_'+ datetime.now().strftime('%b-%d-%y %H:%M:%S') + '.html','wb')
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='test result', description=u'result:')
        runner.run(suit)
        fp.close()








