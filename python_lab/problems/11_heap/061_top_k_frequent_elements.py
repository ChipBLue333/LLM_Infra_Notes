"""
Problem 061: Top K Frequent Elements

Difficulty:
Medium

Topic:
Hash Map / Heap / Array

Description:
给定一个整数数组 nums 和一个整数 k，请返回出现频率最高的 k 个元素。

返回结果的顺序不重要。

注意：
本题要按“出现次数”排序，不是按数值大小排序。

Input:
nums: List[int] - 整数数组
k: int - 需要返回的高频元素数量

Output:
List[int] - 出现频率最高的 k 个元素，顺序不限

Examples:
Example 1:
Input:
nums = [1, 1, 1, 2, 2, 3]
k = 2
Output:
[1, 2]
Explanation:
1 出现 3 次，2 出现 2 次，它们是频率最高的两个元素。

Example 2:
Input:
nums = [1]
k = 1
Output:
[1]

Example 3:
Input:
nums = [4, 4, 4, 6, 6, 7, 7, 7, 7]
k = 2
Output:
[7, 4]
Explanation:
7 出现 4 次，4 出现 3 次，是频率最高的两个元素。

Constraints:
- 1 <= len(nums) <= 100000
- -10000 <= nums[i] <= 10000
- 1 <= k <= 不同元素的数量
- 测试数据保证答案唯一

Task:
实现 top_k_frequent(nums, k) 函数。

要求：
1. 不要使用 collections.Counter。
2. 先用 dict 自己统计每个数字出现的次数。
3. 推荐使用大小为 k 的最小堆维护当前频率最高的 k 个元素。
4. 返回结果顺序不限。

提示：
- 堆里可以保存二元组：(frequency, num)。
- 当堆大小超过 k 时，弹出频率最小的元素。
- 遍历完频率表后，堆里剩下的元素就是答案。
"""

from typing import List
import heapq


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    # 遍历nums 用dict统计每个数字出现的次数
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    # 用最小堆维护当前频率最高的 k 个元素 二元组 (frequency, num)
    min_heap = []
    for num, count in freq.items():
        if len(min_heap) < k:
            heapq.heappush(min_heap, (count, num))
        else:
            if count > min_heap[0][0]:  # 如果当前频率比堆顶还大，说明它应该进入前 k 大的行列
                heapq.heapreplace(min_heap, (count, num))
    # 返回堆里剩下的元素的num部分
    return [num for count, num in min_heap]


def same_elements(actual: List[int], expected: List[int]) -> bool:
    return sorted(actual) == sorted(expected)


def run_tests():
    assert same_elements(top_k_frequent([1, 1, 1, 2, 2, 3], 2), [1, 2])
    assert same_elements(top_k_frequent([1], 1), [1])
    assert same_elements(top_k_frequent([4, 4, 4, 6, 6, 7, 7, 7, 7], 2), [7, 4])
    assert same_elements(top_k_frequent([-1, -1, -2, -2, -2, 3], 1), [-2])
    assert same_elements(top_k_frequent([5, 6, 5, 6, 5, 7], 2), [5, 6])
    assert same_elements(top_k_frequent([9, 8, 7, 9, 8, 9], 3), [9, 8, 7])

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
