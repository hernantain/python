import unittest
from hello_world import hello


class TestHello(unittest.TestCase):

	def testHelloWorld(self):
		self.assertEqual(hello(),'Hello, World!')



if __name__ == '__main__':
    unittest.main()
