"""
Problem 065: Find Median from Data Stream

Difficulty:
Medium

Topic:
Heap / Design / Data Stream

Description:
设计一个 MedianFinder 类，用来持续接收整数，并在任意时刻返回当前所有数字的中位数。

中位数定义：
- 如果数字个数是奇数，中位数是排序后位于正中间的数字。
- 如果数字个数是偶数，中位数是排序后中间两个数字的平均值。

你需要支持两个操作：
1. add_num(num): 向数据流中加入一个整数。
2. find_median(): 返回当前所有数字的中位数。

Input:
一系列 add_num 和 find_median 操作。

Output:
find_median 返回 float 类型的中位数。

Examples:
Example 1:
Input:
mf = MedianFinder()
mf.add_num(1)
mf.add_num(2)
mf.find_median()
mf.add_num(3)
mf.find_median()
Output:
1.5
2.0

Example 2:
Input:
mf = MedianFinder()
mf.add_num(-1)
mf.add_num(-2)
mf.add_num(-3)
mf.find_median()
Output:
-2.0

Constraints:
- -100000 <= num <= 100000
- add_num 至少会在 find_median 之前调用一次
- 操作次数最多为 50000

Task:
实现 MedianFinder 类。

要求：
1. 使用 heapq。
2. 不要每次 find_median 都整体排序。
3. 用两个堆维护较小的一半和较大的一半。
4. add_num 的时间复杂度目标是 O(log n)。
5. find_median 的时间复杂度目标是 O(1)。

提示：
- Python 的 heapq 是最小堆。
- 可以用负数模拟最大堆。
- 一个堆保存较小的一半数字，另一个堆保存较大的一半数字。
- 保持两个堆的大小差不超过 1。
"""

import heapq


class MedianFinder:
    def __init__(self):
        # 定义两个堆：一个最大堆（用负数模拟）保存较小的一半数字，一个最小堆保存较大的一半数字
        self.small = []  # 最大堆，存储较小的一半数字（用负数模拟）
        self.large = []  # 最小堆，存储较大的一半数字


    def add_num(self, num: int) -> None:
        # 数据入堆
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)  # 加入最大堆
        else:
            heapq.heappush(self.large, num)  # 加入最小堆

        # 平衡两个堆的大小
        # 如果最大堆的元素比最小堆多超过1个，将最大堆的堆顶元素移动到最小堆
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        # 如果最小堆的元素比最大堆多，将最小堆的堆顶元素移动到最大堆
        elif len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))


    def find_median(self) -> float:

        # 计算中位数
        if len(self.small) > len(self.large):
            return float(-self.small[0])  # 最大堆顶元素是较小的一半的最大值
        else:
            return (-self.small[0] + self.large[0]) / 2.0  # 两个堆顶元素的平均值


def run_tests():
    mf = MedianFinder()
    mf.add_num(1)
    mf.add_num(2)
    assert mf.find_median() == 1.5
    mf.add_num(3)
    assert mf.find_median() == 2.0

    mf = MedianFinder()
    mf.add_num(-1)
    mf.add_num(-2)
    mf.add_num(-3)
    assert mf.find_median() == -2.0

    mf = MedianFinder()
    mf.add_num(5)
    assert mf.find_median() == 5.0
    mf.add_num(15)
    assert mf.find_median() == 10.0
    mf.add_num(1)
    assert mf.find_median() == 5.0
    mf.add_num(3)
    assert mf.find_median() == 4.0

    mf = MedianFinder()
    for num in [2, 2, 2, 2]:
        mf.add_num(num)
    assert mf.find_median() == 2.0

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
