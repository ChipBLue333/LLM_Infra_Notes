"""
Problem 057: Merge Intervals

Difficulty:
Medium

Topic:
Array / Sorting / Intervals

Description:
给定一个区间列表 intervals，其中 intervals[i] = [start_i, end_i]。

请合并所有重叠的区间，并返回一个不重叠的区间列表。
返回结果中的区间应覆盖原始输入中所有区间的范围。

注意：
如果两个区间边界相接，也应该合并。
例如 [1, 4] 和 [4, 5] 合并后是 [1, 5]。

Input:
intervals: List[List[int]] - 一个二维列表，每个元素表示一个区间的起点和终点

Output:
List[List[int]] - 合并后的不重叠区间列表

Examples:
Example 1:
Input:
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
Output:
[[1, 6], [8, 10], [15, 18]]
Explanation:
[1, 3] 和 [2, 6] 重叠，合并为 [1, 6]。

Example 2:
Input:
intervals = [[1, 4], [4, 5]]
Output:
[[1, 5]]
Explanation:
两个区间边界相接，也需要合并。

Example 3:
Input:
intervals = [[1, 4], [0, 2], [3, 5]]
Output:
[[0, 5]]
Explanation:
排序后所有区间可以合并成一个大区间。

Constraints:
- 1 <= len(intervals) <= 100000
- intervals[i].length == 2
- 0 <= start_i <= end_i <= 100000

Task:
实现 merge_intervals(intervals) 函数。

要求：
1. 返回合并后的区间列表。
2. 推荐先按区间起点排序。
3. 不要使用暴力两两合并。

提示：
- 先按 start 从小到大排序。
- 维护一个结果列表 merged。
- 当前区间如果和 merged 的最后一个区间重叠，就更新最后一个区间的 end。
- 如果不重叠，就把当前区间作为新区间加入结果。
"""

from typing import List


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    # 按区间起点排序
    intervals.sort(key=lambda x: x[0])
    merged = []  # 存储合并后的区间
    # last是merged中最后一个区间
    last = None
    for interval in intervals:
        if not last or last[1] < interval[0]:  # 没有重叠
            merged.append(interval)
            last = interval # 更新last为当前区间
        else:  # 有重叠，更新last的end
            last[1] = max(last[1], interval[1])
    return merged


def run_tests():
    assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [
        [1, 6],
        [8, 10],
        [15, 18],
    ]
    assert merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]
    assert merge_intervals([[1, 4], [0, 2], [3, 5]]) == [[0, 5]]
    assert merge_intervals([[1, 4]]) == [[1, 4]]
    assert merge_intervals([[1, 4], [5, 6]]) == [[1, 4], [5, 6]]
    assert merge_intervals([[1, 10], [2, 3], [4, 5], [6, 7]]) == [[1, 10]]
    assert merge_intervals([[5, 7], [1, 3], [2, 4], [8, 9]]) == [
        [1, 4],
        [5, 7],
        [8, 9],
    ]

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
