"""
Problem 035: Unique Paths

Difficulty:
Medium

Topic:
Dynamic Programming / Matrix

Description:
一个机器人位于一个 m x n 网格的左上角。

机器人每次只能向下或者向右移动一步。
机器人想要到达网格的右下角。

请返回从左上角到右下角一共有多少条不同的路径。

Input:
m: int - 网格的行数
n: int - 网格的列数

Output:
int - 不同路径的数量

Examples:
Example 1:
Input:
m = 3, n = 7
Output:
28
Explanation:
从左上角到右下角一共有 28 条不同路径。

Example 2:
Input:
m = 3, n = 2
Output:
3
Explanation:
可能的路径包括：
1. 右 -> 下 -> 下
2. 下 -> 右 -> 下
3. 下 -> 下 -> 右

Example 3:
Input:
m = 1, n = 5
Output:
1
Explanation:
只有一行时，机器人只能一直向右走，所以只有 1 条路径。

Constraints:
- 1 <= m <= 100
- 1 <= n <= 100
- 答案保证小于等于 2 * 10^9

Task:
实现 unique_paths(m, n) 函数。

要求：
1. 使用动态规划。
2. 不要用递归暴力枚举所有路径。
3. 可以使用二维 dp 数组。
4. 注意第一行和第一列的初始化。

思考：
- `dp[i][j]` 应该表示什么？
- 到达格子 `(i, j)` 之前，机器人只能从哪两个方向过来？
- 为什么第一行所有格子的路径数都是 1？
- 为什么第一列所有格子的路径数也是 1？
"""


def unique_paths(m: int, n: int) -> int:
    # TODO: implement here
    # dp[i][j] 表示到达格子 (i, j) 的路径数
    # 到达 (i, j) 只能从 (i-1, j) 向下走或者从 (i, j-1) 向右走过来
    # 定义 dp 数组
    dp = [[0] * n for _ in range(m)]

    # 初始化第一行和第一列
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1

    # 填充 dp 数组
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]  # 当前位置路径数 = 上方路径数 + 左方路径数

    return dp[m-1][n-1] # 最终答案在右下角


def run_tests():
    assert unique_paths(3, 7) == 28
    assert unique_paths(3, 2) == 3
    assert unique_paths(1, 5) == 1
    assert unique_paths(5, 1) == 1
    assert unique_paths(1, 1) == 1
    assert unique_paths(2, 2) == 2
    assert unique_paths(3, 3) == 6
    assert unique_paths(4, 4) == 20
    assert unique_paths(10, 10) == 48620

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
