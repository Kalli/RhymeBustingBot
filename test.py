import rhyming
import unittest


class Test1(unittest.TestCase):

    def testRhyming(self):
        r = rhyming.rhyme("tool", "fool")
        self.assertEqual(r ,2)
        r = rhyming.rhyme("understand", "moaned")
        self.assertEqual(r, 0)
        r = rhyming.rhyme("magazine", "limousine")
        self.assertEqual(r, 4)

if __name__ == '__main__':
    unittest.main()