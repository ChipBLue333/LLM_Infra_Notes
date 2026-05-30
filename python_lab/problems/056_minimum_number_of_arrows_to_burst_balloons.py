"""
Problem 056: Minimum Number of Arrows to Burst Balloons

Difficulty:
Medium

Topic:
Array / Sorting / Greedy / Intervals

Description:
有一些气球贴在一面二维墙上，每个气球用一个区间 points[i] = [x_start, x_end] 表示。
这个区间表示气球在 x 轴上覆盖的水平范围。

你可以从任意 x 坐标垂直射出一支箭。
如果一支箭的 x 坐标满足 x_start <= x <= x_end，那么这支箭可以射爆该气球。

请返回射爆所有气球所需的最少箭数。

Input:
points: List[List[int]] - 每个元素是一个气球的起点和终点坐标

Output:
int - 射爆所有气球所需的最少箭数

Examples:
Example 1:
Input:
points = [[10, 16], [2, 8], [1, 6], [7, 12]]
Output:
2
Explanation:
可以在 x = 6 射爆 [2, 8] 和 [1, 6]，在 x = 11 射爆 [10, 16] 和 [7, 12]。

Example 2:
Input:
points = [[1, 2], [3, 4], [5, 6], [7, 8]]
Output:
4
Explanation:
四个气球互不重叠，需要四支箭。

Example 3:
Input:
points = [[1, 2], [2, 3], [3, 4], [4, 5]]
Output:
2
Explanation:
边界相接也可以被同一支箭射爆，例如 x = 2 可以射爆前两个气球。

Constraints:
- 1 <= len(points) <= 100000
- points[i].length == 2
- -2^31 <= x_start < x_end <= 2^31 - 1

Task:
实现 find_min_arrow_shots(points) 函数。

要求：
1. 返回射爆所有气球的最少箭数。
2. 推荐先对区间排序，再使用贪心策略扫描。
3. 不要暴力枚举每一支箭的位置。

提示：
- 这题和“最多保留不重叠区间”很像，但这里是在找最少的箭。
- 一支箭可以覆盖一组互相有交集的气球。
- 可以优先考虑把箭射在当前气球的结束位置。
- 注意：如果下一个气球的 start <= 当前箭的位置，它可以被当前箭射爆。
"""

from typing import List


def find_min_arrow_shots(points: List[List[int]]) -> int:
    # TODO: implement here
    # 尽量找当前未被射爆的气球的右边界 作为箭的位置
    # 排序
    points.sort(key=lambda x: x[1])  # 按照结束位置排序
    arrows = 0
    current_arrow_position = float('-inf')  # 当前箭的位置，初始为负无穷
    for start, end in points:
        # 如果当前气球的起点在当前箭的位置之后，说明需要射一支新箭
        if start > current_arrow_position:
            arrows += 1  # 需要一支新箭
            current_arrow_position = end  # 将箭的位置更新为当前气球的结束位置
    return arrows


def run_tests():
    assert find_min_arrow_shots([[10, 16], [2, 8], [1, 6], [7, 12]]) == 2
    assert find_min_arrow_shots([[1, 2], [3, 4], [5, 6], [7, 8]]) == 4
    assert find_min_arrow_shots([[1, 2], [2, 3], [3, 4], [4, 5]]) == 2
    assert find_min_arrow_shots([[1, 2]]) == 1
    assert find_min_arrow_shots([[1, 10], [2, 9], [3, 8], [4, 7]]) == 1
    assert find_min_arrow_shots([[-5, -1], [-3, 2], [3, 6], [4, 8]]) == 2
    assert find_min_arrow_shots([[1, 5], [6, 10], [2, 6], [7, 12]]) == 2

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
