"""
Problem 031: Climbing Stairs

Difficulty:
Easy

Topic:
Dynamic Programming / Math

Description:
你正在爬一段楼梯。楼梯一共有 n 阶。

每次你可以爬 1 阶或 2 阶。
请返回爬到第 n 阶一共有多少种不同的方法。

Input:
n: int - 楼梯总阶数

Output:
int - 不同爬法的数量

Examples:
Example 1:
Input:
n = 2
Output:
2
Explanation:
有两种方法：
1. 1 阶 + 1 阶
2. 2 阶

Example 2:
Input:
n = 3
Output:
3
Explanation:
有三种方法：
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶

Constraints:
- 1 <= n <= 45

Task:
实现 climb_stairs(n) 函数。

要求：
1. 不要使用递归暴力枚举所有路径。
2. 优先使用动态规划。
3. 可以使用数组 `dp`，也可以使用两个变量压缩空间。
4. 不要直接调用斐波那契库或数学公式。

思考：
- 到达第 n 阶的最后一步可能来自哪里？
- `dp[i]` 应该表示什么？
- `dp[1]` 和 `dp[2]` 分别是多少？
- 为什么 `dp[i] = dp[i - 1] + dp[i - 2]`？
"""


def climb_stairs(n: int) -> int:
    # TODO: implement here
    # 核心状态转移 dp[i] = dp[i - 1] + dp[i - 2]

    if n == 1:
        return 1
    
    # 初始化dp数组
    dp = [0] * (n + 1)
    dp[1] = 1  # 爬到第1阶只有一种方法
    dp[2] = 2  # 爬到第2阶有两种方法
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def run_tests():
    assert climb_stairs(1) == 1
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
    assert climb_stairs(4) == 5
    assert climb_stairs(5) == 8
    assert climb_stairs(10) == 89
    assert climb_stairs(45) == 1836311903

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
