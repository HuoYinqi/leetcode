"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
"""

# 双指针法


class Solution:
    def max_area(self, height=[]):
        if len(height) < 2:
            return 0

        head = 0
        end = len(height) - 1
        out = 0
        while head < end:
            temp = (end - head) * min(height[head], height[end])
            out = max(temp, out)
            if height[head] < height[end]:
                temp_head = height[head]
                while temp_head > height[head + 1] and head < end:
                    head += 1
                head += 1

            else:
                temp_end = height[end]
                while temp_end > height[end - 1] and head < end:
                    end -= 1
                end -= 1
        return out


test = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
ans = test.max_area(height)
print(ans)
