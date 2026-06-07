"""
Problem 063: Merge K Sorted Arrays

Difficulty:
Medium

Topic:
Heap / Array / K-Way Merge

Description:
给定 k 个按非递减顺序排列的整数数组，请将它们合并成一个按非递减顺序排列的数组。

你需要使用最小堆完成多路合并。不要先把所有元素放入一个数组后再整体排序。

Input:
arrays: List[List[int]] - 包含 k 个有序整数数组的二维数组

Output:
List[int] - 合并后的有序整数数组

Examples:
Example 1:
Input:
arrays = [[1, 4, 5], [1, 3, 4], [2, 6]]
Output:
[1, 1, 2, 3, 4, 4, 5, 6]

Example 2:
Input:
arrays = [[], [-2, 0, 3], [], [-1, 4]]
Output:
[-2, -1, 0, 3, 4]

Constraints:
- 0 <= len(arrays) <= 10000
- 0 <= len(arrays[i]) <= 10000
- 所有数组的元素总数不超过 100000
- -100000 <= arrays[i][j] <= 100000
- 每个数组都按非递减顺序排列

Task:
实现 merge_k_sorted_arrays(arrays) 函数。

要求：
1. 使用 heapq 实现最小堆。
2. 不要对全部元素进行整体排序。
3. 堆的大小最多保持为 k。

提示：
- 初始化时，只需要把每个非空数组的第一个元素放入堆。
- 堆中可以保存三元组：(value, array_index, element_index)。
- 每次从堆中取出最小元素后，只需要把同一个数组的下一个元素放入堆。
"""

from typing import List
import heapq

def merge_k_sorted_arrays(arrays: List[List[int]]) -> List[int]:
    # 将每个非空数组的第一个元素放入堆中
    min_heap = []
    for i, arr in enumerate(arrays):
        if arr:  # 只处理非空数组
            heapq.heappush(min_heap, (arr[0], i, 0))  # (value, array_index, element_index)

    result = []
    while min_heap:
        value, array_index, element_index = heapq.heappop(min_heap)
        result.append(value)

        # 如果当前数组还有下一个元素，将其加入堆中
        if element_index + 1 < len(arrays[array_index]):
            next_value = arrays[array_index][element_index + 1]
            heapq.heappush(min_heap, (next_value, array_index, element_index + 1))

    return result


def run_tests():
    assert merge_k_sorted_arrays([[1, 4, 5], [1, 3, 4], [2, 6]]) == [
        1, 1, 2, 3, 4, 4, 5, 6
    ]
    assert merge_k_sorted_arrays([[], [-2, 0, 3], [], [-1, 4]]) == [
        -2, -1, 0, 3, 4
    ]
    assert merge_k_sorted_arrays([]) == []
    assert merge_k_sorted_arrays([[], [], []]) == []
    assert merge_k_sorted_arrays([[1, 2, 3]]) == [1, 2, 3]
    assert merge_k_sorted_arrays([[1, 1, 1], [1, 1], [1]]) == [
        1, 1, 1, 1, 1, 1
    ]
    assert merge_k_sorted_arrays([[-5, -2], [-4, 0], [-3, 7]]) == [
        -5, -4, -3, -2, 0, 7
    ]

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
