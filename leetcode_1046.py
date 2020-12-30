# 力扣1046：最后一块石头的重量

# 描述
# 有一堆石头，每块石头的重量都是正整数。
# 每一回合，从中选取两块最重的石头，然后将他们一起粉碎。假设石头的重量分别是x和y，
# x <= y。那么粉碎的结果可能如下
# 如果 x == y，那么两块石头都会完全粉碎
# 如果 x != y，那么重量为x的石头将会完全粉碎，而重量为y的石头新重量为y - x
# 最后，最多只会剩下一块石头，返回此石头的重量，如果没有石头剩下，那么返回0

# 思路：
# 最大堆来求解

from typing import List
import heapq


class Solution:
    def last_stone_weight(self, stones: List[int]) -> int:
        heap = [-each for each in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            first_stone = -heapq.heappop(heap)
            second_stone = -heapq.heappop(heap)

            if first_stone != second_stone:
                heapq.heappush(heap, second_stone - first_stone)
        if heap:
            return -heap[0]
        else:
            return 0


# test
if __name__ == "__main__":
    test_data = [2, 7, 4, 1, 8, 1]
    assert Solution().last_stone_weight(test_data) == 1