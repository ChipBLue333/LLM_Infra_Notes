"""
Problem 041: Partition Equal Subset Sum

Difficulty:
Medium

Topic:
Dynamic Programming / 0-1 Knapsack

Description:
给定一个只包含正整数的数组 `nums`。

请判断是否可以把这个数组分成两个子集，使得两个子集的元素和相等。

每个数字只能使用一次。

Input:
nums: list[int] - 一个正整数数组

Output:
bool - 如果可以分成两个和相等的子集，返回 True；否则返回 False

Examples:
Example 1:
Input:
nums = [1, 5, 11, 5]
Output:
True
Explanation:
可以分成 [1, 5, 5] 和 [11]，两个子集的和都是 11。

Example 2:
Input:
nums = [1, 2, 3, 5]
Output:
False
Explanation:
无法分成两个和相等的子集。

Constraints:
- 1 <= len(nums) <= 200
- 1 <= nums[i] <= 100

Task:
实现 can_partition(nums) 函数。

要求：
1. 使用动态规划。
2. 不要使用递归暴力枚举所有子集。
3. 每个数字只能使用一次。
4. 如果数组总和是奇数，可以直接返回 False。
5. 将问题转换成：是否存在一个子集，其元素和等于总和的一半。

思考：
- 如果总和是 total，那么目标子集和 target 应该是多少？
- `dp[x]` 应该表示什么？
- `dp[0]` 应该初始化为什么？
- 为什么每个数字只能用一次时，金额/容量要倒序遍历？
- 如果正序遍历，会不会让同一个数字在一轮里被重复使用？
"""

from typing import List


def can_partition(nums: List[int]) -> bool:
    # TODO: implement here
    # 定义dp数组，dp[x]表示是否存在一个子集，其元素和等于x  (只关心true/false，不关心具体组合)
    # 计算总和
    total = sum(nums)
    # 如果总和是奇数，无法分成两个和相等的子集
    if total % 2 != 0:
        return False
    target = total // 2
    # 初始化dp数组
    dp = [False] * (target + 1)
    dp[0] = True  # 凑出金额0有一种方式：不选择任何数字
    for num in nums:
        for x in range(target, num - 1, -1):  # 倒序遍历金额 从target开始 因为小于num的金额无法使用这个数字
            dp[x] = dp[x] or dp[x - num]  # 是否可以凑出金额x，要么之前就可以，要么现在这个数字可以凑出
    return dp[target]


def run_tests():
    assert can_partition([1, 5, 11, 5]) is True
    assert can_partition([1, 2, 3, 5]) is False
    assert can_partition([1, 2, 3, 4]) is True
    assert can_partition([2, 2, 3, 5]) is False
    assert can_partition([100]) is False
    assert can_partition([2, 2]) is True

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
