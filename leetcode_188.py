# 力扣188：买股票的最佳时机IV

# 描述：
# 给定一个整数数组prices，它的第i个元素prices[i]是一支给定股票在第i天的价格。
# 设计一个算法来计算你能获取到的最大利润。你最多可以完成k笔交易
# 注意： 你不能同时参与多笔交易（你必须在购买前出售掉之前的股票）

# 思路： 动态规划
# 用两个二维数组buy，sell记录两个不同的状态，buy[i][j]代表第i天进行了第j次交易并且
# 手上还有股票（即处于可卖状态）获得的最大利润
# sell[i][j]代表第i天进行了j次交易并且手上没有股票（即处于可购买状态）的最大利润
# 状态转移方程：
#           buy[i][j] = max(buy[i-1][j], sell[i-1][j]-prices[i])
#           sell[i][j] = max(sell[[i-1][j], buy[i-1][j-1]]+prices[i])
# 还有就是边界问题
import sys
from typing import List


class Solution:
    def max_profit(self, k: int, prices: List[int]) -> int:
        length = len(prices)
        if length == 0:
            return 0
        # 更新最大交易次数
        k = min(k, length // 2)

        # 初始化两个状态的二维数组
        buy = [[0] * (k + 1)] * length
        sell = [[0] * (k + 1)] * length

        buy[0][0] = -prices[0]
        for i in range(1, k + 1):
            buy[0][i] = -sys.maxsize

        for i in range(1, length):
            buy[i][0] = max(buy[i - 1][0], sell[i - 1][0] - prices[i])
            for j in range(1, k + 1):
                buy[i][j] = max(buy[i - 1][j], sell[i - 1][j] - prices[i])
                sell[i][j] = max(sell[i - 1][j], buy[i - 1][j - 1] + prices[i])
        return max(sell[length - 1])


# test
if __name__ == "__main__":
    test_data = [2, 4, 1]
    k = 2
    ans = Solution().max_profit(k, test_data)
    print(ans)

    test_data = [3, 0, 7, 5, 0, 3, 1, 8, 9, 4, 7, 2, 10]
    k = 2
    ans = Solution().max_profit(k, test_data)
    print(ans)