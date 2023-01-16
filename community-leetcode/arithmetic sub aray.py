def checkArithmeticSubArrays(nums: List[int], l: List[int], r: List[int]) -> List[bool]:
    result = []
    for left, right in zip(l, r):
        max_num, min_num, lookup = max(nums[left:right + 1]), min(nums[left:right + 1]), set(nums[left:right + 1])
        if max_num == min_num:
            result.append(True)

        dividend, remainder = divmod(max_num - min_num, len(nums[left:right + 1]) - 1)
        if remainder:
            result.append(False)
        else:
            if dividend:
                result.append(all(i in lookup for i in range(min_num, max_num, dividend)))
    return result


class TestSolutions(unittest.TestCase):
    def test_1(self):
        nums, l, r = [-3, -6, -8, -4, -2, -8, -6, 0, 0, 0, 0], [5, 4, 3, 2, 4, 7, 6, 1, 7], [6, 5, 6, 3, 7, 10, 7, 4, 10]
        expected = [True, True, True, True, False, True, True, True, True]
        actual = checkArithmeticSubArrays(nums, l, r)
        self.assertEqual(expected, actual)
