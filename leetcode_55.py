# 力扣55：跳跃游戏

# 描述
# 给定一个非父整数数组，你是最初位于数组的第一个位置。
# 数组中的每个元素代表你在该位置可以跳跃的最大程度
# 判断你是否能够到达最后一个位置

# 思路
# (1) 先找出所有0的位置，只要能够跨过所有0即可以到达最后一个位置
# (2) 找到能达到的最大位置，然后不断更新最大位置，最后判断最大位置能否大于该数组的长度

from typing import List


class Solution:
    def can_jump(self, nums: List[int]) -> bool:
        # 如果该数组长度为1，返回True
        if len(nums) == 1:
            return True

        # 如果第一个数为0，返回False
        if nums[0] == 0:
            return False

        # 存放数组中为0的索引值
        value0_ids = [i for i, num in enumerate(nums) if num == 0]
        arr = [i + nums[i] for i in range(len(nums))]
        max_value = 0
        if len(value0_ids) == 0:
            return True

        for i in range(len(arr)):
            if i == 0:
                max_value = max(nums[: arr[i]])
            else:
                max_value = max(max_value, max(nums[arr[i - 1] : arr[i]]))
            if max_value <= arr[i] and max_value < len(nums) - 1:
                return False
        return True

    def can_jump_else(self, nums: List[int]) -> bool:
        max_value = 0
        for i, num in enumerate(nums):
            if i > max_value:
                return False
            max_value = max(max_value, i + num)
        return True


# test
if __name__ == "__main__":
    test_data = [1, 0, 1, 0]
    ans = Solution().can_jump(test_data)
    print(ans)
    ans = Solution().can_jump_else(test_data)
    print(ans)
