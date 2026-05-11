"""
Problem 019: Subsets

Difficulty:
Medium

Topic:
Backtracking / DFS / Array

Description:
给定一个不包含重复元素的整数列表 nums，返回它的所有子集。

子集可以包含 nums 中的任意数量元素，包括空集和完整集合。
结果中的子集顺序不限，每个子集内部元素的顺序应与它们在 nums 中出现的顺序一致。

Input:
nums: List[int] - 不包含重复元素的整数列表

Output:
List[List[int]] - nums 的所有子集

Examples:
Example 1:
Input:
nums = [1, 2, 3]
Output:
[[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]

Example 2:
Input:
nums = [0]
Output:
[[], [0]]

Constraints:
- 0 <= len(nums) <= 10
- -10 <= nums[i] <= 10
- nums 中的所有元素互不相同

Task:
实现 subsets(nums) 函数。

要求：
- 不要使用 itertools。
- 建议使用回溯。
- 注意把当前 path 加入结果时需要复制一份。
"""

from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    # TODO: implement here
    # 如果是空集，直接返回包含空集的列表
    if not nums:
        return [[]]
    
    result = []
    path = []

    def backtrack(start: int):
        # 将当前路径加入结果
        result.append(path.copy())
        
        for i in range(start, len(nums)):
            # 选择当前元素
            path.append(nums[i])
            # 继续递归选择下一个元素
            backtrack(i + 1)
            # 回退，撤销选择
            path.pop()

    backtrack(0)
    
    return result



def normalize(result: List[List[int]]) -> List[List[int]]:
    return sorted([sorted(item) for item in result])


def run_tests():
    assert normalize(subsets([1, 2, 3])) == normalize(
        [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    )
    assert normalize(subsets([0])) == normalize([[], [0]])
    assert normalize(subsets([])) == normalize([[]])
    assert normalize(subsets([-1, 2])) == normalize([[], [-1], [2], [-1, 2]])

    result = subsets([4, 5, 6, 7])
    assert len(result) == 16
    assert [] in result
    assert [4, 5, 6, 7] in result

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
