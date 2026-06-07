"""
Problem 034: Maximum Subarray

Difficulty:
Medium

Topic:
Dynamic Programming / Array

Description:
给定一个整数数组 nums，请找出一个具有最大和的连续子数组，并返回这个最大和。

子数组必须是数组中连续的一段，并且至少包含一个元素。

Input:
nums: List[int] - 整数数组

Output:
int - 连续子数组的最大和

Examples:
Example 1:
Input:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output:
6
Explanation:
连续子数组 [4, -1, 2, 1] 的和最大，为 6。

Example 2:
Input:
nums = [1]
Output:
1
Explanation:
只有一个元素，最大子数组和就是它本身。

Example 3:
Input:
nums = [5, 4, -1, 7, 8]
Output:
23
Explanation:
整个数组的和最大，为 23。

Constraints:
- 1 <= len(nums) <= 100000
- -10000 <= nums[i] <= 10000

Task:
实现 max_sub_array(nums) 函数。

要求：
1. 使用动态规划或等价的一次遍历思路。
2. 不要使用双重循环枚举所有子数组。
3. 子数组必须连续。
4. 注意所有数字都是负数的情况。

思考：
- `dp[i]` 可以表示“必须以第 i 个元素结尾的最大子数组和”。
- 如果前面的连续子数组和是负数，接上它会让当前结果变大还是变小？
- 面对 nums[i]，你有哪两个选择：
  1. 接在前一个连续子数组后面；
  2. 从 nums[i] 自己重新开始。
- 为什么最终答案不一定是 `dp[-1]`？
"""

from typing import List


def max_sub_array(nums: List[int]) -> int:
    # TODO: implement here
    # dp[i] 表示必须以第 i 个元素结尾的最大连续子数组和
    dp = [0] * len(nums)
    dp[0] = nums[0]
    max_sum = dp[0]

    for i in range(1, len(nums)):   # 从第二个元素开始遍历
        dp[i] = max(nums[i], dp[i-1] + nums[i]) # 选择接在前一个连续子数组后面还是从当前元素重新开始
        max_sum = max(max_sum, dp[i])   # 每次更新最大值，因为最大子数组不一定以最后一个元素结尾

    return max_sum


def run_tests():
    assert max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_sub_array([1]) == 1
    assert max_sub_array([5, 4, -1, 7, 8]) == 23
    assert max_sub_array([-1]) == -1
    assert max_sub_array([-3, -2, -5]) == -2
    assert max_sub_array([0, 0, 0]) == 0
    assert max_sub_array([4, -1, 2, -7, 3, 4]) == 7
    assert max_sub_array([-2, -1, 3, -1, 2, -5, 4]) == 4

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
