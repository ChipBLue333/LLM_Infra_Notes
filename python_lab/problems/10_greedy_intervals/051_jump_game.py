"""
Problem 051: Jump Game

Difficulty:
Medium

Topic:
Array / Greedy

Description:
给定一个非负整数数组 `nums`，你最初位于数组的第一个下标。

数组中的每个元素表示你在该位置最多可以向前跳多少步。
请判断你是否能够到达最后一个下标。

Input:
nums: list[int] - 每个元素表示当前位置最多可以跳跃的步数

Output:
bool - 如果可以到达最后一个下标，返回 True；否则返回 False

Examples:
Example 1:
Input:
nums = [2, 3, 1, 1, 4]
Output:
True
Explanation:
可以先从下标 0 跳到下标 1，再从下标 1 跳到最后一个下标。

Example 2:
Input:
nums = [3, 2, 1, 0, 4]
Output:
False
Explanation:
无论如何都会停在下标 3，因为 nums[3] = 0，无法继续向前跳到最后一个下标。

Example 3:
Input:
nums = [0]
Output:
True
Explanation:
一开始就已经位于最后一个下标。

Constraints:
- 1 <= len(nums) <= 10^4
- 0 <= nums[i] <= 10^5

Task:
实现 can_jump(nums) 函数。

要求：
1. 返回是否可以到达最后一个下标。
2. 推荐使用贪心思路。
3. 不要使用递归搜索所有跳法。

提示：
- 你不需要真的枚举每一步跳到哪里。
- 可以维护一个变量，表示当前已经能够到达的最远下标。
- 遍历过程中，如果当前位置已经超过了最远可达下标，说明这个位置不可达。
"""

from typing import List


def can_jump(nums: List[int]) -> bool:
    # TODO: implement here
    # 定义farthest变量，表示当前能够到达的最远下标
    farthest = 0
    for i in range(len(nums)):
        # 如果当前位置i已经超过了farthest，说明这个位置不可达，直接返回False
        if i > farthest:
            return False
        # 更新farthest为当前位置能够跳跃的最远下标
        farthest = max(farthest, i + nums[i])
    # 如果遍历结束后farthest已经能够到达或超过最后一个下标，返回True
    return farthest >= len(nums) - 1


def run_tests():
    assert can_jump([2, 3, 1, 1, 4]) is True
    assert can_jump([3, 2, 1, 0, 4]) is False
    assert can_jump([0]) is True
    assert can_jump([1, 0]) is True
    assert can_jump([0, 1]) is False
    assert can_jump([2, 0, 0]) is True
    assert can_jump([1, 1, 0, 1]) is False
    assert can_jump([4, 0, 0, 0, 0]) is True

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
