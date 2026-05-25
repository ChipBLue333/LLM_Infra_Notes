"""
Problem 038: Triangle

Difficulty:
Medium

Topic:
Dynamic Programming / Array

Description:
给定一个三角形数组 `triangle`。

从顶部出发，每一步只能移动到下一行中相邻的数字。

如果当前位于第 `i` 行第 `j` 个数字，那么下一步只能移动到：
- 第 `i + 1` 行第 `j` 个数字；
- 第 `i + 1` 行第 `j + 1` 个数字。

请返回从顶部到底部的最小路径和。

Input:
triangle: list[list[int]] - 一个三角形数组

Output:
int - 从顶部到底部的最小路径和

Examples:
Example 1:
Input:
triangle = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3],
]
Output:
11
Explanation:
最小路径是 2 -> 3 -> 5 -> 1，路径和为 11。

Example 2:
Input:
triangle = [[-10]]
Output:
-10

Constraints:
- 1 <= len(triangle) <= 200
- len(triangle[i]) == i + 1
- -10^4 <= triangle[i][j] <= 10^4

Task:
实现 minimum_total(triangle) 函数。

要求：
1. 使用动态规划。
2. 不要用递归暴力枚举所有路径。
3. 可以使用二维 dp 数组。
4. 不要修改输入 triangle。
5. 注意每一行的第一个元素和最后一个元素，它们能从哪里来。

思考：
- `dp[i][j]` 应该表示什么？
- 第 `i` 行第 `j` 个位置，可能从上一行哪些位置走过来？
- 如果 `j == 0`，它只有哪个来源？
- 如果 `j == len(triangle[i]) - 1`，它只有哪个来源？
- 最终答案是在最后一个格子吗，还是在最后一行的最小值？
"""

from typing import List


def minimum_total(triangle: List[List[int]]) -> int:
    # TODO: implement here
    # 定义dp数组 表示到达(i, j)位置的最小路径和
    m = len(triangle)
    # 创建三角形数组
    dp = [[0] * (i + 1) for i in range(m)]
    # 初始化dp数组 第一行只有一个元素，直接等于三角形的第一个元素
    dp[0][0] = triangle[0][0]
    # 填充dp数组
    for i in range(1, m): # 从第一行遍历到最后一行
        for j in range(i + 1):
            if j == 0:
                dp[i][j] = dp[i - 1][j] + triangle[i][j] # 第一列只能从上一行的第一列来
            elif j == i:
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j] # 最后一列只能从上一行的最后一列来
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j] # 中间位置可以从上一行的两个位置来，取较小的路径和
    # 最终答案是在最后一行的最小值
    return min(dp[m - 1])



def run_tests():
    assert minimum_total([
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3],
    ]) == 11

    assert minimum_total([[-10]]) == -10

    assert minimum_total([
        [1],
        [2, 3],
    ]) == 3

    assert minimum_total([
        [5],
        [9, 6],
        [4, 6, 8],
        [0, 7, 1, 5],
    ]) == 18

    assert minimum_total([
        [-1],
        [2, 3],
        [1, -1, -3],
    ]) == -1

    assert minimum_total([
        [0],
        [0, 0],
        [0, 0, 0],
        [0, 0, 0, 0],
    ]) == 0

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
