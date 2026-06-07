"""
Problem 001: 两数之和 (Two Sum)

Difficulty:
Easy

Topic:
Array / Hash Map

Description:
给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该数组中找出和为目标值 `target` 的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。

Input:
- nums: List[int]，整数数组
- target: int，目标和

Output:
- List[int]，包含两个符合条件的下标。

Examples:
Example 1:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: 因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

Example 2:
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9

Task:
实现 solution 函数。
"""

from typing import List


def solution(nums: List[int], target: int) -> List[int]:
    # 使用字典记录遍历过的数字及其对应的下标 {数字: 下标}
    seen_map = {}
    
    # 遍历数组，enumerate 会同时返回索引 i 和 值 num
    for i, num in enumerate(nums):
        complement = target - num  # 计算需要的另一半
        
        # 检查另一半是否已经在之前遍历的过程中记录在字典中了
        if complement in seen_map:
            # 如果存在，说明找到了配对！
            # seen_map[complement] 是之前那个数的下标，i 是当前数字的下标
            return [seen_map[complement], i]
        
        # 如果没找到配对，就把当前数字 num 及其下标 i 存入字典中
        seen_map[num] = i
        
    return []


def run_tests():
    assert sorted(solution([2, 7, 11, 15], 9)) == [0, 1], "Test case 1 failed"
    assert sorted(solution([3, 2, 4], 6)) == [1, 2], "Test case 2 failed"
    assert sorted(solution([3, 3], 6)) == [0, 1], "Test case 3 failed"
    print("All test cases passed!")


if __name__ == "__main__":
    run_tests()
