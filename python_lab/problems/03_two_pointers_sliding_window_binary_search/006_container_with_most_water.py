"""
Problem 006: Container With Most Water

Difficulty:
Medium

Topic:
Array / Two Pointers

Description:
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
返回容器可以储存的最大水量。
说明：你不能倾斜容器。

Input:
height: list[int] - 一个整数数组，代表垂线的高度。

Output:
int - 可以储存的最大水量。

Examples:
Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4

Task:
实现 max_area(height) 函数。
"""

from typing import List

def max_area(height: List[int]) -> int:
    # TODO: implement here
    # 接水体积是 min(height[left], height[right]) * (right - left)
    left, right = 0, len(height) - 1 # 双指针 左指针指向数组开头，右指针指向数组结尾
    max_water = 0 # 初始化最大水量为0
    while left < right: # 当左指针小于右指针时继续循环
        # 计算当前水量
        current_water = min(height[left], height[right]) * (right - left)
        max_water = max(max_water, current_water) # 更新最大水量
        # 移动较短的指针
        if height[left] < height[right]:
            left += 1 # 左指针向右移动
        else:
            right -= 1 # 右指针向左移动
    return max_water

def run_tests():
    assert max_area([1,8,6,2,5,4,8,3,7]) == 49
    assert max_area([1,1]) == 1
    assert max_area([4,3,2,1,4]) == 16
    assert max_area([1,2,1]) == 2
    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
