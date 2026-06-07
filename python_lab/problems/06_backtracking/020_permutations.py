"""
Problem 020: Permutations

Difficulty:
Medium

Topic:
Backtracking / DFS / Array

Description:
给定一个不包含重复元素的整数列表 nums，返回它的所有全排列。

全排列表示把 nums 中的所有元素都使用一次，并按照不同顺序组成列表。
结果顺序不限。

Input:
nums: List[int] - 不包含重复元素的整数列表

Output:
List[List[int]] - nums 的所有全排列

Examples:
Example 1:
Input:
nums = [1, 2, 3]
Output:
[
    [1, 2, 3],
    [1, 3, 2],
    [2, 1, 3],
    [2, 3, 1],
    [3, 1, 2],
    [3, 2, 1],
]

Example 2:
Input:
nums = [0, 1]
Output:
[[0, 1], [1, 0]]

Example 3:
Input:
nums = [1]
Output:
[[1]]

Constraints:
- 1 <= len(nums) <= 8
- -10 <= nums[i] <= 10
- nums 中的所有元素互不相同

Task:
实现 permute(nums) 函数。

要求：
- 不要使用 itertools。
- 建议使用回溯。
- 每个元素在一个排列中只能使用一次。
- 当 path 长度等于 nums 长度时，说明得到一个完整排列。
"""

from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    # TODO: implement here
    # 如果 nums 为空，直接返回包含空列表的列表
    if not nums:
        return [[]]
    
    result = []
    path = []
    used = [False] * len(nums)  # nums有多少就给多少未被使用的标记 一旦被使用就改变

    # 回溯函数
    def backtrack():
        # 如果当前路径长度等于 nums 长度，说明得到一个完整排列
        if len(path) == len(nums):
            result.append(path.copy())
            return
        
        for i in range(len(nums)):
            # 如果当前元素已经被使用，跳过
            if used[i]:
                continue
            
            # 选择当前元素
            path.append(nums[i])
            used[i] = True
            
            # 继续递归选择下一个元素
            backtrack()
            
            # 回退，撤销选择
            path.pop()
            used[i] = False

    backtrack()
    return result


def normalize(result: List[List[int]]) -> List[List[int]]:
    return sorted(result)


def run_tests():
    assert normalize(permute([1, 2, 3])) == normalize(
        [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1],
        ]
    )
    assert normalize(permute([0, 1])) == normalize([[0, 1], [1, 0]])
    assert normalize(permute([1])) == normalize([[1]])

    result = permute([-1, 0, 1])
    assert len(result) == 6
    assert [-1, 0, 1] in result
    assert [1, 0, -1] in result

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
