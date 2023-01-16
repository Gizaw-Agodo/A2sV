import unittest
from typing import List


def kthLargestNumber(nums: List[str], k: int) -> str:
    nums = [int(num) for num in nums]
    nums.sort()
    return str(nums[-k])


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums, k = ["3", "6", "7", "10"], 4
        expected = "3"
        actual = kthLargestNumber(nums, k)
        self.assertEqual(expected, actual)

    def test_2(self):
        nums, k = ["0", "0"], 2
        expected = "0"
        actual = kthLargestNumber(nums, k)
        self.assertEqual(expected, actual)

    def test_3(self):
        nums, k = ["2", "21", "12", "1"], 3
        expected = "2"
        actual = kthLargestNumber(nums, k)
        self.assertEqual(expected, actual)
