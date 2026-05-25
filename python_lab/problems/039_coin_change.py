"""
Problem 039: Coin Change

Difficulty:
Medium

Topic:
Dynamic Programming / Complete Knapsack

Description:
给定一个整数数组 `coins`，其中 `coins[i]` 表示第 i 种硬币的面额。
每种硬币可以使用无限次。

再给定一个整数 `amount`，表示需要凑出的总金额。

请返回凑出总金额所需要的最少硬币数量。
如果无法凑出该金额，返回 -1。

Input:
coins: list[int] - 不同面额的硬币
amount: int - 目标金额

Output:
int - 凑出 amount 所需要的最少硬币数；如果无法凑出，返回 -1

Examples:
Example 1:
Input:
coins = [1, 2, 5], amount = 11
Output:
3
Explanation:
11 = 5 + 5 + 1，一共需要 3 枚硬币。

Example 2:
Input:
coins = [2], amount = 3
Output:
-1
Explanation:
只使用面额为 2 的硬币，无法凑出金额 3。

Example 3:
Input:
coins = [1], amount = 0
Output:
0
Explanation:
金额为 0 时，不需要任何硬币。

Constraints:
- 1 <= len(coins) <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4
- 每种硬币可以使用无限次。

Task:
实现 coin_change(coins, amount) 函数。

要求：
1. 使用动态规划。
2. 不要使用递归暴力搜索所有组合。
3. `amount == 0` 时应该返回 0。
4. 如果某个金额无法被凑出，需要用一个明确的“不可达状态”表示。
5. 最终如果 `amount` 仍然不可达，返回 -1。

思考：
- `dp[x]` 应该表示什么？
- `dp[0]` 应该初始化成什么？
- 对于金额 x，如果最后一枚硬币是 coin，那么前一个状态是什么？
- 为什么不可达状态不能随便初始化为 0？
- 硬币可以无限次使用，这对循环转移有什么影响？
"""

from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    # TODO: implement here
    # 定义dp数组，dp[x]表示凑出金额x所需的最少硬币数
    dp = [amount + 1] * (amount + 1) # 初始化为不可达状态
    dp[0] = 0

    for x in range(1, amount + 1):  # 枚举金额 最后会得到凑出amount所需的最少硬币数
        for coin in coins:  # 枚举硬币面额 看能不能凑出金额x
            if coin <= x:   # 如果当前硬币面额不大于金额x，说明可以使用这个硬币
                dp[x] = min(dp[x], dp[x - coin] + 1)   # dp[x - coin] + 1表示使用一个coin硬币后，剩余金额x - coin所需的最少硬币数（此前遍历得到的一种方法）加上这个coin硬币本身的一枚 

    if dp[amount] == amount + 1:    # 没有被更新的金额仍然是不可达状态，说明无法凑出amount
        return -1
    return dp[amount]


def run_tests():
    assert coin_change([1, 2, 5], 11) == 3
    assert coin_change([2], 3) == -1
    assert coin_change([1], 0) == 0
    assert coin_change([1], 2) == 2
    assert coin_change([2, 5, 10, 1], 27) == 4
    assert coin_change([186, 419, 83, 408], 6249) == 20

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
