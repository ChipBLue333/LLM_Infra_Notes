"""
Problem 033: House Robber

Difficulty:
Medium

Topic:
Dynamic Programming / Array

Description:
你是一个小偷，计划偷窃沿街排列的一排房屋。

每间房屋里都有一定金额的钱，使用整数数组 nums 表示，其中 nums[i] 是第 i 间房屋中的金额。

相邻的两间房屋不能在同一晚被偷，否则会触发报警系统。

请返回在不触发报警的前提下，你能偷到的最大金额。

Input:
nums: List[int] - 每间房屋中的金额

Output:
int - 可以偷到的最大金额

Examples:
Example 1:
Input:
nums = [1, 2, 3, 1]
Output:
4
Explanation:
偷第 0 间和第 2 间，总金额为 1 + 3 = 4。

Example 2:
Input:
nums = [2, 7, 9, 3, 1]
Output:
12
Explanation:
偷第 0 间、第 2 间和第 4 间，总金额为 2 + 9 + 1 = 12。

Example 3:
Input:
nums = [2, 1, 1, 2]
Output:
4
Explanation:
偷第 0 间和第 3 间，总金额为 2 + 2 = 4。

Constraints:
- 1 <= len(nums) <= 100
- 0 <= nums[i] <= 400

Task:
实现 rob(nums) 函数。

要求：
1. 使用动态规划。
2. 不要用递归暴力枚举所有偷法。
3. 可以使用 dp 数组，也可以使用两个变量压缩空间。
4. 注意处理只有 1 间房屋、只有 2 间房屋的边界情况。

思考：
- `dp[i]` 应该表示什么？
- 面对第 i 间房屋时，你有哪两个选择？
- 如果偷第 i 间，上一间房屋能不能偷？
- 为什么状态转移可以写成“偷当前房屋”和“不偷当前房屋”两种情况的最大值？
"""

from typing import List


def rob(nums: List[int]) -> int:
    # TODO: implement here
    # 偷东西越多越好 dp[i] 偷到第i间房屋时的最大金额
    # 偷当前房屋（第i间）：dp[i-2] + nums[i]
    # 不偷当前房屋：dp[i-1]
    # 定义dp数组
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])   
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    return dp[-1]  


def run_tests():
    assert rob([1, 2, 3, 1]) == 4
    assert rob([2, 7, 9, 3, 1]) == 12
    assert rob([2, 1, 1, 2]) == 4
    assert rob([1]) == 1
    assert rob([2, 1]) == 2
    assert rob([1, 2]) == 2
    assert rob([0, 0, 0]) == 0
    assert rob([5, 3, 4, 11, 2]) == 16

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
