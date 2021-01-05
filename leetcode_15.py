"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。
示例：
给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[[-1, 0, 1], [-1, -1, 2]]
"""


class Solution:
    def three_sum(self, nums):
        size = len(nums)
        if size < 3:
            return []

        nums.sort()
        ret = []
        for i in range(size):
            if nums[i] > 0:
                return ret

            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            left_id = i + 1
            right_id = size - 1
            target = -nums[i]
            while left_id < right_id:
                if nums[left_id] + nums[right_id] == target:
                    ret.append([nums[i], nums[left_id], nums[right_id]])
                    while left_id < right_id and nums[left_id] == nums[left_id + 1]:
                        left_id += 1
                    while left_id < right_id and nums[right_id] == nums[right_id - 1]:
                        right_id -= 1
                if nums[left_id] + nums[right_id] < target:
                    left_id += 1
                else:
                    right_id -= 1
        return ret


if __name__ == "__main__":
    test = Solution()
    ans = test.three_sum([-1, -1, 2, 0, 1])
    print(ans)
