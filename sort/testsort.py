#!/usr/bin/env python3
import unittest
import random

from manysort import *

N = 100

class TestSort(unittest.TestCase):
    def test_sort(self):
        self._test_sort(bubble1)
        self._test_sort(selection1)
        self._test_sort(insertion1)
        self._test_sort(mergesort1)
        self._test_sort(quicksort1)
        self._test_sort(heapsort1)

    def _test_sort(self, func):
        random.seed(0)
        for _ in range(10):
            nums = random.choices(range(-N, N), k=N)
            # print(nums)
            self.assertEqual(sorted(nums), func(nums), msg=nums)
        print(str(func), "is passed")

if __name__ == "__main__":
    unittest.main()