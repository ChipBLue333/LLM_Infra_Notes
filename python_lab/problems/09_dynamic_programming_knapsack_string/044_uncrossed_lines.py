"""
Problem 044: Uncrossed Lines

Difficulty:
Medium

Topic:
Dynamic Programming / Array / 2D DP / Longest Common Subsequence

Description:
给定两个整数数组 `nums1` 和 `nums2`。

你可以在两个数组之间画线，规则如下：
- 如果 `nums1[i] == nums2[j]`，可以在这两个数字之间画一条线。
- 每个数字最多只能连接一条线。
- 画出的线不能相交。

请返回最多可以画多少条不相交的线。

本题本质上是在数组上寻找“最长公共子序列”的长度。

Input:
nums1: list[int] - 第一个整数数组
nums2: list[int] - 第二个整数数组

Output:
int - 最多可以画出的不相交线数量

Examples:
Example 1:
Input:
nums1 = [1, 4, 2], nums2 = [1, 2, 4]
Output:
2
Explanation:
可以连接两个 1，再连接两个 2；或者连接两个 1，再连接两个 4。
最多只能画 2 条不相交的线。

Example 2:
Input:
nums1 = [2, 5, 1, 2, 5], nums2 = [10, 5, 2, 1, 5, 2]
Output:
3

Example 3:
Input:
nums1 = [1, 3, 7, 1, 7, 5], nums2 = [1, 9, 2, 5, 1]
Output:
2

Constraints:
- 1 <= len(nums1), len(nums2) <= 500
- 1 <= nums1[i], nums2[j] <= 2000

Task:
实现 max_uncrossed_lines(nums1, nums2) 函数。

要求：
1. 使用动态规划。
2. 不要使用递归暴力枚举所有连接方式。
3. 建议使用二维 DP 表。
4. `dp[i][j]` 可以表示 nums1 的前 i 个元素和 nums2 的前 j 个元素最多能画多少条不相交线。
5. 注意 i、j 和数组下标之间差 1 的关系。

思考：
- 如果 nums1[i - 1] == nums2[j - 1]，当前两个数字能否连接？
- 如果当前两个数字不相等，应该尝试跳过哪一边的当前数字？
- 这道题和 Longest Common Subsequence 的转移有什么相同点？
"""

from typing import List


def max_uncrossed_lines(nums1: List[int], nums2: List[int]) -> int:
    # TODO: implement here
    # 定义dp[i][j] 表示nums1的前i个元素和nums2的前j个元素最多能画多少条不相交线
    # 不相交的线说明两个数组下标都是单调递增的
    m = len(nums1)
    n = len(nums2)
    dp = [[0] * (n + 1) for _ in range(m + 1)] # 0行和0列表示空数组的情况
    # 填充dp表
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if nums1[i - 1] == nums2[j - 1]: # 当前数字相等，可以连接
                dp[i][j] = dp[i - 1][j - 1] + 1
            else: # 当前数字不相等，尝试跳过nums1当前数字或nums2当前数字
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # 取跳过nums1当前数字或跳过nums2当前数字的较大值 则下标单调递增
    return dp[m][n]



def run_tests():
    assert max_uncrossed_lines([1, 4, 2], [1, 2, 4]) == 2
    assert max_uncrossed_lines([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]) == 3
    assert max_uncrossed_lines([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]) == 2
    assert max_uncrossed_lines([1], [1]) == 1
    assert max_uncrossed_lines([1], [2]) == 0
    assert max_uncrossed_lines([1, 1, 2, 1], [1, 2, 1, 1]) == 3
    assert max_uncrossed_lines([3, 3, 3], [3, 3]) == 2

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
