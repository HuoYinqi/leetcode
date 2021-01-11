# 力扣1202：交换字符串中的元素

# 描述
# 给你一个字符串 s，以及该字符串中的一些「索引对」数组 pairs，其中 pairs[i] = [a, b] 表示字符串中的两个索引（编号从 0 开始）。
# 你可以 任意多次交换 在 pairs 中任意一对索引处的字符。
# 返回在经过若干次交换后，s 可以变成的按字典序最小的字符串。

# 思路
# 并查集
import unittest
import collections


class DisjointSetUnion:
    def __init__(self, n: int):
        self.n = n
        self.uf = [-1] * n

    def find(self, x: int) -> int:
        if self.uf[x] < 0:
            return x
        self.uf[x] = self.find(self.uf[x])
        return self.uf[x]

    def union(self, x: int, y: int):
        fx, fy = self.find(x), self.find(y)
        if fx == fy and fx >= 0:
            return
        if self.uf[fx] > self.uf[fy]:
            fx, fy = fy, fx
        self.uf[fx] += self.uf[fy]
        self.uf[fy] = fx
        self.n -= 1

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def smallest_string_with_swaps(self, s, pairs) -> str:
        djs = DisjointSetUnion(len(s))
        for i, j in pairs:
            djs.union(i, j)

        mp = collections.defaultdict(list)
        for i, ch in enumerate(s):
            root = djs.find(i)
            mp[root].append(ch)

        for each in mp.values():
            each.sort(reverse=True)

        ret = []
        for i in range(len(s)):
            root = djs.find(i)
            element = mp[root].pop()
            ret.append(element)

        return "".join(ret)


class TestDisjointSetUnion(unittest.TestCase):
    def setUp(self) -> None:
        self.djs = DisjointSetUnion(10)

    def test_init(self):
        self.assertEqual(self.djs.n, 10)
        self.assertEqual(self.djs.uf, [-1] * 10)

    def test_union(self):
        self.djs.union(1, 3)
        self.assertEqual(self.djs.n, 9)
        self.assertEqual(self.djs.uf[3], 1)
        self.assertEqual(self.djs.uf[1], -2)

    def test_find(self):
        self.djs.union(1, 3)
        ans = self.djs.find(3)
        self.assertEqual(ans, 1)


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_smallest_string_with_swaps(self):
        test_data = "udyyek"
        test_pairs = [[3, 3], [3, 0], [5, 1], [3, 1], [3, 4], [3, 5]]
        ans = self.solution.smallest_string_with_swaps(test_data, test_pairs)
        exception = "deykuy"
        self.assertEqual(ans, exception)

    def test_smallest_string_with_swaps_empty_input(self):
        test_data = ""
        test_pairs = []
        ans = self.solution.smallest_string_with_swaps(test_data, test_pairs)
        exception = ""
        self.assertEqual(ans, exception)

    def test_smallest_string_with_swaps_single_char(self):
        test_data = "z"
        test_pairs = []
        ans = self.solution.smallest_string_with_swaps(test_data, test_pairs)
        exception = "z"
        self.assertEqual(ans, exception)


if __name__ == "__main__":
    unittest.main()
