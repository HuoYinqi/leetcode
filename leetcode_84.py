# 力扣84：柱状图中的最大矩形
# 描述
# 给定n个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，
# 且宽度为1.求在该柱状图中，能够勾勒出来的矩形的最大面积

from typing import List
import unittest


class Solution:
    def largest_rectangle_area(self, heights: List[int]) -> int:
        if not heights:
            return 0

        length = len(heights)
        left = [None] * length
        right = [None] * length
        temp = []

        for i in range(length):
            while temp and heights[i] <= heights[temp[-1]]:
                temp.pop()

            left[i] = temp[-1] if temp else -1
            temp.append(i)

        temp = []
        for i in range(length - 1, -1, -1):
            while temp and heights[i] <= heights[temp[-1]]:
                temp.pop()

            right[i] = temp[-1] if temp else length
            temp.append(i)

        return max([(right[i] - left[i] - 1) * heights[i] for i in range(length)])


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_largest_rectangle_area(self):
        test_data = [1, 1]
        ans = self.solution.largest_rectangle_area(test_data)
        exception = 2
        self.assertEqual(ans, exception)

    def test_largest_rectangle_area_empty_input(self):
        test_data = []
        ans = self.solution.largest_rectangle_area(test_data)
        exception = 0
        self.assertEqual(ans, exception)


if __name__ == "__main__":
    unittest.main()
