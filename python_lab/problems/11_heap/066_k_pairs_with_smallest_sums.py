"""
Problem 066: K Pairs with Smallest Sums

Difficulty:
Medium

Topic:
Heap / Array / K-Way Merge

Description:
给定两个按非递减顺序排列的整数数组 nums1 和 nums2，以及一个整数 k。

请返回和最小的 k 个数对。
每个数对由 nums1 中的一个元素和 nums2 中的一个元素组成，格式为 [nums1[i], nums2[j]]。

如果所有可能的数对数量少于 k，则返回所有数对。

Input:
nums1: List[int] - 第一个非递减数组
nums2: List[int] - 第二个非递减数组
k: int - 需要返回的数对数量

Output:
List[List[int]] - 和最小的 k 个数对，顺序按照弹出堆的顺序即可

Examples:
Example 1:
Input:
nums1 = [1, 7, 11]
nums2 = [2, 4, 6]
k = 3
Output:
[[1, 2], [1, 4], [1, 6]]

Example 2:
Input:
nums1 = [1, 1, 2]
nums2 = [1, 2, 3]
k = 2
Output:
[[1, 1], [1, 1]]

Example 3:
Input:
nums1 = [1, 2]
nums2 = [3]
k = 3
Output:
[[1, 3], [2, 3]]

Constraints:
- 0 <= len(nums1), len(nums2) <= 10000
- -100000 <= nums1[i], nums2[j] <= 100000
- nums1 和 nums2 都按非递减顺序排列
- 1 <= k <= 10000

Task:
实现 k_smallest_pairs(nums1, nums2, k) 函数。

要求：
1. 使用 heapq。
2. 不要生成所有数对后整体排序。
3. 堆中保存当前候选数对的和以及对应下标。
4. 找到 k 个结果后立即停止。

提示：
- 固定 nums1[i] 时，随着 j 增大，nums1[i] + nums2[j] 也按非递减顺序增长。
- 可以把每个 nums1[i] 对应的一行看作一条有序序列：
  [nums1[i] + nums2[0], nums1[i] + nums2[1], ...]
- 初始化时不一定需要把所有 i 都放入堆，思考最多需要前多少行。
- 堆中可以保存三元组：(pair_sum, i, j)。
- 每次弹出 (i, j) 后，只需要尝试把同一行的 (i, j + 1) 加入堆。
"""

from typing import List
import heapq


def k_smallest_pairs(nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    # 空数组
    if not nums1 or not nums2:
        return []  
    
    results = []
    heap = []

    # 初始化堆，最多只需要前 k 行
    for i in range(min(k, len(nums1))):
        heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

    # 弹出 k 个最小的数对
    while heap and len(results) < k:
        _, i, j = heapq.heappop(heap)
        results.append([nums1[i], nums2[j]])

        # 如果 j < len(nums2) - 1，将同一行的下一个数对加入堆
        if j + 1 < len(nums2):
            heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

    return results


def run_tests():
    assert k_smallest_pairs([1, 7, 11], [2, 4, 6], 3) == [
        [1, 2],
        [1, 4],
        [1, 6],
    ]
    assert k_smallest_pairs([1, 1, 2], [1, 2, 3], 2) == [
        [1, 1],
        [1, 1],
    ]
    assert k_smallest_pairs([1, 2], [3], 3) == [[1, 3], [2, 3]]
    assert k_smallest_pairs([], [1, 2], 3) == []
    assert k_smallest_pairs([1, 2], [], 3) == []
    assert k_smallest_pairs([-2, -1], [3, 4], 3) == [
        [-2, 3],
        [-2, 4],
        [-1, 3],
    ]
    assert k_smallest_pairs([1, 1, 1], [1, 1], 10) == [
        [1, 1],
        [1, 1],
        [1, 1],
        [1, 1],
        [1, 1],
        [1, 1],
    ]

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
