"""
Problem 008: Search Insert Position

Difficulty:
Easy

Topic:
Array / Binary Search

Description:
给定一个排序数组 nums 和一个目标值 target。
如果 target 存在于 nums 中，返回它的下标。
如果 target 不存在于 nums 中，返回它按顺序插入数组时应该所在的位置。

要求算法时间复杂度为 O(log n)。

Input:
nums: List[int] - 一个严格递增排序的整数数组
target: int - 目标整数

Output:
int - target 的下标，或者 target 应该插入的位置

Examples:
Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Example 4:
Input: nums = [1,3,5,6], target = 0
Output: 0

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums 中的值严格递增
- -10^4 <= target <= 10^4

Task:
实现 search_insert(nums, target) 函数。
"""

from typing import List


def search_insert(nums: List[int], target: int) -> int:
    # TODO: implement here
    # nums严格递增，使用二分查找
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2    # 避免(left + right)可能溢出
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:    # 如果中值小于目标 则目标在[mid+1, right]区间
            left = mid + 1
        else:
            right = mid - 1
    return left


def run_tests():
    assert search_insert([1, 3, 5, 6], 5) == 2
    assert search_insert([1, 3, 5, 6], 2) == 1
    assert search_insert([1, 3, 5, 6], 7) == 4
    assert search_insert([1, 3, 5, 6], 0) == 0
    assert search_insert([1], 1) == 0
    assert search_insert([1], 0) == 0
    assert search_insert([1], 2) == 1
    assert search_insert([-3, -1, 2, 8], -2) == 1
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
