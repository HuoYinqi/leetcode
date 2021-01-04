# 力扣86：分割链表

# 描述
# 给你一个链表和特定值x，请你对链表进行分割，使得所有小于x的节点都出现在大于或等于x的节点之前。
# 应当保留两个分区的初始相当位置。

# 实例
# 输入 head = 1 -> 4 -> 3 -> 2 -> 5 -> 2
# 输出 1 -> 2 -> 2 -> 4 -> 3 -> 5

import unittest


class ListNode:
    def __init__(self, x) -> None:
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        big_head = ListNode(0)
        small_head = ListNode(0)

        big = big_head
        small = small_head
        temp = head

        while temp:
            if temp.val < x:
                small.next = ListNode(temp.val)
                small = small.next
            else:
                big.next = ListNode(temp.val)
                big = big.next
            temp = temp.next

        small.next = big_head.next
        return small_head.next


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_partition(self):
        test_node = ListNode(0)
        head_node = test_node
        data = [1, 4, 3, 2, 5, 2]
        for each in data:
            test_node.next = ListNode(each)
            test_node = test_node.next
        ans = self.solution.partition(head_node.next, 5)

        exception = [1, 4, 3, 2, 2, 5]
        for each in exception:
            self.assertEqual(ans.val, each)
            ans = ans.next if ans else None


if __name__ == "__main__":
    unittest.main()
