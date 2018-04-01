from tests.test_utils.test_utility import *


# This class tests if bishop legal moves are allowed as intended
class SquareTests(unittest.TestCase):

    def testEquals(self):
        self.assertTrue(A3 == A3)
        self.assertTrue(F7 == F7)

    def testHash(self):
        self.assertTrue(A1.order == 0)
        self.assertTrue(A3.order == 16)
        self.assertTrue(F7.order == 53)
        self.assertTrue(C2.order == 10)

    def testNotEquals(self):
        self.assertFalse(C2 == G6)
        self.assertFalse(H1 == A7)

    def testAdd(self):
        self.assertTrue(A3 + (1, 1) == B4)
        self.assertTrue(C3 + (4, 3) == G6)

    def testSub(self):
        self.assertTrue(C5 - (1, 1) == B4)
        self.assertTrue(F7 - (2, 3) == D4)

    def testLessThan(self):
        self.assertTrue(A2 < A3)
        self.assertTrue(B1 < B7)
        self.assertTrue(A3 < B4)
        self.assertTrue(C3 < G6)

    def testRepresentation(self):
        self.assertTrue(A2.__repr__() == "A2")
        self.assertTrue(B1.__repr__() == "B1")
        self.assertTrue(A3.__repr__() == "A3")
        self.assertTrue(C3.__repr__() == "C3")
