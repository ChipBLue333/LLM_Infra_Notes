"""
Problem 042: Target Sum

Difficulty:
Medium

Topic:
Dynamic Programming / 0-1 Knapsack / Count Ways

Description:
给定一个非负整数数组 `nums` 和一个整数 `target`。

你需要给数组中的每个数字前面添加一个 `+` 或 `-` 符号，
使得最终表达式的计算结果等于 `target`。

请返回一共有多少种不同的符号添加方式。

注意：
- 每个数字都必须使用一次。
- 每个数字只能选择 `+` 或 `-` 一种符号。
- 即使数组中有重复数字，它们位于不同位置，也算作不同选择。

Input:
nums: list[int] - 一个非负整数数组
target: int - 目标和

Output:
int - 可以得到目标和的符号添加方式数量

Examples:
Example 1:
Input:
nums = [1, 1, 1, 1, 1], target = 3
Output:
5
Explanation:
一共有 5 种方式可以得到 3。

Example 2:
Input:
nums = [1], target = 1
Output:
1

Example 3:
Input:
nums = [1], target = 2
Output:
0

Constraints:
- 1 <= len(nums) <= 20
- 0 <= nums[i] <= 1000
- -1000 <= target <= 1000
- sum(nums) <= 1000

Task:
实现 find_target_sum_ways(nums, target) 函数。

要求：
1. 使用动态规划。
2. 不要使用递归暴力枚举所有符号组合。
3. 尝试把问题转换为“从 nums 中选择若干个数，使其和等于某个容量”的计数问题。
4. 注意处理无法转换的情况。
5. 注意数组中出现 0 时，方案数会如何变化。

思考：
- 如果所有加号数字之和为 positive，所有减号数字之和为 negative，
  那么 positive - negative = target。
- 又因为 positive + negative = sum(nums)。
- 你能推导出 positive 应该等于多少吗？
- 什么时候这个 positive 不可能是合法容量？
- `dp[x]` 应该表示什么？
- 每个数字只能使用一次时，容量应该正序还是倒序遍历？
"""

from typing import List


def find_target_sum_ways(nums: List[int], target: int) -> int:
    # TODO: implement here
    # 定义dp[i]凑出i的方案数
    s = sum(nums)
    # 计算正数的和
    # positive + negative = s
    # positive - negative = target
    positive = (s + target) // 2
    # 如果正数的和不是整数或者负数的和为负数，返回0
    if (s + target) % 2 != 0 or positive < 0:
        return 0
    dp = [0] * (positive + 1)
    dp[0] = 1
    for num in nums:
        for j in range(positive, num - 1, -1):
            dp[j] += dp[j - num]
    return dp[positive]



def run_tests():
    assert find_target_sum_ways([1, 1, 1, 1, 1], 3) == 5
    assert find_target_sum_ways([1], 1) == 1
    assert find_target_sum_ways([1], 2) == 0
    assert find_target_sum_ways([0], 0) == 2
    assert find_target_sum_ways([0, 0, 1], 1) == 4
    assert find_target_sum_ways([2, 3, 5, 7], 3) == 2
    assert find_target_sum_ways([100], -100) == 1

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
