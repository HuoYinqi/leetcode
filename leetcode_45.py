# 力扣45：跳跃游戏II

# 描述：
# 给定一个非负整数数组，你最初位于数组的第一个位置
# 数组中的每个元素代表你在该位置可以跳跃的最大长度
# 你的目标是使用最少的跳跃此书到达数组的最后一个位置

# 思路：在数组的每个位置i，都有跳到的最大位置 i + nums[i]

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        # 该数组保存每个位置能跳到的最大索引处
        jump_max_index = [i + nums[i] for i in range(length)]
        count = 0

        if length == 1:
            return count

        def jump(left, right, count):
            count += 1
            max_id = max(jump_max_index[left : right + 1])
            if max_id >= length - 1:
                return count
            return jump(right, max_id, count)

        count = jump(0, 0, 0)
        return count


# test
if __name__ == "__main__":
    test_data = [2, 3, 1, 1, 4]
    ans = Solution().jump(test_data)
    print(ans)

    test_data = [1, 2]
    ans = Solution().jump(test_data)
    print(ans)