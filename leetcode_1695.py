# 力扣1698：删除字数组的最大得分

# 思路：移动窗口

from typing import List


class Solution(object):
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        i = 0
        diffnum = set()
        n = len(nums)
        res = 0
        temp = 0
        for j in range(n):
            temp += nums[j]
            while nums[j] in diffnum:
                diffnum.remove(nums[i])
                temp -= nums[i]
                i += 1
            diffnum.add(nums[j])
            res = max(res, temp)
        return res


if __name__ == "__main__":
    test_data = [4, 2, 4, 5, 6]
    ans = Solution().maximumUniqueSubarray(test_data)
    print(ans)

    test_data = [5, 2, 1, 2, 5, 2, 1, 2, 5]
    ans = Solution().maximumUniqueSubarray(test_data)
    print(ans)
