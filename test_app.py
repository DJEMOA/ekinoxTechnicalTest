import unittest
from app import getOffers

# We define here our unit tests
class TestGetOffers(unittest.TestCase):
    def testBasic(self):
        # test positive value
        self.assertGreater(getOffers("abc"),0)

        #test 1 saga
        self.assertAlmostEqual(getOffers(""), "Error : Empty value inserted")

    def testOffers(self):
        #test 1 saga
        self.assertAlmostEqual(getOffers("Back to the Future 1"), 15)

        #test 2 saga
        self.assertAlmostEqual(getOffers("Back to the Future 1 \n Back to the Future 3"), 27)