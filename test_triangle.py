# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(3, 4, 7), 'Scalene', '3,4,7 is a scalene triangle')

    def testIsoscelesTriangle(self):
        self.assertEqual(classifyTriangle(2, 2, 4), 'Isosceles', '2,2,4 is an isosceles triangle')

    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(3, 8, 6), 'NotATriangle', '3,8,6 is not a triangle')

    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(201, 8, 6), 'InvalidInput', '201,8,6 is an invalid input')

    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle(-2, 3, 4), 'InvalidInput', '-2,3,4 is an invalid input')
        
        
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
