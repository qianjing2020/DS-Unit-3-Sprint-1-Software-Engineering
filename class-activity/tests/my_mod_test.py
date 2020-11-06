# test my_mod enlarge() function

import unittest
from my_lambdata.my_mod import enlarge

class TestMyMod(unittest.TestCase):

    def test_enlarge(self):
        self.assertEqual(enlarge(9), 900)


if __name__=="__main__":
    unittest.main()