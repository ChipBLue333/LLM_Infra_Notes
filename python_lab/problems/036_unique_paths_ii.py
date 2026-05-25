"""
Problem 036: Unique Paths II

Difficulty:
Medium

Topic:
Dynamic Programming / Matrix

Description:
一个机器人位于一个 m x n 网格的左上角。

机器人每次只能向下或者向右移动一步，并且想要到达网格的右下角。

现在网格中有一些障碍物。`obstacle_grid[i][j] == 1` 表示该格子有障碍，
机器人不能进入这个格子；`obstacle_grid[i][j] == 0` 表示该格子可以通过。

请返回从左上角到右下角一共有多少条不同路径。

Input:
obstacle_grid: list[list[int]] - 只包含 0 和 1 的二维网格

Output:
int - 不同路径的数量

Examples:
Example 1:
Input:
obstacle_grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0],
]
Output:
2
Explanation:
中间格子有障碍，机器人只能从障碍的上方或左方绕过去，共 2 条路径。

Example 2:
Input:
obstacle_grid = [
    [0, 1],
    [0, 0],
]
Output:
1
Explanation:
第一行第二个格子有障碍，只能先向下再向右。

Example 3:
Input:
obstacle_grid = [[1]]
Output:
0
Explanation:
起点本身有障碍，无法出发。

Constraints:
- 1 <= len(obstacle_grid) <= 100
- 1 <= len(obstacle_grid[0]) <= 100
- obstacle_grid[i][j] 只能是 0 或 1
- 结果保证小于等于 2 * 10^9

Task:
实现 unique_paths_with_obstacles(obstacle_grid) 函数。

要求：
1. 使用动态规划。
2. 不要用递归暴力枚举所有路径。
3. 可以使用二维 dp 数组。
4. 如果某个格子有障碍，该格子的路径数应该是 0。
5. 注意第一行和第一列的初始化不再一定全部是 1。

思考：
- `dp[i][j]` 应该表示什么？
- 如果起点或终点有障碍，答案是什么？
- 第一行遇到障碍后，障碍右侧的格子还能到达吗？
- 第一列遇到障碍后，障碍下方的格子还能到达吗？
- 对于普通非障碍格子，状态转移和 Problem 035 有什么相同点？
"""

from typing import List


def unique_paths_with_obstacles(obstacle_grid: List[List[int]]) -> int:
    # TODO: implement here
    # 定义dp数组
    r = len(obstacle_grid)
    c = len(obstacle_grid[0])
    dp = [[0] * c for _ in range(r)]

    # 初始化dp
    for i in range(r):
        if obstacle_grid[i][0] == 1:  # 如果第一列有障碍，后续格子都无法到达
            break
        dp[i][0] = 1
    for j in range(c):
        if obstacle_grid[0][j] == 1:  # 如果第一行有障碍，后续格子都无法到达
            break
        dp[0][j] = 1
    
    # 填充dp数组
    for i in range(1, r):
        for j in range(1, c):
            if obstacle_grid[i][j] == 1:  # 如果当前格子有障碍，路径数为0
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]  # 当前位置路径数 = 上方路径数 + 左方路径数

    return dp[r-1][c-1]   # 返回右下角的路径数


def run_tests():
    assert unique_paths_with_obstacles([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]) == 2

    assert unique_paths_with_obstacles([
        [0, 1],
        [0, 0],
    ]) == 1

    assert unique_paths_with_obstacles([[1]]) == 0
    assert unique_paths_with_obstacles([[0]]) == 1

    assert unique_paths_with_obstacles([
        [0, 0],
        [1, 1],
        [0, 0],
    ]) == 0

    assert unique_paths_with_obstacles([
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0],
    ]) == 4

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
