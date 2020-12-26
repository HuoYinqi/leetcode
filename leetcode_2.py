# 力扣2：两数相加

# 描述：
# 给出两个非空的链表用来表示两个非负的整数。其中，它们各自的位数是按照逆序的方式存储的，
# 并且它们的每个节点只能储存一位数字
# 如果，我们将这两个数字相加起来，则会返回一个新的链表来表示它们的和。
# 你可以假设除了数字0之外，这两个数都不会以0开头


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class Solution:
    def add_two_number(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)  # 保存头节点
        node = head
        carry = 0  # 保存进位

        while l1 or l2:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            value = (num1 + num2 + carry) % 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            node.next = ListNode(value)
            carry = (num1 + num2 + carry) // 10
            node = node.next

        if carry != 0:
            node.next = ListNode(carry)
        return head.next


# test
if __name__ == "__main__":
    test_data_1 = [2, 4, 3]
    test_data_2 = [5, 6, 4]

    l1 = ListNode(0)
    l2 = ListNode(0)

    node1 = l1
    node2 = l2
    for each in test_data_1:
        node1.next = ListNode(each)
        node1 = node1.next

    for each in test_data_2:
        node2.next = ListNode(each)
        node2 = node2.next

    data = Solution().add_two_number(l1.next, l2.next)
    while data:
        print(data.val)
        data = data.next
