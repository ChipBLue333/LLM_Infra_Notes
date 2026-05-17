"""
Problem 024: Subsets II

Difficulty:
Medium

Topic:
Backtracking / DFS / Array

Description:
给定一个可能包含重复元素的整数列表 nums，返回该列表所有不重复的子集。

子集内部元素的顺序应与搜索选择顺序保持一致；返回结果的整体顺序不作要求。

Input:
nums: List[int] - 可能包含重复元素的整数列表

Output:
List[List[int]] - 所有不重复的子集

Examples:
Example 1:
Input:
nums = [1, 2, 2]
Output:
[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]

Example 2:
Input:
nums = [0]
Output:
[[], [0]]

Constraints:
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10

Task:
实现 subsets_with_dup(nums) 函数。

要求：
1. 先对 nums 排序，方便处理重复元素。
2. 使用回溯算法。
3. 不要使用 set(tuple(...)) 这种方式事后去重。
4. 重点思考：这题是“子集/组合型搜索”，每一层应该从哪个下标开始？
5. 重点思考：同一层遇到重复数字时，应该如何跳过？
"""

from typing import List


def subsets_with_dup(nums: List[int]) -> List[List[int]]:
    # TODO: implement here
    # 先排序
    nums.sort()
    result = []
    # 如果是空集，直接返回 [[]]
    if not nums:
        return [[]]
    
    # 回溯函数
    path = []
    def backtrack(start: int):
        # 将当前路径加入结果
        result.append(path.copy())
        
        for i in range(start, len(nums)):
            # 如果当前元素和前一个元素相同，并且不是同一层的第一个元素，跳过
            if i > start and nums[i] == nums[i - 1]:
                continue
            
            # 选择当前元素
            path.append(nums[i])
            # 继续回溯，注意下一个起始位置是 i + 1
            backtrack(i + 1)
            # 回退选择
            path.pop()

    backtrack(0)
    return result


def run_tests():
    def normalize(result: List[List[int]]) -> List[List[int]]:
        return sorted([list(item) for item in result])

    assert normalize(subsets_with_dup([1, 2, 2])) == normalize(
        [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
    )
    assert normalize(subsets_with_dup([0])) == normalize([[], [0]])
    assert normalize(subsets_with_dup([1, 1])) == normalize([[], [1], [1, 1]])
    assert normalize(subsets_with_dup([2, 1, 2])) == normalize(
        [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
    )
    assert normalize(subsets_with_dup([-1, -1, 2])) == normalize(
        [[], [-1], [-1, -1], [-1, -1, 2], [-1, 2], [2]]
    )
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
