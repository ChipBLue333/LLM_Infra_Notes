"""
Problem 032: Min Cost Climbing Stairs

Difficulty:
Easy

Topic:
Dynamic Programming / Array

Description:
给定一个整数数组 cost，其中 cost[i] 表示踩到第 i 阶楼梯需要支付的体力值。

你可以从第 0 阶或第 1 阶开始。
每次你可以向上爬 1 阶或 2 阶。
当你越过最后一阶时，就到达楼顶。

请返回到达楼顶所需的最小体力值。

Input:
cost: List[int] - 每一阶楼梯的体力消耗

Output:
int - 到达楼顶的最小体力值

Examples:
Example 1:
Input:
cost = [10, 15, 20]
Output:
15
Explanation:
从第 1 阶开始，支付 15，然后直接爬 2 阶到楼顶。

Example 2:
Input:
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output:
6
Explanation:
选择代价较低的路径，可以用总成本 6 到达楼顶。

Constraints:
- 2 <= len(cost) <= 1000
- 0 <= cost[i] <= 999

Task:
实现 min_cost_climbing_stairs(cost) 函数。

要求：
1. 使用动态规划。
2. 不要用递归暴力枚举所有路径。
3. 可以使用 dp 数组，也可以使用两个变量压缩空间。
4. 注意：楼顶不是 cost 数组里的某一个下标，而是下标 len(cost) 对应的位置。

思考：
- `dp[i]` 应该表示到达哪里的最小成本？
- 到达第 i 阶，最后一步可能来自哪两个位置？
- 为什么楼顶可以被看作第 len(cost) 阶？
- 踩到某一阶时，cost 应该在什么时候加？
"""

from typing import List


def min_cost_climbing_stairs(cost: List[int]) -> int:
    # TODO: implement here
    # 状态 dp[i] 表示到达第 i 阶且已经支付的最小成本
    dp = [0] * (len(cost) + 1)  # dp 数组长度比 cost 多 1，因为楼顶是 len(cost) 阶
    # 初始值
    dp[0] = cost[0]
    dp[1] = cost[1]
    # 状态转移
    for i in range(2, len(cost) + 1):
        if i < len(cost):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        else:
            dp[i] = min(dp[i - 1], dp[i - 2])  # 到达楼顶不需要再加 cost
    return dp[len(cost)]





def run_tests():
    assert min_cost_climbing_stairs([10, 15, 20]) == 15
    assert min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
    assert min_cost_climbing_stairs([0, 0]) == 0
    assert min_cost_climbing_stairs([5, 10]) == 5
    assert min_cost_climbing_stairs([10, 5]) == 5
    assert min_cost_climbing_stairs([1, 2, 3, 4]) == 4

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
