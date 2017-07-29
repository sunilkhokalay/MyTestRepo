import unittest


class ComplexMath(object):
    '''
    This class represent complex numbers
    '''
    def __init__(self, realpart, imaginarypart):
        self.x = realpart
        self.y = imaginarypart

    def __add__(self, other):
        return ComplexMath(self.x+other.x,self.y+other.y)

    def __sub__(self, other):
        return ComplexMath(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        if self.y < 0:
            return "{}-j{}".format(self.x,self.y)
        else:
            return "{}+j{}".format(self.x,self.y)

    def __repr__(self):
        return "ComplexMath({},{})".format(self.x,self.y)

class TestComplexMath(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("This is common setup")

    @classmethod
    def tearDownClass(cls):
        print("This is common clean up")

    def setUp(self):
        print("This is test setup to initialize test values")
        self.a = ComplexMath(5, 5)
        self.b = ComplexMath(5, 5)

    def tearDown(self):
        print("This is test tear down to clean the test values")
        del self.a
        del self.b

    def testComplexAddtion(self):
        print(self.a+self.b)
        assert (self.a+self.b) == (ComplexMath(10,10)),"Addition failed!"

    def testComplexSubstraction(self):
        print(self.a-self.b)
        assert (self.a - self.b) == (ComplexMath(0, 0)), "Substraction failed!"

    def testOne(self):
        self.assertEqual("Hi","Hi","Strings are not equal")

    @unittest.skip
    def testTwo(self):
        self.assertListEqual([1,2,3,4], [4,3,2,1], "Lists are not equal")

    def testThree(self):
        self.assertDictEqual({'a':1,'b':2},{'b':2,'a':1},"DIct not equal")

    def testFour(self):
        self.assertAlmostEqual(1.6, 1.599, places=2, msg = "Float are not almost equal")


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestComplexMath))
# suite.addTest(TestComplexMath("testOne"))
# suite.addTests([TestComplexMath("testOne"),TestComplexMath("testFour")])

runner = unittest.TextTestRunner()
runner.run(suite)
