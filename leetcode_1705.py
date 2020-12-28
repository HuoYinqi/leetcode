# 力扣1705：吃苹果的最大数目

import heapq
from typing import List


class Solution:
    def eaten_apples(self, apples: List[int], days: List[int]) -> int:
        count = 0
        heap = []
        i = 0
        n = len(apples)
        while heap or i < n:
            if i < n and apples[i] != 0:
                heapq.heappush(heap, [i + days[i], apples[i]])

            while heap and (heap[0][0] <= i or heap[0][1] < 0):
                heapq.heappop(heap)

            if heap:
                count += 1
                heap[0][1] -= 1
            i += 1

        return count


# test
if __name__ == "__main__":
    test_apples = [1, 2, 3, 5, 2]
    test_days = [3, 2, 1, 4, 2]
    ans = Solution().eaten_apples(test_apples, test_days)
    print(ans)