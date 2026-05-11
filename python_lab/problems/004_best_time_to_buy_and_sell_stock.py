"""
Problem 004: Best Time to Buy and Sell Stock

Difficulty:
Easy

Topic:
Array / Dynamic Programming

Description:
给定一个数组 `prices`，其中 `prices[i]` 是一支给定股票第 i 天的价格。
你只能选择某一天买入这只股票，并选择在未来的某一个不同的日子卖出该股票，设计一个算法来计算你所能获取的最大利润。
返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0。

Input:
prices: list[int]

Output:
int

Examples:
示例 1:
输入: prices = [7, 1, 5, 3, 6, 4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6 - 1 = 5。注意利润不能是 7-1 = 6，因为卖出价格需要大于买入价格，同时不能在买入前卖出。

示例 2:
输入: prices = [7, 6, 4, 3, 1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

Constraints:
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4

Task:
Implement max_profit(prices).
"""

from typing import List


def max_profit(prices: List[int]) -> int:
    # TODO: implement here
    # 假设第i天卖出利润最高 则买入时是0到i-1天里价格最低的一天
    # 用一个变量表示迄今为止遇到过的最低买入价格    遍历一遍价格数组即可求解
    min_price = prices[0]
    max_p = 0
    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]   # 更新最低买入价格
        else:
            max_p = max(max_p, prices[i] - min_price)   # 如果不是最低买入价格就计算利润 看看是不是最大利润
    return max_p


def run_tests():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5, "Test Case 1 Failed"
    assert max_profit([7, 6, 4, 3, 1]) == 0, "Test Case 2 Failed"
    assert max_profit([2, 4, 1]) == 2, "Test Case 3 Failed"
    assert max_profit([2, 1, 2, 1, 0, 1, 2]) == 2, "Test Case 4 Failed"
    assert max_profit([1, 2]) == 1, "Test Case 5 Failed"
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
