"""
Problem 040: Coin Change II

Difficulty:
Medium

Topic:
Dynamic Programming / Complete Knapsack

Description:
给定一个整数数组 `coins`，其中 `coins[i]` 表示第 i 种硬币的面额。
每种硬币可以使用无限次。

再给定一个整数 `amount`，表示需要凑出的总金额。

请返回可以凑出总金额的不同组合数量。

注意：
组合不关心硬币顺序。
例如 `1 + 2 + 2` 和 `2 + 1 + 2` 属于同一种组合。

Input:
amount: int - 目标金额
coins: list[int] - 不同面额的硬币

Output:
int - 可以凑出 amount 的不同组合数量

Examples:
Example 1:
Input:
amount = 5, coins = [1, 2, 5]
Output:
4
Explanation:
有 4 种组合：
- 5
- 2 + 2 + 1
- 2 + 1 + 1 + 1
- 1 + 1 + 1 + 1 + 1

Example 2:
Input:
amount = 3, coins = [2]
Output:
0
Explanation:
无法只用面额为 2 的硬币凑出 3。

Example 3:
Input:
amount = 10, coins = [10]
Output:
1

Constraints:
- 1 <= len(coins) <= 300
- 1 <= coins[i] <= 5000
- coins 中的面额互不相同
- 0 <= amount <= 5000

Task:
实现 change(amount, coins) 函数。

要求：
1. 使用动态规划。
2. 不要使用递归暴力枚举所有组合。
3. 每种硬币可以使用无限次。
4. 组合不关心顺序，所以 `[1, 2, 2]` 和 `[2, 1, 2]` 只能算作一种。
5. `amount == 0` 时应该返回 1，表示“不选择任何硬币”这一种组合。

思考：
- `dp[x]` 应该表示什么？
- `dp[0]` 为什么是 1，而不是 0？
- 这题是求“最少硬币数”，还是求“方案数量”？
- 如果先遍历金额、再遍历硬币，会不会把相同组合的不同顺序重复计算？
- 为了只计算组合数，应该先遍历硬币，还是先遍历金额？
"""

from typing import List


def change(amount: int, coins: List[int]) -> int:
    # TODO: implement here
    # 定义dp数组，dp[x]表示凑出金额x的组合数量
    dp = [0] * (amount + 1)
    dp[0] = 1  # 凑出金额0有一种方式：不选择任何硬币
    for coin in coins:
        for x in range(coin, amount + 1):   # 枚举金额 从coin开始 因为小于coin的金额无法使用这个硬币
            dp[x] += dp[x - coin]   # 为什么不是dp[x] = dp[x - coin]
    return dp[amount]

def run_tests():
    assert change(5, [1, 2, 5]) == 4
    assert change(3, [2]) == 0
    assert change(10, [10]) == 1
    assert change(0, [1, 2, 5]) == 1
    assert change(4, [1, 2, 3]) == 4
    assert change(7, [2, 3, 5]) == 2

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
