"""
Problem 060: Kth Largest Element in an Array

Difficulty:
Medium

Topic:
Heap / Array

Description:
给定一个整数数组 nums 和一个整数 k，请返回数组中第 k 大的元素。

注意：
这里说的是“排序后第 k 大的元素”，不是第 k 个不同的元素。

Input:
nums: List[int] - 整数数组
k: int - 要查找第几大的元素

Output:
int - 数组中第 k 大的元素

Examples:
Example 1:
Input:
nums = [3, 2, 1, 5, 6, 4]
k = 2
Output:
5
Explanation:
排序后是 [6, 5, 4, 3, 2, 1]，第 2 大是 5。

Example 2:
Input:
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
Output:
4
Explanation:
排序后是 [6, 5, 5, 4, 3, 3, 2, 2, 1]，第 4 大是 4。

Constraints:
- 1 <= k <= len(nums) <= 100000
- -100000 <= nums[i] <= 100000
- nums 中可以有重复元素

Task:
实现 find_kth_largest(nums, k) 函数。

要求：
1. 不要直接使用 sorted(nums) 或 nums.sort() 完成整题。
2. 推荐使用最小堆维护当前见过的前 k 大元素。
3. 堆的大小应该尽量保持不超过 k。

提示：
- Python 的 heapq 是最小堆。
- 当堆中保存的是“当前前 k 大元素”时，堆顶就是这 k 个数里最小的那个。
- 遍历结束后，堆顶应该就是整个数组的第 k 大元素。
"""

from typing import List
import heapq

def find_kth_largest(nums: List[int], k: int) -> int:
    # 在当前堆中保存前 k 大的元素
    min_heap = []
    for num in nums:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        else:
            if num > min_heap[0]:  # 如果当前数比堆顶还大，说明它应该进入前 k 大的行列
                heapq.heapreplace(min_heap, num)  # 替换掉堆顶
    return min_heap[0]  # 堆顶就是第 k 大的元素


def run_tests():
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    assert find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert find_kth_largest([1], 1) == 1
    assert find_kth_largest([2, 1], 1) == 2
    assert find_kth_largest([2, 1], 2) == 1
    assert find_kth_largest([-1, -2, -3, -4], 2) == -2
    assert find_kth_largest([5, 5, 5, 5], 3) == 5
    assert find_kth_largest([7, 10, 4, 3, 20, 15], 3) == 10

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
