"""
Problem 007: Minimum Size Subarray Sum

Difficulty:
Medium

Topic:
Array / Sliding Window

Description:
给定一个含有 n 个正整数的数组和一个正整数 target。
找出该数组中满足其总和 >= target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。
如果不存在符合条件的子数组，返回 0。

Input:
target: int - 目标正整数
nums: List[int] - 一个正整数数组

Output:
int - 满足条件的最小连续子数组长度。如果没找到则返回 0。

Examples:
Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Constraints:
- 1 <= target <= 10^9
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4
- 你能实现时间复杂度为 O(n) 的解法吗？

Task:
实现 min_sub_array_len(target, nums) 函数。
"""

from typing import List

def min_sub_array_len(target: int, nums: List[int]) -> int:
    # TODO: implement here
    # 用一个变量记录当前的和，用两个指针表示当前的子数组范围
    left = 0
    right = 0
    current_sum = 0
    min_length = 10**5 + 1 # 初始化最小长度为极大值
    while right < len(nums):
        current_sum += nums[right] # 将右指针指向的元素加入当前和
        right += 1 # 右指针向右移动
        while current_sum >= target: # 当当前和大于等于目标时，尝试缩小子数组
            min_length = min(min_length, right - left) # 更新最小长度
            current_sum -= nums[left] # 将左指针指向的元素从当前和中移除
            left += 1 # 左指针向右移动
    return min_length if min_length != 10**5 + 1 else 0 # 如果最小长度没有更新过，说明没有找到满足条件的子数组，返回0，否则
    # 扫一遍 最小长度的值就被选出来了
    


def run_tests():
    assert min_sub_array_len(7, [2,3,1,2,4,3]) == 2
    assert min_sub_array_len(4, [1,4,4]) == 1
    assert min_sub_array_len(11, [1,1,1,1,1,1,1,1]) == 0
    assert min_sub_array_len(11, [1,2,3,4,5]) == 3
    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
