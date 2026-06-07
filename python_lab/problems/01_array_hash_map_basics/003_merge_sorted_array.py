"""
Problem 003: 合并两个有序数组 (Merge Sorted Array)

Difficulty:
Easy

Topic:
Array / Two Pointers

Description:
给你两个按 非递减顺序 排列的整数数组 `nums1` 和 `nums2`，另有两个整数 `m` 和 `n` ，分别表示 `nums1` 和 `nums2` 中的元素数目。

请你合并 `nums2` 到 `nums1` 中，使合并后的数组同样按 非递减顺序 排列。

注意：最终，合并后数组不应由函数返回，而是存储在数组 `nums1` 中。为了应对这种情况，`nums1` 的初始长度为 `m + n`，其中前 `m` 个元素表示应合并的元素，后 `n` 个元素为 0 ，应忽略。`nums2` 的长度为 `n` 。

Input:
- nums1: List[int]，长度为 m + n
- m: int，nums1 中有效元素的个数
- nums2: List[int]，长度为 n
- n: int，nums2 中有效元素的个数

Output:
- 无返回值 (None)，直接在 nums1 上进行原地 (in-place) 修改。

Examples:
Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6] (这里指 nums1 修改后的结果)
Explanation: 需要合并 [1,2,3] 和 [2,5,6] 。合并结果是 [1,2,2,3,5,6] 。

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]

Constraints:
- nums1.length == m + n
- nums2.length == n
- 0 <= m, n <= 200
- 1 <= m + n <= 200
- -10^9 <= nums1[i], nums2[j] <= 10^9

Task:
实现 solution 函数。
"""

from typing import List


def solution(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    修改 nums1 即可，无需返回新数组。
    """
    # TODO: implement here
    # 定义三个指针p1 p2 p
    # 从nums2的最大元素开始找 如果nums2的最大元素比nums1的最大元素还大 那么就把nums2的最大元素放在nums1的最后面
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1
    while p1 >= 0 and p2 >= 0:
        if nums2[p2] > nums1[p1]:
            nums1[p] = nums2[p2]
            p2 -= 1
        else:
            nums1[p] = nums1[p1]
            p1 -= 1
        p -= 1
    # 边界情况 如果nums2还有剩余元素（全都比nums1小） 那么就把剩余元素放在nums1的前面
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1


def run_tests():
    nums1_1 = [1, 2, 3, 0, 0, 0]
    solution(nums1_1, 3, [2, 5, 6], 3)
    assert nums1_1 == [1, 2, 2, 3, 5, 6], f"Test case 1 failed: {nums1_1}"

    nums1_2 = [1]
    solution(nums1_2, 1, [], 0)
    assert nums1_2 == [1], f"Test case 2 failed: {nums1_2}"

    nums1_3 = [0]
    solution(nums1_3, 0, [1], 1)
    assert nums1_3 == [1], f"Test case 3 failed: {nums1_3}"
    
    nums1_4 = [2, 0]
    solution(nums1_4, 1, [1], 1)
    assert nums1_4 == [1, 2], f"Test case 4 failed: {nums1_4}"

    print("All test cases passed!")


if __name__ == "__main__":
    run_tests()
