"""
Problem 064: Kth Smallest Element in a Sorted Matrix

Difficulty:
Medium

Topic:
Heap / Matrix / K-Way Merge

Description:
给定一个 n x n 的整数矩阵 matrix。
矩阵的每一行和每一列都按非递减顺序排列。

请返回矩阵中第 k 小的元素。

第 k 小按照元素在矩阵中出现的次数计算，而不是按照不同元素计算。
例如，在 [1, 2, 2, 3] 中，第 3 小的元素是 2。

Input:
matrix: List[List[int]] - 每行、每列都有序的正方形矩阵
k: int - 要查找的顺序位置

Output:
int - 矩阵中的第 k 小元素

Examples:
Example 1:
Input:
matrix = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15],
]
k = 8
Output:
13

Example 2:
Input:
matrix = [
    [1, 2],
    [1, 3],
]
k = 2
Output:
1

Constraints:
- 1 <= len(matrix) <= 300
- len(matrix[i]) == len(matrix)
- -1000000000 <= matrix[i][j] <= 1000000000
- matrix 的每一行和每一列都按非递减顺序排列
- 1 <= k <= len(matrix) * len(matrix)

Task:
实现 kth_smallest(matrix, k) 函数。

要求：
1. 使用 heapq 实现最小堆。
2. 不要展开矩阵后整体排序。
3. 使用多路合并思路，将每一行看作一条有序序列。
4. 找到第 k 小元素后立即停止，不需要合并整个矩阵。

提示：
- 初始化时，将每一行的第一个元素加入堆。
- 堆中可以保存三元组：(value, row_index, column_index)。
- 每次弹出一个元素后，只推进它所属的那一行。
- 思考需要从堆中弹出多少次，最后一次弹出的值就是答案。
"""

from typing import List
import heapq


def kth_smallest(matrix: List[List[int]], k: int) -> int:
    # 将每行第一列的元素加入最小堆
    min_heap = []
    for i in range(min(k, len(matrix))):  # 只需要加入前 k 行的第一个元素
        heapq.heappush(min_heap, (matrix[i][0], i, 0))  # (value, row_index, column_index)

    # 弹出前 k-1 个元素
    for _ in range(k - 1):
        value, row_index, column_index = heapq.heappop(min_heap)
        # 如果当前行右侧还有下一个元素，将其加入堆中
        if column_index + 1 < len(matrix[row_index]):
            next_value = matrix[row_index][column_index + 1]
            heapq.heappush(min_heap, (next_value, row_index, column_index + 1))

    # 第 k 个元素就是堆顶
    return heapq.heappop(min_heap)[0]


def run_tests():
    assert kth_smallest(
        [
            [1, 5, 9],
            [10, 11, 13],
            [12, 13, 15],
        ],
        8,
    ) == 13
    assert kth_smallest([[1, 2], [1, 3]], 2) == 1
    assert kth_smallest([[-5]], 1) == -5
    assert kth_smallest([[1, 2], [3, 4]], 1) == 1
    assert kth_smallest([[1, 2], [3, 4]], 4) == 4
    assert kth_smallest([[1, 1, 3], [1, 2, 4], [2, 2, 5]], 6) == 2
    assert kth_smallest([[-10, -5, 0], [-9, -4, 3], [-8, 1, 7]], 5) == -4

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
