"""
Problem 037: Minimum Path Sum

Difficulty:
Medium

Topic:
Dynamic Programming / Matrix

Description:
给定一个 m x n 的非负整数网格 `grid`。

你从左上角出发，每次只能向右或者向下移动一步，直到到达右下角。

路径和是路径经过的所有格子数字之和，包括起点和终点。

请返回从左上角到右下角的最小路径和。

Input:
grid: list[list[int]] - 一个只包含非负整数的二维网格

Output:
int - 最小路径和

Examples:
Example 1:
Input:
grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1],
]
Output:
7
Explanation:
路径 1 -> 3 -> 1 -> 1 -> 1 的和最小，结果为 7。

Example 2:
Input:
grid = [
    [1, 2, 3],
    [4, 5, 6],
]
Output:
12
Explanation:
路径 1 -> 2 -> 3 -> 6 的和最小，结果为 12。

Constraints:
- 1 <= len(grid) <= 200
- 1 <= len(grid[0]) <= 200
- 0 <= grid[i][j] <= 200

Task:
实现 min_path_sum(grid) 函数。

要求：
1. 使用动态规划。
2. 不要用递归暴力枚举所有路径。
3. 可以使用二维 dp 数组。
4. 注意第一行和第一列的初始化。
5. 不要修改输入 grid。

思考：
- `dp[i][j]` 应该表示什么？
- 到达 `(i, j)` 之前，只可能来自哪两个格子？
- 为什么这里不是把上方和左方相加？
- 第一行的格子只能从哪里来？
- 第一列的格子只能从哪里来？
"""

from typing import List


def min_path_sum(grid: List[List[int]]) -> int:
    # TODO: implement here
    # 定义dp数组 表示到达(i, j)位置的最小路径和
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    # 初始化dp数组 第一行/第一列 因为边缘处只能从一个方向来，所以只能累加
    dp[0][0] = grid[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
    # 填充dp数组
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j] # 当前格子值 + 上方/左方较小的路径和
    
    # print(dp) # 打印dp数组以便调试
    return dp[m - 1][n - 1]



def run_tests():
    assert min_path_sum([
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1],
    ]) == 7

    assert min_path_sum([
        [1, 2, 3],
        [4, 5, 6],
    ]) == 12

    assert min_path_sum([[5]]) == 5

    assert min_path_sum([
        [1, 2, 3],
    ]) == 6

    assert min_path_sum([
        [1],
        [2],
        [3],
    ]) == 6

    assert min_path_sum([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]) == 0

    assert min_path_sum([
        [9, 1, 4, 8],
        [6, 2, 1, 7],
        [5, 3, 2, 1],
    ]) == 16

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
