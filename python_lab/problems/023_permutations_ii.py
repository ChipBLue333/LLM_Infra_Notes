"""
Problem 023: Permutations II

Difficulty:
Medium

Topic:
Backtracking / DFS / Array

Description:
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

Input:
nums: List[int] - 包含重复元素的整数列表

Output:
List[List[int]] - 所有不重复的全排列

Examples:
Example 1:
Input: nums = [1, 1, 2]
Output:
[[1, 1, 2],
 [1, 2, 1],
 [2, 1, 1]]

Example 2:
Input: nums = [1, 2, 3]
Output:
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

Constraints:
- 1 <= nums.length <= 8
- -10 <= nums[i] <= 10

Task:
实现 permute_unique(nums) 函数。

说明与挑战：
1. 本题是全排列（Permutations）加上含重复元素的去重。请思考：全排列去重跟组合去重在 `for` 循环中有什么细微区别？（同样需要先排序）。
2. 【进阶挑战】请在这道题中，尝试使用刚刚讲过的重点：**“显式回溯”**。
   - 使用全局共享的 `path` 列表；
   - 每次做选择时 `path.append(...)`；
   - 递归返回时 `path.pop(...)`；
   - 保存结果时 `result.append(path.copy())`。
   - 同样也需要一个共享的 `used` 数组来做全排列的防重选。
"""

from typing import List

def permute_unique(nums: List[int]) -> List[List[int]]:
    # TODO: implement here
    # 先对nums进行排序，方便后续剪枝和去重
    nums.sort()
    result = []
    used = [False] * len(nums)  # 用于标记元素是否被使用过
    path = []  # 当前的排列路径
    # 定义回溯函数
    def backtrack():
        # 如果当前路径的长度等于输入数组的长度，说明找到了一个完整的排列
        if len(path) == len(nums):
            result.append(path.copy())
            return
        for i in range(len(nums)):
            # 如果当前元素已经被使用过，跳过
            if used[i]:
                continue
            # 如果当前元素和前一个元素相同，并且前一个元素没有被使用过，跳过（避免重复排列）
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue
            # 做选择
            used[i] = True
            path.append(nums[i])
            # 递归回溯
            backtrack()
            # 撤销选择
            path.pop()
            used[i] = False
    backtrack()
    return result   


def run_tests():
    def check_result(result, expected):
        # 排列题因为内部顺序不能破坏，所以只能对外部的整体列表进行排序后比较
        res_sorted = sorted(result)
        exp_sorted = sorted(expected)
        assert res_sorted == exp_sorted, f"Expected {expected}, but got {result}"

    check_result(
        permute_unique([1, 1, 2]),
        [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
    )
    check_result(
        permute_unique([1, 2, 3]),
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    )
    check_result(
        permute_unique([1, 1]),
        [[1, 1]]
    )
    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
