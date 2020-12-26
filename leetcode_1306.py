# 力扣1306：跳跃游戏III

# 描述：
# 这里有一个非负整数数组arr，你最开始位于该数组的起始下标start处。当你位于下标i处时，你可以跳到
# i + arr[i]或者i - arr[i]。
# 请判断自己是否能够跳到对应元素值为0的任一下标处


# 思路 广度搜索优先 -> 占用内存空间相比深度优先搜索更少

from typing import List
import collections


class Solution:
    def can_reach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True

        used = {start}  # 用集合来存放跳过的索引值
        pre_process = collections.deque([start])
        while len(pre_process) > 0:
            cur_pos = pre_process.popleft()
            step = arr[cur_pos]
            for pos in [cur_pos + step, cur_pos - step]:
                if 0 <= pos < len(arr) and pos not in used:
                    if arr[pos] == 0:
                        return True
                    used.add(pos)
                    pre_process.append(pos)
        return False


# test
if __name__ == "__main__":
    test_data = [4, 2, 3, 0, 3, 1, 2]
    start = 5
    ans = Solution().can_reach(test_data, start)
    print(ans)
