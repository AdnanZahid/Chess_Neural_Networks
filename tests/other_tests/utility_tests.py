from tests.test_utils.test_utility import *


# This class tests if bishop legal moves are allowed as intended
class UtilityTests(unittest.TestCase):

    def testFileAdvanceCheck(self):
        # File advance (asserts true)
        self.assertTrue(Utility.fileAdvanceCheck(EvaluationMove(A1, B1)))
        self.assertTrue(Utility.fileAdvanceCheck(EvaluationMove(E1, D1)))
        # Both advance (asserts true)
        self.assertTrue(Utility.fileAdvanceCheck(EvaluationMove(H1, C2)))
        # Rank advance (asserts false)
        self.assertFalse(Utility.fileAdvanceCheck(EvaluationMove(A1, A2)))
        # Same square (asserts false)
        self.assertFalse(Utility.fileAdvanceCheck(EvaluationMove(F3, F3)))

    def testRankAdvanceCheck(self):
        # Rank advance (asserts true)
        self.assertTrue(Utility.rankAdvanceCheck(EvaluationMove(A1, A2)))
        self.assertTrue(Utility.rankAdvanceCheck(EvaluationMove(E5, E1)))
        # Both advance (asserts true)
        self.assertTrue(Utility.rankAdvanceCheck(EvaluationMove(H7, B6)))
        # File advance (asserts false)
        self.assertFalse(Utility.rankAdvanceCheck(EvaluationMove(A1, B1)))
        # Same square (asserts false)
        self.assertFalse(Utility.rankAdvanceCheck(EvaluationMove(B7, B7)))

    def testFileAdvanceOnlyCheck(self):
        # File advance (asserts true)
        self.assertTrue(Utility.fileAdvanceOnlyCheck(EvaluationMove(A1, B1)))
        self.assertTrue(Utility.fileAdvanceOnlyCheck(EvaluationMove(E1, D1)))
        # Both advance (asserts false)
        self.assertFalse(Utility.fileAdvanceOnlyCheck(EvaluationMove(H1, C2)))
        # Rank advance (asserts false)
        self.assertFalse(Utility.fileAdvanceOnlyCheck(EvaluationMove(A1, A2)))
        # Same square (asserts false)
        self.assertFalse(Utility.fileAdvanceOnlyCheck(EvaluationMove(F3, F3)))

    def testRankAdvanceOnlyCheck(self):
        # Rank advance (asserts true)
        self.assertTrue(Utility.rankAdvanceOnlyCheck(EvaluationMove(A1, A2)))
        self.assertTrue(Utility.rankAdvanceOnlyCheck(EvaluationMove(E5, E1)))
        # Both advance (asserts false)
        self.assertFalse(Utility.rankAdvanceOnlyCheck(EvaluationMove(H7, B6)))
        # File advance (asserts false)
        self.assertFalse(Utility.rankAdvanceOnlyCheck(EvaluationMove(A1, B1)))
        # Same square (asserts false)
        self.assertFalse(Utility.rankAdvanceOnlyCheck(EvaluationMove(B7, B7)))

    def testFileOrRankAdvanceExclusiveCheck(self):
        # File advance (asserts true)
        self.assertTrue(Utility.fileOrRankAdvanceExclusiveCheck(EvaluationMove(A1, B1)))
        self.assertTrue(Utility.fileOrRankAdvanceExclusiveCheck(EvaluationMove(E1, D1)))
        # Both advance (asserts false)
        self.assertFalse(Utility.fileOrRankAdvanceExclusiveCheck(EvaluationMove(H1, C2)))
        # Same square (asserts false)
        self.assertFalse(Utility.fileOrRankAdvanceExclusiveCheck(EvaluationMove(F3, F3)))

        # Rank advance (asserts true)
        self.assertTrue(Utility.fileOrRankAdvanceExclusiveCheck(EvaluationMove(A1, A2)))
        self.assertTrue(Utility.fileOrRankAdvanceExclusiveCheck(EvaluationMove(E5, B5)))
        # Both advance (asserts false)
        self.assertFalse(Utility.fileOrRankAdvanceExclusiveCheck(EvaluationMove(H7, B6)))
        # Same square (asserts false)
        self.assertFalse(Utility.fileOrRankAdvanceExclusiveCheck(EvaluationMove(B7, B7)))

    def testFileOrRankAdvanceBothCheck(self):
        # Both advance (asserts true)
        self.assertTrue(Utility.fileOrRankAdvanceBothCheck(EvaluationMove(H1, C2)))
        # File advance (asserts false)
        self.assertFalse(Utility.fileOrRankAdvanceBothCheck(EvaluationMove(A1, B1)))
        self.assertFalse(Utility.fileOrRankAdvanceBothCheck(EvaluationMove(E1, D1)))
        # Same square (asserts false)
        self.assertFalse(Utility.fileOrRankAdvanceBothCheck(EvaluationMove(F3, F3)))
        # Both advance (asserts true)
        self.assertTrue(Utility.fileOrRankAdvanceBothCheck(EvaluationMove(H7, B6)))
        # Rank advance (asserts false)
        self.assertFalse(Utility.fileOrRankAdvanceBothCheck(EvaluationMove(A1, A2)))
        self.assertFalse(Utility.fileOrRankAdvanceBothCheck(EvaluationMove(E5, B5)))
        # Same square (asserts false)
        self.assertFalse(Utility.fileOrRankAdvanceBothCheck(EvaluationMove(B7, B7)))

    def testGetFileAndRankAdvance(self):
        self.assertTrue(Utility.getFileAndRankAdvance(EvaluationMove(A1, B1)) == (1, 0))
        self.assertTrue(Utility.getFileAndRankAdvance(EvaluationMove(E1, D1)) == (-1, 0))
        self.assertTrue(Utility.getFileAndRankAdvance(EvaluationMove(H1, C2)) == (-5, 1))
        self.assertTrue(Utility.getFileAndRankAdvance(EvaluationMove(F3, F3)) == (0, 0))
        self.assertTrue(Utility.getFileAndRankAdvance(EvaluationMove(A1, A2)) == (0, 1))
        self.assertTrue(Utility.getFileAndRankAdvance(EvaluationMove(E5, B5)) == (-3, 0))
        self.assertTrue(Utility.getFileAndRankAdvance(EvaluationMove(H7, B6)) == (-6, -1))
        self.assertTrue(Utility.getFileAndRankAdvance(EvaluationMove(B7, B7)) == (0, 0))

    def testGetFileAndRankSingleAdvance(self):
        self.assertTrue(Utility.getFileAndRankSingleAdvance((1, 0)) == (1, 0))
        self.assertTrue(Utility.getFileAndRankSingleAdvance((-1, 0)) == (-1, 0))
        self.assertTrue(Utility.getFileAndRankSingleAdvance((-5, 1)) == (-1, 1))
        self.assertTrue(Utility.getFileAndRankSingleAdvance((0, 0)) == (0, 0))
        self.assertTrue(Utility.getFileAndRankSingleAdvance((0, 1)) == (0, 1))
        self.assertTrue(Utility.getFileAndRankSingleAdvance((-3, 0)) == (-1, 0))
        self.assertTrue(Utility.getFileAndRankSingleAdvance((-6, -1)) == (-1, -1))
        self.assertTrue(Utility.getFileAndRankSingleAdvance((0, 0)) == (0, 0))

    # def testIsMoveInCorrectDirection(self):
