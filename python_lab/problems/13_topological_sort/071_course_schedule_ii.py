"""
Problem 071: Course Schedule II

Difficulty:
Medium

Topic:
Graph / Topological Sort / BFS

Description:
你需要修 n 门课程，课程编号从 0 到 n - 1。

给定先修关系数组 prerequisites，其中 prerequisites[i] = [course, prereq]
表示如果想学习 course，必须先学习 prereq。

请返回一种可以完成所有课程的学习顺序。

如果存在环，导致无法完成所有课程，请返回空列表 []。
如果有多个合法答案，返回其中任意一个即可。

Input:
num_courses: int - 课程总数
prerequisites: List[List[int]] - 先修关系数组

Output:
List[int] - 一个合法的课程学习顺序；如果无法完成所有课程，返回 []

Examples:
Example 1:
Input:
num_courses = 2
prerequisites = [[1, 0]]
Output:
[0, 1]
Explanation:
必须先学习课程 0，才能学习课程 1。

Example 2:
Input:
num_courses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
Output:
[0, 1, 2, 3]
Explanation:
[0, 2, 1, 3] 也是合法答案。

Example 3:
Input:
num_courses = 2
prerequisites = [[1, 0], [0, 1]]
Output:
[]
Explanation:
课程 0 和课程 1 互相依赖，形成环，无法完成所有课程。

Constraints:
- 1 <= num_courses <= 2000
- 0 <= len(prerequisites) <= 5000
- prerequisites[i].length == 2
- 0 <= course, prereq < num_courses
- prerequisites 中没有重复的先修关系

Task:
实现 find_order(num_courses, prerequisites) 函数。

要求：
1. 使用拓扑排序完成这题。
2. 建立邻接表 graph，其中 prereq 指向 course。
3. 记录每门课的入度 indegree。
4. 从所有入度为 0 的课程开始。
5. 每弹出一门课，就把它加入结果数组 order。
6. 最后如果 order 的长度等于 num_courses，返回 order；否则返回 []。

提示：
- 这题和 Problem 070 很像，但这次不仅要判断 True / False，还要保存学习顺序。
- 如果返回非空结果，每门课必须只出现一次。
- 对于每一组 [course, prereq]，prereq 在结果中必须出现在 course 前面。
"""

from collections import deque
from typing import List


def find_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
    # 建立邻接表graph和入度数组indegree
    graph = {i: [] for i in range(num_courses)}
    indegree = [0] * num_courses
    # 填充graph和indegree
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1
    # 从所有入度为0的课程开始
    queue = deque([i for i in range(num_courses) if indegree[i] == 0])
    order = []
    # 不断弹出课程，更新邻居的入度
    while queue:
        course = queue.popleft()
        order.append(course)
        for neighbor in graph[course]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    # 如果order的长度等于num_courses，返回order；否则返回[]
    return order if len(order) == num_courses else []


def is_valid_order(
    order: List[int], num_courses: int, prerequisites: List[List[int]]
) -> bool:
    if len(order) != num_courses:
        return False

    if set(order) != set(range(num_courses)):
        return False

    position = {course: index for index, course in enumerate(order)}
    for course, prereq in prerequisites:
        if position[prereq] > position[course]:
            return False

    return True


def run_tests():
    order = find_order(2, [[1, 0]])
    assert is_valid_order(order, 2, [[1, 0]])

    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    order = find_order(4, prerequisites)
    assert is_valid_order(order, 4, prerequisites)

    assert find_order(2, [[1, 0], [0, 1]]) == []

    order = find_order(1, [])
    assert is_valid_order(order, 1, [])

    prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [4, 2]]
    order = find_order(5, prerequisites)
    assert is_valid_order(order, 5, prerequisites)

    assert find_order(3, [[0, 1], [1, 2], [2, 0]]) == []

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
