"""
Problem 021: Combination Sum

Difficulty:
Medium

Topic:
Backtracking / DFS / Array

Description:
给定一个无重复元素的正整数数组 candidates 和一个正整数 target，找出 candidates 中所有可以使数字和为目标数 target 的唯一组合。

candidates 中的数字可以无限制重复被选取。如果至少一个所选数字数量不同，则两种组合是不同的。
结果中不允许包含重复的组合。
返回结果的顺序不限，组合内元素的顺序也不限。

Input:
candidates: List[int] - 无重复元素的正整数数组
target: int - 目标和

Output:
List[List[int]] - 所有和为 target 的组合

Examples:
Example 1:
Input: candidates = [2, 3, 6, 7], target = 7
Output: [[2, 2, 3], [7]]
解释：
2 和 3 可以形成一组候选，2 + 2 + 3 = 7。
7 也是一个候选，7 = 7。
这是所有可能的两组组合。

Example 2:
Input: candidates = [2, 3, 5], target = 8
Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

Example 3:
Input: candidates = [2], target = 1
Output: []

Constraints:
- 1 <= candidates.length <= 30
- 2 <= candidates[i] <= 40
- candidates 的所有元素绝对互不相同
- 1 <= target <= 40

Task:
实现 combination_sum(candidates, target) 函数。
建议使用回溯法，注意如何避免生成重复的组合。
"""

from typing import List

def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    # TODO: implement here
    # 先对 candidates 进行排序，方便后续剪枝
    candidates.sort()
    result = []
    # 定义回溯函数
    def backtrack(start, path, target):
        # 如果目标值为 0，说明找到了一个有效组合
        if target == 0:
            result.append(path)
            return
        # 从当前索引开始遍历候选数
        for i in range(start, len(candidates)):
            # 如果当前候选数大于剩余目标值，后续的候选数也会更大，直接剪枝
            if candidates[i] > target:
                break
            # 递归调用，允许重复使用当前候选数
            backtrack(i, path + [candidates[i]], target - candidates[i])
    # 从第一个候选数开始回溯
    backtrack(0, [], target)
    return result

def run_tests():
    def check_result(result, expected):
        # 排序以便于比较
        res_sorted = sorted([sorted(comb) for comb in result])
        exp_sorted = sorted([sorted(comb) for comb in expected])
        assert res_sorted == exp_sorted, f"Expected {expected}, but got {result}"

    check_result(combination_sum([2, 3, 6, 7], 7), [[2, 2, 3], [7]])
    check_result(combination_sum([2, 3, 5], 8), [[2, 2, 2, 2], [2, 3, 3], [3, 5]])
    check_result(combination_sum([2], 1), [])
    check_result(combination_sum([3, 5, 8], 11), [[3, 3, 5], [3, 8]])
    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
