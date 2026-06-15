/*
Problem 001: 两数之和 (Two Sum)

Difficulty:
Easy

Topic:
Array / Hash Map / std::vector / std::unordered_map

Description:
给定一个整数数组 nums 和一个整数 target，请找出和为 target 的两个元素，
并返回它们的下标。

每组输入恰好存在一个答案，同一个元素不能使用两次。
返回的两个下标顺序不限。

Input:
nums: 整数数组
target: 目标和

Output:
包含两个下标的 std::vector<int>

Examples:
Example 1:
Input:
nums = {2, 7, 11, 15}, target = 9

Output:
{0, 1}

Example 2:
Input:
nums = {3, 2, 4}, target = 6

Output:
{1, 2}

Constraints:
- 2 <= nums.size() <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- 每组输入恰好存在一个答案

Task:
实现 two_sum 函数。

要求:
1. 目标时间复杂度为 O(n)。
2. 使用 std::unordered_map 记录已经遍历过的数字及其下标。
3. 不允许使用双层循环暴力枚举。
4. 不要修改 nums。
5. 函数参数应避免不必要地复制整个数组。

思考:
- nums 为什么适合通过 const 引用传入？
- unordered_map 应该保存“数字到下标”还是“下标到数字”？
- 为什么应该先查找 complement，再保存当前数字？
- nums 中有重复数字时，怎样避免使用同一个元素两次？
*/

#include <cassert>
#include <cstddef>
#include <iostream>
#include <unordered_map>
#include <vector>


std::vector<int> two_sum(const std::vector<int>& nums, int target) {
    // TODO: 使用一次遍历和 std::unordered_map 完成实现
    return {};
}


void assert_valid_answer(
    const std::vector<int>& nums,
    int target,
    const std::vector<int>& answer
) {
    assert(answer.size() == 2);

    const int first = answer[0];
    const int second = answer[1];

    assert(first >= 0);
    assert(second >= 0);
    assert(static_cast<std::size_t>(first) < nums.size());
    assert(static_cast<std::size_t>(second) < nums.size());
    assert(first != second);
    assert(nums[static_cast<std::size_t>(first)]
        + nums[static_cast<std::size_t>(second)] == target);
}


void run_tests() {
    assert_valid_answer({2, 7, 11, 15}, 9, two_sum({2, 7, 11, 15}, 9));
    assert_valid_answer({3, 2, 4}, 6, two_sum({3, 2, 4}, 6));
    assert_valid_answer({3, 3}, 6, two_sum({3, 3}, 6));
    assert_valid_answer({-3, 4, 3, 90}, 0, two_sum({-3, 4, 3, 90}, 0));
    assert_valid_answer({0, 4, 3, 0}, 0, two_sum({0, 4, 3, 0}, 0));

    std::cout << "All tests passed!\n";
}


int main() {
    run_tests();
    return 0;
}
