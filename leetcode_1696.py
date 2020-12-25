# 力扣1696：跳跃游戏VI

# 思路：动态分配，最小堆

from typing import List
import heapq


class Solution(object):
    def maxResult(self, nums: List, k: int) -> int:
        length = len(nums)

        # 初始化动态数组dp, 堆
        dp = [nums[0]] + [None] * (length - 1)
        heap = []
        heapq.heappush(heap, (-nums[0], 0))

        for i in range(1, length):
            if heap:
                while i - heap[0][1] > k:
                    heapq.heappop(heap)
                dp[i] = -heap[0][0] + nums[i]
                heapq.heappush(heap, (-dp[i], i))
        return dp[-1]


# test
if __name__ == "__main__":
    test_data = [1, -1, -2, 4, -7, 3]
    step = 2
    ans = Solution().maxResult(test_data, step)
    print(ans)

    test_data = [10, -5, -2, 4, 0, 3]
    step = 3
    ans = Solution().maxResult(test_data, step)
    print(ans)
