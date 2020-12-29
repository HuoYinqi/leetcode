# 力扣330：按要求补齐数组

# 描述
# 给定一个已排序的正整数数组nums，和一个正整数n。从[1, n]区间内选取任意个数字补充
# 到nums中，使得[1, n]区间内的数字都可以用nums中某几个数字的和来表示。请输出满足
# 上诉要求的最少需要补充的数字个数

from typing import List


class Solution:
    def min_patches(self, nums: List[int], n: int) -> int:
        length = len(nums)
        i = 0
        x = 1
        pathches = 0

        while x <= n:
            if i < length and nums[i] <= x:
                x += nums[i]
                i += 1
            else:
                x <<= 1
                pathches += 1

        return pathches


# test
if __name__ == "__main__":
    test_data, n = [1, 3], 6
    ans = Solution().min_patches(test_data, n)
    assert ans == 1

    test_data, n = [1, 5, 10], 6
    ans = Solution().min_patches(test_data, n)
    assert ans == 2
