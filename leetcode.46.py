'''
给定一个 没有重复 数字的序列，返回其所有可能的全排列。
示例:

输入: [1,2,3]
输出: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liweiw/
'''



import copy
class Solution:
    def permute(self, nums):
        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                temp = copy.copy(path)
                res.append(temp)
                return
            
            for i in range(size):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    dfs(nums, size, depth+1, path, used, res)
                    used[i] = False
                    path.pop()

        size = len(nums)
        if size == 0:
            return []
        
        used = [False for i in range(size)]
        res = []
        dfs(nums, size, 0, [], used, res)
        return res

if __name__ == '__main__':
    nums = [1, 2, 3]
    test = Solution()
    ans = test.permute(nums)
    print(ans)