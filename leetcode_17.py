"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
示例：
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

# 采用递归回溯法
class Solution:
    def letter_combinations(self, digits):
        if not digits:
            return []

        dict_ = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }
        temp = []
        for i in digits:
            if int(i) in dict_:
                temp.append(dict_[int(i)])

        ret = []

        def dfs(s, temp):
            if not temp:
                ret.append(s)
                return
            for i in temp[0]:
                dfs(s + i, temp[1:])

        dfs("", temp)
        return ret


test = Solution()
ans = test.letter_combinations("25")
print(ans)
