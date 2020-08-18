import unittest
from GetCount import* 

class Test_Remotetest(unittest.TestCase):
    def test_A(self):
        self.assertEquals(count_remotePress('code'),14)

    def test_B(self):
        self.assertEquals(count_remotePress('tech'),16)

if __name__ == '__main__':
    unittest.main()
