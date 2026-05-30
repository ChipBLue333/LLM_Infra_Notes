"""
Problem 059: Meeting Rooms II

Difficulty:
Medium

Topic:
Array / Sorting / Heap / Intervals

Description:
给定一个会议时间列表 intervals，其中 intervals[i] = [start_i, end_i]，
表示一个会议从 start_i 开始，到 end_i 结束。

请返回安排所有会议所需的最少会议室数量。

注意：
如果一个会议在时间 t 结束，另一个会议也在时间 t 开始，
它们可以使用同一个会议室。

Input:
intervals: List[List[int]] - 每个元素表示一个会议的开始时间和结束时间

Output:
int - 最少需要的会议室数量

Examples:
Example 1:
Input:
intervals = [[0, 30], [5, 10], [15, 20]]
Output:
2
Explanation:
[5, 10] 和 [15, 20] 可以共用一个会议室，但 [0, 30] 会一直占用另一个会议室。

Example 2:
Input:
intervals = [[7, 10], [2, 4]]
Output:
1
Explanation:
两个会议没有时间重叠，只需要一个会议室。

Example 3:
Input:
intervals = [[1, 5], [5, 8], [8, 10]]
Output:
1
Explanation:
会议结束时间等于下一个会议开始时间时，可以复用同一个会议室。

Constraints:
- 0 <= len(intervals) <= 100000
- intervals[i].length == 2
- 0 <= start_i < end_i <= 1000000

Task:
实现 min_meeting_rooms(intervals) 函数。

要求：
1. 不要用暴力两两比较。
2. 推荐先按会议开始时间排序。
3. 推荐使用最小堆维护当前正在使用的会议室结束时间。

提示：
- 最小堆里可以存“当前每个会议室正在进行的会议结束时间”。
- 处理一个新会议时，先看最早结束的会议室能不能复用。
- 如果 earliest_end <= current_start，说明这个会议室可以复用。
- 否则需要新增一个会议室。
"""

from typing import List
import heapq

def min_meeting_rooms(intervals: List[List[int]]) -> int:
    # 按时间排序
    intervals.sort(key=lambda x: x[0])
    # 创建最小堆 rooms

    rooms = []
    for start, end in intervals:
        # 如果 rooms 不空，且最早结束的会议室可以复用
        if rooms and rooms[0] <= start:
            # 弹出最早结束的会议室
            heapq.heappop(rooms)
        # 无论复用与否，都要把当前会议的结束时间加入堆
        heapq.heappush(rooms, end)
    # 堆的大小就是需要的会议室数量
    return len(rooms)


def run_tests():
    assert min_meeting_rooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert min_meeting_rooms([[7, 10], [2, 4]]) == 1
    assert min_meeting_rooms([[1, 5], [5, 8], [8, 10]]) == 1
    assert min_meeting_rooms([]) == 0
    assert min_meeting_rooms([[1, 10]]) == 1
    assert min_meeting_rooms([[1, 4], [2, 5], [3, 6]]) == 3
    assert min_meeting_rooms([[1, 3], [3, 6], [4, 7], [6, 8]]) == 2
    assert min_meeting_rooms([[5, 10], [0, 30], [15, 20], [20, 25]]) == 2

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
