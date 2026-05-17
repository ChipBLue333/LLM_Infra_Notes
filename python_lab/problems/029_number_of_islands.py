"""
Problem 029: Number of Islands

Difficulty:
Medium

Topic:
DFS / BFS / Matrix / Connected Components

Description:
给定一个由字符组成的二维网格 grid，其中：
- "1" 表示陆地；
- "0" 表示水域。

一个岛屿由上下左右相邻的陆地连接而成。你需要返回网格中岛屿的数量。

注意：
- 只考虑水平和垂直方向相邻；
- 对角线相邻不算连接；
- 你可以修改输入的 grid，也可以使用额外的 visited 结构。

Input:
grid: List[List[str]] - 一个 m x n 的二维字符网格

Output:
int - 岛屿数量

Examples:
Example 1:
Input:
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
Output:
1

Example 2:
Input:
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
Output:
3

Constraints:
- 1 <= len(grid) <= 300
- 1 <= len(grid[0]) <= 300
- grid[i][j] 只会是 "0" 或 "1"
- 只统计上下左右连通的陆地块

Task:
实现 num_islands(grid) 函数。

要求：
1. 使用 DFS 或 BFS。
2. 外层遍历每一个格子。
3. 每当遇到一个尚未访问的陆地，就说明发现了一个新岛屿。
4. 从这个格子出发，把同一个岛屿上的所有陆地都标记为已访问。
5. 不要使用第三方库。

思考：
- 这题和 Word Search 的 DFS 状态有什么不同？
- 为什么每次从一个新陆地出发时，答案可以加 1？
- 如何避免同一片岛屿被重复统计？
- 原地把 "1" 改成 "0" 和使用 visited 集合，各有什么取舍？
"""

from typing import List


def num_islands(grid: List[List[str]]) -> int:
    # TODO: implement here
    if not grid:
        return 0
    count = 0
    rows, cols = len(grid), len(grid[0])    # 获取行数和列数

    # 将grid复制一份，以免修改原输入
    g_in = [row[:] for row in grid]

    def dfs(r, c):
        if 0 <= r < rows and 0 <= c < cols and g_in[r][c] == "1":
            g_in[r][c] = "0"  # 标记为已访问
            dfs(r + 1, c)   # 向下
            dfs(r - 1, c)   # 向上
            dfs(r, c + 1)   # 向右
            dfs(r, c - 1)   # 向左

    for i in range(rows):
        for j in range(cols):
            if g_in[i][j] == "1":
                count += 1
                dfs(i, j)

    return count


def run_tests():
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    assert num_islands(grid) == 1

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert num_islands(grid) == 3

    assert num_islands([["0"]]) == 0
    assert num_islands([["1"]]) == 1

    grid = [
        ["1", "0", "1"],
        ["0", "1", "0"],
        ["1", "0", "1"],
    ]
    assert num_islands(grid) == 5

    grid = [
        ["1", "1", "1"],
        ["1", "1", "1"],
        ["1", "1", "1"],
    ]
    assert num_islands(grid) == 1

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
