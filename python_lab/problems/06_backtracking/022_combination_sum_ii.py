"""
Problem 022: Combination Sum II

Difficulty:
Medium

Topic:
Backtracking / DFS / Array

Description:
给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

注意：解集不能包含重复的组合。

Input:
candidates: List[int] - 包含重复元素的正整数数组
target: int - 目标和

Output:
List[List[int]] - 所有和为 target 的不重复组合

Examples:
Example 1:
Input: candidates = [10, 1, 2, 7, 6, 1, 5], target = 8
Output:
[
  [1, 1, 6],
  [1, 2, 5],
  [1, 7],
  [2, 6]
]

Example 2:
Input: candidates = [2, 5, 2, 1, 2], target = 5
Output:
[
  [1, 2, 2],
  [5]
]

Constraints:
- 1 <= candidates.length <= 100
- 1 <= candidates[i] <= 50
- 1 <= target <= 30

Task:
实现 combination_sum2(candidates, target) 函数。
"""

from typing import List

def combination_sum2(candidates: List[int], target: int) -> List[List[int]]:
    # TODO: implement here
    # 先对 candidates 进行排序，方便后续剪枝和去重
    candidates.sort()
    result = []
    # 定义回溯函数
    def backtrack(start, path, target):
        if target == 0:
            result.append(path)
            return
        for i in range(start, len(candidates)):
            # 如果当前数字大于剩余目标，后续数字也会大于目标，直接剪枝
            if candidates[i] > target:
                break
            # 跳过重复的数字，避免生成重复组合
            if i > start and candidates[i] == candidates[i - 1]:    # 每次收录时都检查是不是和前一个重复了 遍历一遍肯定不会重复
                continue
            # 递归调用，注意 i + 1 表示每个数字只能使用一次
            backtrack(i + 1, path + [candidates[i]], target - candidates[i])

    backtrack(0, [], target)
    return result

def run_tests():
    def check_result(result, expected):
        # 排序以便于比较
        res_sorted = sorted([sorted(comb) for comb in result])
        exp_sorted = sorted([sorted(comb) for comb in expected])
        assert res_sorted == exp_sorted, f"Expected {expected}, but got {result}"

    check_result(
        combination_sum2([10, 1, 2, 7, 6, 1, 5], 8),
        [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    )
    check_result(
        combination_sum2([2, 5, 2, 1, 2], 5),
        [[1, 2, 2], [5]]
    )
    check_result(
        combination_sum2([2], 1),
        []
    )
    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
