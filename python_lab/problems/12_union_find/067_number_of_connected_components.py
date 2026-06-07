"""
Problem 067: Number of Connected Components

Difficulty:
Medium

Topic:
Union Find / Graph

Description:
给定一个包含 n 个节点的无向图，节点编号为 0 到 n - 1。

你会得到一个边列表 edges，其中 edges[i] = [a, b] 表示节点 a 和节点 b 之间有一条无向边。

请返回图中连通分量的数量。

连通分量是指一组节点：组内任意两个节点都可以通过若干条边互相到达，
并且这组节点与其他组之间没有路径相连。

Input:
n: int - 节点数量
edges: List[List[int]] - 无向边列表

Output:
int - 连通分量数量

Examples:
Example 1:
Input:
n = 5
edges = [[0, 1], [1, 2], [3, 4]]
Output:
2
Explanation:
节点 0、1、2 组成一个连通分量，节点 3、4 组成另一个连通分量。

Example 2:
Input:
n = 5
edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
Output:
1
Explanation:
所有节点都连在一起，所以只有 1 个连通分量。

Example 3:
Input:
n = 4
edges = []
Output:
4
Explanation:
没有任何边时，每个节点都是一个独立的连通分量。

Constraints:
- 1 <= n <= 20000
- 0 <= len(edges) <= 50000
- edges[i].length == 2
- 0 <= edges[i][0], edges[i][1] < n
- 输入可能包含重复边
- 输入可能包含自环，例如 [2, 2]

Task:
实现 count_components(n, edges) 函数。

要求：
1. 使用 Union Find / Disjoint Set Union。
2. 不要使用 DFS 或 BFS 完成这题。
3. 实现 find 函数，用于找到一个节点所属集合的根节点。
4. 实现 union 函数，用于合并两个集合。
5. 每次成功合并两个原本不同的集合时，连通分量数量减少 1。

提示：
- 初始时，每个节点都是自己的根节点，所以一共有 n 个连通分量。
- 如果两个节点的根节点不同，说明它们原本属于两个不同的连通分量。
- 路径压缩可以让 find 更快。
- 重复边和自环不应该让连通分量数量继续减少。
"""

from typing import List


def count_components(n: int, edges: List[List[int]]) -> int:
    # 初始化 parent 数组，每个节点的父节点初始为自己
    parent = list(range(n))
    count = n  # 初始连通分量数量为 n
    # 实现find和union函数
    def find(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]  # 路径压缩
            x = parent[x]
        return x
    

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_x] = root_y  # 合并集合
            return True
        return False
    
    # 处理每条边
    for a, b in edges:
        if union(a, b):
            count -= 1  # 成功合并两个不同的集合，连通分量数量减少 1


    return count


def run_tests():
    assert count_components(5, [[0, 1], [1, 2], [3, 4]]) == 2
    assert count_components(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1
    assert count_components(4, []) == 4
    assert count_components(1, []) == 1
    assert count_components(6, [[0, 1], [2, 3], [4, 5]]) == 3
    assert count_components(5, [[0, 1], [1, 2], [0, 2], [3, 4]]) == 2
    assert count_components(3, [[0, 0], [1, 1], [0, 1]]) == 2
    assert count_components(6, [[0, 1], [1, 2], [3, 4], [2, 3]]) == 2

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
