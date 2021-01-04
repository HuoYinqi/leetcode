# 力扣239：滑动窗口的最大值

# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
# 你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
# 返回滑动窗口中的最大值。

# 思路：
# （1） 单调队列
# （2） 优先堆

from typing import List
import unittest
import collections


class Solution:
    def max_sliding_window(self, nums: List[int], k: int):
        length = len(nums)
        d = collections.deque()

        for i in range(k):
            while d and nums[i] >= nums[d[-1]]:
                d.pop()
            d.append(i)
        ret = [nums[d[0]]]
        for i in range(k, length):
            while d and nums[i] >= nums[d[-1]]:
                d.pop()
            d.append(i)
            while d[0] <= i - k:
                d.popleft()
            ret.append(nums[d[0]])

        return ret


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_max_sliding_window(self):
        test_data = [1, 3, -1, -3, 5, 3, 6, 7]
        ans = self.solution.max_sliding_window(test_data, 3)
        exception = [3, 3, 5, 5, 6, 7]
        self.assertEqual(ans, exception)

    def test_max_sliding_window_different_n(self):
        test_data = [1, 3, -1, -3, 5, 3, 6, 7]
        ans = self.solution.max_sliding_window(test_data, 4)
        exception = [3, 5, 5, 6, 7]
        self.assertEqual(ans, exception)


if __name__ == "__main__":
    unittest.main()
