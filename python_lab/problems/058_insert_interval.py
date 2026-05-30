"""
Problem 058: Insert Interval

Difficulty:
Medium

Topic:
Array / Intervals

Description:
给定一个已经按起点升序排列、且内部没有重叠的区间列表 intervals，
再给定一个新区间 new_interval。

请将 new_interval 插入到 intervals 中，并在必要时合并重叠区间。
返回插入并合并后的区间列表。

注意：
1. intervals 已经按 start 升序排列。
2. intervals 内部原本不重叠。
3. 如果两个区间边界相接，也应该合并。
   例如 [1, 3] 和 [3, 5] 合并后是 [1, 5]。

Input:
intervals: List[List[int]] - 已排序、无重叠的区间列表
new_interval: List[int] - 需要插入的新区间

Output:
List[List[int]] - 插入并合并后的区间列表

Examples:
Example 1:
Input:
intervals = [[1, 3], [6, 9]]
new_interval = [2, 5]
Output:
[[1, 5], [6, 9]]
Explanation:
[2, 5] 和 [1, 3] 重叠，合并成 [1, 5]。

Example 2:
Input:
intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
new_interval = [4, 8]
Output:
[[1, 2], [3, 10], [12, 16]]
Explanation:
[4, 8] 会和 [3, 5]、[6, 7]、[8, 10] 连续合并。

Example 3:
Input:
intervals = []
new_interval = [5, 7]
Output:
[[5, 7]]

Constraints:
- 0 <= len(intervals) <= 100000
- intervals[i].length == 2
- new_interval.length == 2
- 0 <= start_i <= end_i <= 100000
- 0 <= new_start <= new_end <= 100000
- intervals 按 start 升序排列，且互不重叠

Task:
实现 insert_interval(intervals, new_interval) 函数。

要求：
1. 不要先把 new_interval 加进去再整体排序。
2. 尽量使用一次线性扫描完成。
3. 可以创建新的结果列表。

提示：
- 可以把原区间分成三类：完全在新区间左边、和新区间有重叠、完全在新区间右边。
- 重叠时，需要不断扩展 new_interval 的左右边界。
- 找到第一个完全在新区间右边的区间后，剩余区间可以直接加入结果。
"""

from typing import List


def insert_interval(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    result = []
    inserted = False
    for interval in intervals:
        if interval[1] < new_interval[0]:  # 完全在新区间左边
            result.append(interval)
        elif interval[0] > new_interval[1]:  # 完全在新区间右边
            if not inserted:
                result.append(new_interval)
                inserted = True
                result.append(interval)
            else:
                result.append(interval)
        else:  # 和新区间有重叠
            new_interval[0] = min(new_interval[0], interval[0])
            new_interval[1] = max(new_interval[1], interval[1])
    if not inserted:
        result.append(new_interval)

    return result

def run_tests():
    assert insert_interval([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert insert_interval(
        [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
        [4, 8],
    ) == [[1, 2], [3, 10], [12, 16]]
    assert insert_interval([], [5, 7]) == [[5, 7]]
    assert insert_interval([[1, 5]], [2, 3]) == [[1, 5]]
    assert insert_interval([[1, 5]], [6, 8]) == [[1, 5], [6, 8]]
    assert insert_interval([[1, 2], [8, 10]], [3, 7]) == [[1, 2], [3, 7], [8, 10]]
    assert insert_interval([[3, 5], [8, 10]], [1, 2]) == [[1, 2], [3, 5], [8, 10]]
    assert insert_interval([[1, 2], [3, 5]], [6, 7]) == [[1, 2], [3, 5], [6, 7]]

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
