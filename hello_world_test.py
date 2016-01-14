__author__="abhi"

import unittest
from hello_world import Greeter

class MyGreeterTest(unittest.TestCase):
	def test_default_greeting_set(self):
		greeter=Greeter()
		self.assertEqual(greeter.message,'Hello Peps!!')


if __name__=='__main__':
	unittest.main()
