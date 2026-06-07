"""
Problem 052: Jump Game II

Difficulty:
Medium

Topic:
Array / Greedy

Description:
给定一个非负整数数组 `nums`，你最初位于数组的第一个下标。

数组中的每个元素表示你在该位置最多可以向前跳多少步。
请返回到达最后一个下标所需的最少跳跃次数。

题目保证一定可以到达最后一个下标。

Input:
nums: list[int] - 每个元素表示当前位置最多可以跳跃的步数

Output:
int - 到达最后一个下标所需的最少跳跃次数

Examples:
Example 1:
Input:
nums = [2, 3, 1, 1, 4]
Output:
2
Explanation:
最少跳 2 次：从下标 0 跳到下标 1，再从下标 1 跳到最后一个下标。

Example 2:
Input:
nums = [2, 3, 0, 1, 4]
Output:
2
Explanation:
最少跳 2 次：从下标 0 跳到下标 1，再从下标 1 跳到最后一个下标。

Example 3:
Input:
nums = [0]
Output:
0
Explanation:
一开始就在最后一个下标，不需要跳跃。

Constraints:
- 1 <= len(nums) <= 10^4
- 0 <= nums[i] <= 10^5
- 题目保证一定可以到达最后一个下标

Task:
实现 jump(nums) 函数。

要求：
1. 返回到达最后一个下标所需的最少跳跃次数。
2. 推荐使用贪心思路。
3. 不要使用递归搜索所有跳法。

提示：
- 这题不是判断能不能到达，而是计算最少需要跳几次。
- 可以把“当前这一跳能覆盖的范围”看成一个区间。
- 在当前区间内遍历时，持续更新“下一跳最远能覆盖到哪里”。
- 当遍历到当前区间的右边界时，说明必须增加一次跳跃，并把区间扩展到下一跳的最远位置。
"""

from typing import List


def jump(nums: List[int]) -> int:
    # TODO: implement here
    # jumps 表示已经跳了几次
    # current_end 表示当前跳跃能覆盖到的最右边界
    # farthest 表示在当前跳跃范围内，下一跳能覆盖的最远位置
    jumps = 0
    current_end = 0
    farthest = 0
    # 遍历每一个位置i
    for i in range(len(nums) - 1):  # 注意最后一个位置不需要跳跃
        # 更新farthest为当前位置能够跳跃的最远下标
        farthest = max(farthest, i + nums[i])
        # 如果当前位置i已经到达了当前跳跃的边界，说明需要增加一次跳跃
        if i == current_end:
            jumps += 1
            current_end = farthest  # 更新当前跳跃的边界为下一跳能覆盖的最远位置
    return jumps    



def run_tests():
    assert jump([2, 3, 1, 1, 4]) == 2
    assert jump([2, 3, 0, 1, 4]) == 2
    assert jump([0]) == 0
    assert jump([1, 0]) == 1
    assert jump([1, 1, 1, 1]) == 3
    assert jump([4, 0, 0, 0, 0]) == 1
    assert jump([3, 4, 3, 2, 5, 4, 3]) == 3
    assert jump([2, 1]) == 1

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
