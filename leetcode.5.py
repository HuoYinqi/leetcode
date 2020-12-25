"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
"""
# 采用动态数组的方法求解
# dp[i][j]代表子串s[i:j+1]是否是回文子串 是个布尔值


class Solution:
    def longest_palindrome(self, s):
        size = len(s)
        if size < 2:
            return s

        ret = s[0]
        max_len = 1
        dp = [[False for _ in range(size)] for _ in range(size)]
        for j in range(1, size):
            for i in range(0, j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                    if dp[i][j] and max_len < (j - i + 1):
                        max_len = j - i + 1
                        ret = s[i : j + 1]
        return ret


if __name__ == "__main__":
    test = Solution()
    ans = test.longest_palindrome("gb")
    print(ans)
