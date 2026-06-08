"""
Problem 068: Graph Valid Tree

Difficulty:
Medium

Topic:
Union Find / Graph

Description:
给定一个包含 n 个节点的无向图，节点编号为 0 到 n - 1。

你会得到一个边列表 edges，其中 edges[i] = [a, b] 表示节点 a 和节点 b 之间有一条无向边。

请判断这个无向图是否是一棵有效的树。

一棵有效的树需要同时满足：
1. 所有节点都连通；
2. 图中没有环。

Input:
n: int - 节点数量
edges: List[List[int]] - 无向边列表

Output:
bool - 如果这个图是一棵有效的树，返回 True；否则返回 False

Examples:
Example 1:
Input:
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output:
True
Explanation:
所有节点都连通，并且没有环，所以这是一棵树。

Example 2:
Input:
n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output:
False
Explanation:
节点 1、2、3 之间形成了环，所以不是树。

Example 3:
Input:
n = 4
edges = [[0, 1], [2, 3]]
Output:
False
Explanation:
图不连通，所以不是树。

Constraints:
- 1 <= n <= 20000
- 0 <= len(edges) <= 50000
- edges[i].length == 2
- 0 <= edges[i][0], edges[i][1] < n
- 输入不包含重复边
- 输入不包含自环

Task:
实现 valid_tree(n, edges) 函数。

要求：
1. 使用 Union Find / Disjoint Set Union。
2. 不要使用 DFS 或 BFS 完成这题。
3. 如果发现某条边连接的两个节点已经属于同一个集合，说明出现了环。
4. 最终需要确认所有节点属于同一个连通分量。

提示：
- 一棵 n 个节点的树恰好有 n - 1 条边。
- 可以先利用边数快速排除一部分不可能是树的情况。
- 也可以维护连通分量数量，成功合并一次就让数量减少 1。
"""

from typing import List


def valid_tree(n: int, edges: List[List[int]]) -> bool:
    # 判断两个事情 
    # 1. 边数必须是 n - 1 （树的特性）
    # 2. 没有环（即没有重复的连接）
    if len(edges) != n - 1:
        return False

    # 初始化并查集
    parent = list(range(n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # 路径压缩
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_x] = root_y
            return True
        return False

    for a, b in edges:
        if not union(a, b):
            return False

    return True


def run_tests():
    assert valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) is True
    assert valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) is False
    assert valid_tree(4, [[0, 1], [2, 3]]) is False
    assert valid_tree(1, []) is True
    assert valid_tree(2, []) is False
    assert valid_tree(2, [[0, 1]]) is True
    assert valid_tree(4, [[0, 1], [1, 2], [2, 3]]) is True
    assert valid_tree(4, [[0, 1], [1, 2], [2, 0]]) is False
    assert valid_tree(6, [[0, 1], [0, 2], [0, 3], [4, 5]]) is False

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
