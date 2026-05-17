"""
Problem 030: Rotting Oranges

Difficulty:
Medium

Topic:
BFS / Queue / Matrix / Multi-source BFS

Description:
给定一个 m x n 的二维网格 grid，每个格子可能有三种值：
- 0 表示空格子；
- 1 表示新鲜橘子；
- 2 表示腐烂橘子。

每经过 1 分钟，任意一个腐烂橘子都会使它上下左右相邻的新鲜橘子腐烂。
请返回直到没有新鲜橘子为止所需的最少分钟数。
如果永远不可能使所有新鲜橘子腐烂，返回 -1。

Input:
grid: List[List[int]] - 一个 m x n 的二维整数网格

Output:
int - 腐烂所有新鲜橘子所需的最少分钟数；如果无法全部腐烂，返回 -1

Examples:
Example 1:
Input:
grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1],
]
Output:
4

Example 2:
Input:
grid = [
    [2, 1, 1],
    [0, 1, 1],
    [1, 0, 1],
]
Output:
-1

Example 3:
Input:
grid = [[0, 2]]
Output:
0

Constraints:
- 1 <= len(grid) <= 10
- 1 <= len(grid[0]) <= 10
- grid[i][j] 只会是 0、1 或 2

Task:
实现 oranges_rotting(grid) 函数。

要求：
1. 使用 BFS。
2. 一开始要把所有腐烂橘子同时加入队列。
3. 需要统计新鲜橘子的数量。
4. 每一轮 BFS 表示 1 分钟的扩散。
5. 不要使用递归 DFS 来模拟分钟扩散。

思考：
- 为什么这题不是从一个起点 BFS，而是从多个起点同时 BFS？
- 如何保证第一次腐烂某个橘子时，对应时间就是最短时间？
- 分钟数应该在每处理一个节点时增加，还是在每处理一层时增加？
- 什么情况下应该返回 0？
- 什么情况下应该返回 -1？
"""

from collections import deque
from typing import List


def oranges_rotting(grid: List[List[int]]) -> int:
    # TODO: implement here
    # 所有初始腐烂橘子的位置
    rotten = deque()
    fresh_count = 0
    minutes = 0

    # 保存行数和列数
    rows = len(grid)
    cols = len(grid[0]) 

    # 初始化队列和新鲜橘子计数
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                rotten.append((r, c))
            elif grid[r][c] == 1:
                fresh_count += 1

    # 如果没有新鲜橘子，直接返回 0
    if fresh_count == 0:
        return 0

    # 四个方向的偏移量
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # 当队列非空且还有新鲜橘子时，继续 BFS
    while rotten and fresh_count > 0:   # 如果rotten为空，说明没有更多腐烂橘子可以扩散了；如果fresh_count为0，说明所有新鲜橘子已经腐烂了
        # 处理当前层的所有腐烂橘子
        for _ in range(len(rotten)):
            x, y = rotten.popleft() # 当前腐烂橘子的位置
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:    # 如果相邻位置是新鲜橘子
                    grid[nx][ny] = 2
                    fresh_count -= 1
                    rotten.append((nx, ny))
        minutes += 1

    # 如果还有新鲜橘子，说明无法全部腐烂
    if fresh_count > 0:
        return -1

    return minutes


def run_tests():
    grid = [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1],
    ]
    assert oranges_rotting(grid) == 4

    grid = [
        [2, 1, 1],
        [0, 1, 1],
        [1, 0, 1],
    ]
    assert oranges_rotting(grid) == -1

    assert oranges_rotting([[0, 2]]) == 0
    assert oranges_rotting([[0]]) == 0
    assert oranges_rotting([[1]]) == -1
    assert oranges_rotting([[2]]) == 0

    grid = [
        [2, 1, 1],
        [1, 1, 1],
        [0, 1, 2],
    ]
    assert oranges_rotting(grid) == 2

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
