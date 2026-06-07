"""
Problem 062: K Closest Points to Origin

Difficulty:
Medium

Topic:
Heap / Array / Math

Description:
给定一个二维平面上的点数组 points，其中 points[i] = [x, y]。
请返回距离原点 (0, 0) 最近的 k 个点。

两个点之间的欧几里得距离为：
sqrt(x^2 + y^2)

因为 sqrt 不会改变距离大小关系，所以比较距离时可以只比较：
x^2 + y^2

返回结果的顺序不重要。

Input:
points: List[List[int]] - 点数组，每个点由两个整数坐标组成
k: int - 需要返回的最近点数量

Output:
List[List[int]] - 距离原点最近的 k 个点，顺序不限

Examples:
Example 1:
Input:
points = [[1, 3], [-2, 2]]
k = 1
Output:
[[-2, 2]]
Explanation:
[1, 3] 的距离平方是 10，[-2, 2] 的距离平方是 8。

Example 2:
Input:
points = [[3, 3], [5, -1], [-2, 4]]
k = 2
Output:
[[3, 3], [-2, 4]]
Explanation:
[3, 3] 和 [-2, 4] 是距离原点最近的两个点。

Constraints:
- 1 <= len(points) <= 100000
- -10000 <= x, y <= 10000
- 1 <= k <= len(points)
- 测试数据保证答案唯一

Task:
实现 k_closest(points, k) 函数。

要求：
1. 不要直接对整个 points 排序。
2. 推荐使用大小为 k 的最大堆，维护当前距离最近的 k 个点。
3. Python 的 heapq 是最小堆，可以通过保存负距离来模拟最大堆。
4. 返回结果顺序不限。

提示：
- 堆里可以保存三元组：(-distance_squared, x, y)。
- 堆顶代表当前保留的 k 个点里“距离最远”的点。
- 当新点距离比堆顶点更近时，替换堆顶。
"""

from typing import List
import heapq


def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    # 计算距离的平方
    def distance(point):
        return point[0] ** 2 + point[1] ** 2

    # 使用最大堆来维护距离最近的 k 个点
    heap = []
    for point in points:
        dist = distance(point)
        if len(heap) < k:
            heapq.heappush(heap, (-dist, point[0], point[1]))
        elif dist < -heap[0][0]:
            heapq.heapreplace(heap, (-dist, point[0], point[1]))

    # 提取结果
    result = []
    for _, x, y in heap:
        result.append([x, y])

    return result


def normalize(points: List[List[int]]) -> List[List[int]]:
    return sorted(points)


def run_tests():
    assert normalize(k_closest([[1, 3], [-2, 2]], 1)) == normalize([[-2, 2]])
    assert normalize(k_closest([[3, 3], [5, -1], [-2, 4]], 2)) == normalize([[3, 3], [-2, 4]])
    assert normalize(k_closest([[0, 1], [1, 0], [2, 2]], 2)) == normalize([[0, 1], [1, 0]])
    assert normalize(k_closest([[1, 1]], 1)) == normalize([[1, 1]])
    assert normalize(k_closest([[-5, 4], [2, -1], [3, 3], [0, 2]], 2)) == normalize([[2, -1], [0, 2]])
    assert normalize(k_closest([[10, 10], [1, 2], [-2, -2], [3, 0]], 3)) == normalize([[1, 2], [-2, -2], [3, 0]])

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
