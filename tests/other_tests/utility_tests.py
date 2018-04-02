from tests.test_utils.test_utility import *


# This class tests if bishop legal moves are allowed as intended
class UtilityTests(unittest.TestCase):

    def testFileAdvanceCheck(self):
        # File advance (asserts true)
        self.assertTrue(Utility.fileAdvanceCheck(Move(A1, B1)))
        self.assertTrue(Utility.fileAdvanceCheck(Move(E1, D1)))
        # Both advance (asserts true)
        self.assertTrue(Utility.fileAdvanceCheck(Move(H1, C2)))
        # Rank advance (asserts false)
        self.assertFalse(Utility.fileAdvanceCheck(Move(A1, A2)))
        # Same square (asserts false)
        self.assertFalse(Utility.fileAdvanceCheck(Move(F3, F3)))

    def testRankAdvanceCheck(self):
        # Rank advance (asserts true)
        self.assertTrue(Utility.rankAdvanceCheck(Move(A1, A2)))
        self.assertTrue(Utility.rankAdvanceCheck(Move(E5, E1)))
        # Both advance (asserts true)
        self.assertTrue(Utility.rankAdvanceCheck(Move(H7, B6)))
        # File advance (asserts false)
        self.assertFalse(Utility.rankAdvanceCheck(Move(A1, B1)))
        # Same square (asserts false)
        self.assertFalse(Utility.rankAdvanceCheck(Move(B7, B7)))

    def testFileAdvanceOnlyCheck(self):
        # File advance (asserts true)
        self.assertTrue(Utility.fileAdvanceOnlyCheck(Move(A1, B1)))
        self.assertTrue(Utility.fileAdvanceOnlyCheck(Move(E1, D1)))
        # Both advance (asserts false)
        self.assertFalse(Utility.fileAdvanceOnlyCheck(Move(H1, C2)))
        # Rank advance (asserts false)
        self.assertFalse(Utility.fileAdvanceOnlyCheck(Move(A1, A2)))
        # Same square (asserts false)
        self.assertFalse(Utility.fileAdvanceOnlyCheck(Move(F3, F3)))

    def testRankAdvanceOnlyCheck(self):
        # Rank advance (asserts true)
        self.assertTrue(Utility.rankAdvanceOnlyCheck(Move(A1, A2)))
        self.assertTrue(Utility.rankAdvanceOnlyCheck(Move(E5, E1)))
        # Both advance (asserts false)
        self.assertFalse(Utility.rankAdvanceOnlyCheck(Move(H7, B6)))
        # File advance (asserts false)
        self.assertFalse(Utility.rankAdvanceOnlyCheck(Move(A1, B1)))
        # Same square (asserts false)
        self.assertFalse(Utility.rankAdvanceOnlyCheck(Move(B7, B7)))

    def testFileOrRankAdvanceExclusiveCheck(self):
        # File advance (asserts true)
        self.assertTrue(Utility.fileOrRankAdvanceExclusiveCheck(Move(A1, B1)))
        self.assertTrue(Utility.fileOrRankAdvanceExclusiveCheck(Move(E1, D1)))
        # Both advance (asserts false)
        self.assertFalse(Utility.fileOrRankAdvanceExclusiveCheck(Move(H1, C2)))
        # Same square (asserts false)
        self.assertFalse(Utility.fileOrRankAdvanceExclusiveCheck(Move(F3, F3)))

        # Rank advance (asserts true)
        self.assertTrue(Utility.fileOrRankAdvanceExclusiveCheck(Move(A1, A2)))
        self.assertTrue(Utility.fileOrRankAdvanceExclusiveCheck(Move(E5, B5)))
        # Both advance (asserts false)
        self.assertFalse(Utility.fileOrRankAdvanceExclusiveCheck(Move(H7, B6)))
        # Same square (asserts false)
        self.assertFalse(Utility.fileOrRankAdvanceExclusiveCheck(Move(B7, B7)))

    def testFileOrRankAdvanceBothCheck(self):
        # Both advance (asserts true)
        self.assertTrue(Utility.fileOrRankAdvanceBothCheck(Move(H1, C2)))
        # File advance (asserts false)
        self.assertFalse(Utility.fileOrRankAdvanceBothCheck(Move(A1, B1)))
        self.assertFalse(Utility.fileOrRankAdvanceBothCheck(Move(E1, D1)))
        # Same square (asserts false)
        self.assertFalse(Utility.fileOrRankAdvanceBothCheck(Move(F3, F3)))
        # Both advance (asserts true)
        self.assertTrue(Utility.fileOrRankAdvanceBothCheck(Move(H7, B6)))
        # Rank advance (asserts false)
        self.assertFalse(Utility.fileOrRankAdvanceBothCheck(Move(A1, A2)))
        self.assertFalse(Utility.fileOrRankAdvanceBothCheck(Move(E5, B5)))
        # Same square (asserts false)
        self.assertFalse(Utility.fileOrRankAdvanceBothCheck(Move(B7, B7)))

    def testGetFileAndRankAdvance(self):
        self.assertTrue(Utility.getFileAndRankAdvance(Move(A1, B1)) == (1, 0))
        self.assertTrue(Utility.getFileAndRankAdvance(Move(E1, D1)) == (-1, 0))
        self.assertTrue(Utility.getFileAndRankAdvance(Move(H1, C2)) == (-5, 1))
        self.assertTrue(Utility.getFileAndRankAdvance(Move(F3, F3)) == (0, 0))
        self.assertTrue(Utility.getFileAndRankAdvance(Move(A1, A2)) == (0, 1))
        self.assertTrue(Utility.getFileAndRankAdvance(Move(E5, B5)) == (-3, 0))
        self.assertTrue(Utility.getFileAndRankAdvance(Move(H7, B6)) == (-6, -1))
        self.assertTrue(Utility.getFileAndRankAdvance(Move(B7, B7)) == (0, 0))

    def testGetFileAndRankSingleAdvance(self):
        self.assertTrue(Utility.getFileAndRankSingleAdvance((1, 0)) == (1, 0))
        self.assertTrue(Utility.getFileAndRankSingleAdvance((-1, 0)) == (-1, 0))
        self.assertTrue(Utility.getFileAndRankSingleAdvance((-5, 1)) == (-5, 1))
        self.assertTrue(Utility.getFileAndRankSingleAdvance((0, 0)) == (0, 0))
        self.assertTrue(Utility.getFileAndRankSingleAdvance((0, 1)) == (0, 1))
        self.assertTrue(Utility.getFileAndRankSingleAdvance((-3, 0)) == (-1, 0))
        self.assertTrue(Utility.getFileAndRankSingleAdvance((-6, -1)) == (-6, -1))
        self.assertTrue(Utility.getFileAndRankSingleAdvance((0, 0)) == (0, 0))
        self.assertTrue(Utility.getFileAndRankSingleAdvance((5, 0)) == (1, 0))
        self.assertTrue(Utility.getFileAndRankSingleAdvance((4, 2)) == (2, 1))
        self.assertTrue(Utility.getFileAndRankSingleAdvance((2, 1)) == (2, 1))
        self.assertTrue(Utility.getFileAndRankSingleAdvance((5, 4)) == (5, 4))
        self.assertTrue(Utility.getFileAndRankSingleAdvance((2, 4)) == (1, 2))
        self.assertTrue(Utility.getFileAndRankSingleAdvance((1, 2)) == (1, 2))
        self.assertTrue(Utility.getFileAndRankSingleAdvance((-1, 1)) == (-1, 1))
        self.assertTrue(Utility.getFileAndRankSingleAdvance((-5, -5)) == (-1, -1))

    def testIsMoveInCorrectDirection(self):
        directionsList1 = []
        directionsList1.append((1, 2))
        directionsList1.append((2, 1))
        directionsList1.append((-1, 2))
        directionsList1.append((-2, 1))
        directionsList1.append((1, -2))
        directionsList1.append((2, -1))
        directionsList1.append((-1, -2))
        directionsList1.append((-2, -1))

        self.assertTrue(Utility.isMoveInCorrectDirection(Move(E1, F3), directionsList1, Strategy.jumping))

        directionsList2 = []
        directionsList2.append((1, 1))
        directionsList2.append((1, -1))
        directionsList2.append((-1, 1))
        directionsList2.append((-1, -1))
        directionsList2.append((1, 0))
        directionsList2.append((0, 1))
        directionsList2.append((-1, 0))
        directionsList2.append((0, -1))

        self.assertTrue(Utility.isMoveInCorrectDirection(Move(B4, C3), directionsList2, Strategy.sliding))

    def testAbsoluteGCD(self):
        self.assertTrue(Utility.absoluteGCD(1, 0) == 1)
        self.assertTrue(Utility.absoluteGCD(0, -1) == 1)
        self.assertTrue(Utility.absoluteGCD(-5, 1) == 1)
        self.assertTrue(Utility.absoluteGCD(2, 4) == 2)
        self.assertTrue(Utility.absoluteGCD(0, 0) == 0)
