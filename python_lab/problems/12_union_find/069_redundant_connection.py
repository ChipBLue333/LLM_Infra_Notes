"""
Problem 069: Redundant Connection

Difficulty:
Medium

Topic:
Union Find / Graph

Description:
给定一个无向图的边列表 edges。

这个图原本是一棵包含 n 个节点的树，节点编号为 1 到 n。
后来额外添加了一条边，导致图中出现了一个环。

请找出这条多余的边，并返回它。

如果有多条边都可以删除，使图重新变成一棵树，请返回在输入中最后出现的那条边。

Input:
edges: List[List[int]] - 无向边列表，其中 edges[i] = [a, b]

Output:
List[int] - 多余的那条边

Examples:
Example 1:
Input:
edges = [[1, 2], [1, 3], [2, 3]]
Output:
[2, 3]
Explanation:
边 [2, 3] 连接了两个已经连通的节点，因此它造成了环。

Example 2:
Input:
edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
Output:
[1, 4]
Explanation:
加入 [1, 4] 时，节点 1 和节点 4 已经通过 1-2-3-4 连通，因此这条边是多余的。

Example 3:
Input:
edges = [[1, 2], [2, 3], [3, 1]]
Output:
[3, 1]
Explanation:
最后一条边让 1、2、3 形成了环。

Constraints:
- 3 <= len(edges) <= 1000
- edges[i].length == 2
- 1 <= edges[i][0], edges[i][1] <= len(edges)
- edges 中没有重复边
- 输入保证图中恰好有一条多余边

Task:
实现 find_redundant_connection(edges) 函数。

要求：
1. 使用 Union Find / Disjoint Set Union。
2. 不要使用 DFS 或 BFS 完成这题。
3. 按输入顺序遍历每条边。
4. 如果某条边连接的两个节点已经属于同一个集合，那么这条边就是答案。

提示：
- 这题和上一题 Graph Valid Tree 很像。
- 上一题发现环时直接返回 False。
- 这题发现环时，需要返回造成环的那条边。
- 注意节点编号从 1 开始，不是从 0 开始。
"""

from typing import List


def find_redundant_connection(edges: List[List[int]]) -> List[int]:
    # 判断两个事情
    # 1. 这条边连接的两个节点是否已经在同一个集合中
    # 2. 如果不在同一个集合中，就把它们合并到一起
    parent = list(range(len(edges) + 1))  # 初始化父节点数组


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
            return [a, b]

    return []


def run_tests():
    assert find_redundant_connection([[1, 2], [1, 3], [2, 3]]) == [2, 3]
    assert find_redundant_connection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4]
    assert find_redundant_connection([[1, 2], [2, 3], [3, 1]]) == [3, 1]
    assert find_redundant_connection([[1, 4], [3, 4], [1, 3], [1, 2], [4, 5]]) == [1, 3]
    assert find_redundant_connection([[1, 5], [3, 4], [3, 5], [4, 5], [2, 4]]) == [4, 5]

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
