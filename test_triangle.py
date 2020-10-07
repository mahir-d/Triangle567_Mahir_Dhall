# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest


from classify_triangle import classify_triangle
# import classify_triangle from triangle


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    """ This class tests the classification of triangles using the
        classify_triangle function
    """

    def test_negative(self):
        """ This function tests for negative side inputs """
        self.assertEqual(classify_triangle(-1, 2, 3),
                         'InvalidInput', 'side a is a negative integer')
        self.assertEqual(classify_triangle(1, -2, 3),
                         'InvalidInput', 'side b is a negative integer')
        self.assertEqual(classify_triangle(1, 2, -3),
                         'InvalidInput', 'side c is a negative integer')
        self.assertEqual(classify_triangle(-1, -2, -3),
                         'InvalidInput', 'All sides are negative integers')

    def test_greater_than(self):
        """ This function tests for invalid triangles when input side is greater
        than 200 """
        self.assertEqual(classify_triangle(201, 190, 199),
                         'InvalidInput', 'side a is greater than 200')
        self.assertEqual(classify_triangle(180, 209, 109),
                         'InvalidInput', 'side b is greater than 200')
        self.assertEqual(classify_triangle(191, 180, 209),
                         'InvalidInput', 'side c is greater than 200')
        self.assertEqual(classify_triangle(291, 280, 209),
                         'InvalidInput', 'All sides were greater than 200')

    def test_invalid_triangle(self):
        """ This function tests for invalid triangles when one side is greater
        than sum of the two other sides """
        self.assertEqual(classify_triangle(40, 5, 7), 'NotATriangle',
                         'side a is greater than the sum of b,c')
        self.assertEqual(classify_triangle(40, 55, 7), 'NotATriangle',
                         'side b is greater than the sum of a,c')
        self.assertEqual(classify_triangle(40, 5, 76), 'NotATriangle',
                         'side c is greater than the sum of a,b')

    def test_type(self):
        """ This function tests for input type of the sides"""
        self.assertEqual(classify_triangle('a', 1, 2),
                         'InvalidInput', 'side a should be of type integer')
        self.assertEqual(classify_triangle(1, 1.0, 2),
                         'InvalidInput', 'side b should be of type integer')
        self.assertEqual(classify_triangle(2, 1, "s"),
                         'InvalidInput', 'side c should be of type integer')
        self.assertEqual(classify_triangle('a', '1', '2'),
                         'InvalidInput', 'side a should be of type integer')

    def test_right_triangle(self):
        """ This function tests for classification of right triangles """
        self.assertEqual(classify_triangle(3, 4, 5), 'Right Scalene',
                         '3,4,5 is a Right triangle')
        self.assertEqual(classify_triangle(5, 3, 4), 'Right Scalene',
                         '5,3,4 is a Right triangle')
        self.assertEqual(classify_triangle(3, 5, 4), 'Right Scalene',
                         '3,5,4 is a Right triangle')

    def test_equilateral_triangles(self):
        """ This function tests for classification of equilateral triangles """
        self.assertEqual(classify_triangle(1, 1, 1),
                         'Equilateral', '1,1,1 should be equilateral')

    def test_isoceles(self):
        """ This function tests for classification of Isoceles triangles """
        self.assertEqual(classify_triangle(4, 4, 2), 'Isoceles',
                         '1,1,2 should be an Isoceles')
        self.assertEqual(classify_triangle(2, 4, 4), 'Isoceles',
                         '2,1,1 should be an Isoceles')
        self.assertEqual(classify_triangle(4, 2, 4), 'Isoceles',
                         '1,2,1 should be an Isoceles')

    def test_scalene(self):
        """ This function tests for classification of Scalene triangles """
        self.assertEqual(classify_triangle(7, 12, 15),
                         'Scalene', '7,12,15 should be Scalene')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
