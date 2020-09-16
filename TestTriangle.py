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
    # define multiple sets of tests as functions with names that begin

    def testNegativeA(self):
        self.assertEqual(classifyTriangle(-1, 2, 3),
                         'InvalidInput', 'side a is a negative integer')

    def testNegativeB(self):
        self.assertEqual(classifyTriangle(1, -2, 3),
                         'InvalidInput', 'side b is a negative integer')

    def testNegativeC(self):
        self.assertEqual(classifyTriangle(1, 2, -3),
                         'InvalidInput', 'side c is a negative integer')

    def testNegative(self):
        self.assertEqual(classifyTriangle(-1, -2, -3),
                         'InvalidInput', 'All sides are negative integers')

    def testGreaterThanA(self):
        self.assertEqual(classifyTriangle(201, 190, 199),
                         'InvalidInput', 'side a is greater than 200')

    def testGreaterThanB(self):
        self.assertEqual(classifyTriangle(180, 209, 109),
                         'InvalidInput', 'side b is greater than 200')

    def testGreaterThanC(self):
        self.assertEqual(classifyTriangle(191, 180, 209),
                         'InvalidInput', 'side c is greater than 200')

    def testgreaterThan(self):
        self.assertEqual(classifyTriangle(291, 280, 209),
                         'InvalidInput', 'All sides were greater than 200')

    def testInvalidTriangleA(self):
        self.assertEqual(classifyTriangle(40, 5, 7), 'NotATriangle',
                         'side a is greater than the sum of b,c')

    def testInvalidTriangleB(self):
        self.assertEqual(classifyTriangle(40, 55, 7), 'NotATriangle',
                         'side b is greater than the sum of a,c')

    def testInvalidTriangleC(self):
        self.assertEqual(classifyTriangle(40, 5, 76), 'NotATriangle',
                         'side c is greater than the sum of a,b')

    def testTypeA(self):
        self.assertEqual(classifyTriangle('a', 1, 2),
                         'InvalidInput', 'side a should be of type integer')

    def testTypeB(self):
        self.assertEqual(classifyTriangle(1, 1.0, 2),
                         'InvalidInput', 'side b should be of type integer')

    def testTypeC(self):
        self.assertEqual(classifyTriangle(2, 1, "s"),
                         'InvalidInput', 'side c should be of type integer')

    def testType(self):
        self.assertEqual(classifyTriangle('a', '1', '2'),
                         'InvalidInput', 'side a should be of type integer')

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right',
                         '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right',
                         '5,3,4 is a Right triangle')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(3, 5, 4), 'Right',
                         '3,5,4 is a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1),
                         'Equilateral', '1,1,1 should be equilateral')

    def testIsocelesA(self):
        self.assertEqual(classifyTriangle(4, 4, 2), 'Isoceles',
                         '1,1,2 should be an Isoceles')

    def testIsocelesB(self):
        self.assertEqual(classifyTriangle(2, 4, 4), 'Isoceles',
                         '2,1,1 should be an Isoceles')

    def testIsocelesC(self):
        self.assertEqual(classifyTriangle(4, 2, 4), 'Isoceles',
                         '1,2,1 should be an Isoceles')

    def testScalene(self):
        self.assertEqual(classifyTriangle(7, 12, 15),
                         'Scalene', '7,12,15 should be Scalene')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
