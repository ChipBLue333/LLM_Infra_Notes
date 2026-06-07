"""
Problem 055: Non-overlapping Intervals

Difficulty:
Medium

Topic:
Array / Sorting / Greedy / Intervals

Description:
给定一个区间列表 intervals，其中 intervals[i] = [start_i, end_i]。

你需要移除尽可能少的区间，使得剩下的区间互不重叠。

请返回需要移除的最少区间数量。

注意：
如果一个区间的结束位置等于另一个区间的开始位置，不算重叠。
例如 [1, 2] 和 [2, 3] 可以同时保留。

Input:
intervals: List[List[int]] - 一个二维列表，每个元素表示一个闭区间的起点和终点

Output:
int - 为了让剩余区间互不重叠，需要移除的最少区间数量

Examples:
Example 1:
Input:
intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
Output:
1
Explanation:
移除 [1, 3] 后，剩下的区间互不重叠。

Example 2:
Input:
intervals = [[1, 2], [1, 2], [1, 2]]
Output:
2
Explanation:
三个区间两两重叠，最多只能保留一个，所以需要移除两个。

Example 3:
Input:
intervals = [[1, 2], [2, 3]]
Output:
0
Explanation:
两个区间边界相接，不算重叠，无需移除。

Constraints:
- 1 <= len(intervals) <= 100000
- intervals[i].length == 2
- -50000 <= start_i < end_i <= 50000

Task:
实现 erase_overlap_intervals(intervals) 函数。

要求：
1. 返回最少需要移除的区间数量。
2. 推荐先对区间排序，再使用贪心策略扫描。
3. 不要暴力枚举所有区间组合。

提示：
- 这题可以反过来思考：最少移除 = 总区间数 - 最多能保留的不重叠区间数。
- 如果想保留尽可能多的区间，通常应该优先保留结束位置更早的区间。
- 扫描时可以维护“当前已保留区间的最右结束位置”。
"""

from typing import List


def erase_overlap_intervals(intervals: List[List[int]]) -> int:
    # 先排序结束位置end
    intervals.sort(key=lambda x: x[1])
    count = 0
    prev_end = float('-inf')
    for start, end in intervals:
        if start >= prev_end:
            # 不重叠，保留这个区间
            prev_end = end
        else:
            # 重叠了，需要移除这个区间
            count += 1
    return count



def run_tests():
    assert erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert erase_overlap_intervals([[1, 2], [1, 2], [1, 2]]) == 2
    assert erase_overlap_intervals([[1, 2], [2, 3]]) == 0
    assert erase_overlap_intervals([[1, 100], [11, 22], [1, 11], [2, 12]]) == 2
    assert erase_overlap_intervals([[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]]) == 2
    assert erase_overlap_intervals([[-10, -1], [-5, 0], [0, 3], [3, 4]]) == 1
    assert erase_overlap_intervals([[5, 6]]) == 0

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
