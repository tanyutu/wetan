import unittest
class ParentTest(unittest.TestCase):
    """
    rewrite the unittest to recevie args (have self.args)
    """
    def __init__(self, methodName='runTest', args=None):
        super(ParentTest, self).__init__(methodName)
        self.args = args
        unittest.TestResult