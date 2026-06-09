"""
Problem 070: Course Schedule

Difficulty:
Medium

Topic:
Graph / Topological Sort / BFS

Description:
你需要修 n 门课程，课程编号从 0 到 n - 1。

有一个先修关系数组 prerequisites，其中 prerequisites[i] = [course, prereq]
表示如果想学习 course，必须先学习 prereq。

请判断是否可以完成所有课程。

如果先修关系中存在环，那么某些课程会互相依赖，无法完成所有课程。
如果不存在环，则可以通过某种顺序完成全部课程。

Input:
num_courses: int - 课程总数
prerequisites: List[List[int]] - 先修关系数组

Output:
bool - 如果可以完成所有课程，返回 True；否则返回 False

Examples:
Example 1:
Input:
num_courses = 2
prerequisites = [[1, 0]]
Output:
True
Explanation:
先学习课程 0，再学习课程 1，可以完成所有课程。

Example 2:
Input:
num_courses = 2
prerequisites = [[1, 0], [0, 1]]
Output:
False
Explanation:
课程 0 和课程 1 互相依赖，形成环，无法完成所有课程。

Example 3:
Input:
num_courses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
Output:
True
Explanation:
一种可行顺序是 0 -> 1 -> 2 -> 3，也可以是 0 -> 2 -> 1 -> 3。

Constraints:
- 1 <= num_courses <= 2000
- 0 <= len(prerequisites) <= 5000
- prerequisites[i].length == 2
- 0 <= course, prereq < num_courses
- prerequisites 中没有重复的先修关系

Task:
实现 can_finish(num_courses, prerequisites) 函数。

要求：
1. 使用拓扑排序完成这题。
2. 建立邻接表 graph，其中 prereq 指向 course。
3. 记录每门课的入度 indegree。
4. 从所有入度为 0 的课程开始，逐步移除依赖。
5. 最后判断被学习过的课程数量是否等于 num_courses。

提示：
- 入度为 0 表示这门课当前没有未完成的先修课。
- 每学完一门课，就可以让它指向的后续课程入度减 1。
- 如果图中存在环，环上的课程入度无法全部降到 0。
"""

from collections import deque
from typing import List


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    # 使用拓扑排序
    # 建立邻接表 graph，其中 prereq 指向 course
    graph = {i: [] for i in range(num_courses)}
    # 记录每门课的入度 indegree
    indegree = {i: 0 for i in range(num_courses)}

    # 填充邻接表和入度数组
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1

    # 找到所有入度为 0 的课程
    queue = deque([i for i in range(num_courses) if indegree[i] == 0])
    learned = 0

    # 拓扑排序
    while queue:
        current = queue.popleft()
        learned += 1
        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return learned == num_courses


def run_tests():
    assert can_finish(2, [[1, 0]]) is True
    assert can_finish(2, [[1, 0], [0, 1]]) is False
    assert can_finish(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) is True
    assert can_finish(1, []) is True
    assert can_finish(3, [[1, 0], [2, 1]]) is True
    assert can_finish(3, [[0, 1], [1, 2], [2, 0]]) is False

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
