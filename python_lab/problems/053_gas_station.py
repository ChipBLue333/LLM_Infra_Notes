"""
Problem 053: Gas Station

Difficulty:
Medium

Topic:
Array / Greedy

Description:
有一圈加油站，第 i 个加油站有 gas[i] 升汽油。

你有一辆油箱容量无限的车，从第 i 个加油站开到第 i + 1 个加油站需要消耗 cost[i] 升汽油。
最后一个加油站之后会回到第一个加油站。

请判断是否存在一个起始加油站下标，使得你从那里出发，可以绕环路行驶一圈并回到起点。
如果存在，返回这个起始下标；如果不存在，返回 -1。

题目保证如果答案存在，则答案唯一。

Input:
gas: list[int] - 每个加油站可获得的汽油量
cost: list[int] - 从当前位置开到下一个位置需要消耗的汽油量

Output:
int - 可行的起始加油站下标；如果不存在，返回 -1

Examples:
Example 1:
Input:
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
Output:
3
Explanation:
从下标 3 出发：
获得 4 升，去下标 4 消耗 1 升，剩余 3 升；
获得 5 升，去下标 0 消耗 2 升，剩余 6 升；
获得 1 升，去下标 1 消耗 3 升，剩余 4 升；
获得 2 升，去下标 2 消耗 4 升，剩余 2 升；
获得 3 升，去下标 3 消耗 5 升，剩余 0 升。

Example 2:
Input:
gas = [2, 3, 4]
cost = [3, 4, 3]
Output:
-1
Explanation:
无论从哪个加油站出发，都无法绕行一圈。

Example 3:
Input:
gas = [5]
cost = [4]
Output:
0
Explanation:
只有一个加油站，汽油足够完成一圈。

Constraints:
- len(gas) == len(cost)
- 1 <= len(gas) <= 10^5
- 0 <= gas[i], cost[i] <= 10^4
- 如果答案存在，则答案唯一

Task:
实现 can_complete_circuit(gas, cost) 函数。

要求：
1. 返回可行的起始下标；如果不存在，返回 -1。
2. 推荐使用 O(n) 贪心解法。
3. 不要对每个起点都模拟一整圈，这会导致 O(n^2)。

提示：
- 先思考一个全局条件：总汽油量是否至少等于总消耗量。
- 再思考局部条件：如果从某个起点出发，走到 i 时油量变成负数，说明这个起点不可行。
- 更进一步：当局部油量变成负数时，当前起点到 i 之间的所有位置都不能作为答案。
"""

from typing import List


def can_complete_circuit(gas: List[int], cost: List[int]) -> int:
    # TODO: implement here
    # 计算总汽油量和总消耗量
    total_gas = sum(gas)
    total_cost = sum(cost)
    # 如果总汽油量小于总消耗量，直接返回 -1
    if total_gas < total_cost:
        return -1  
    # 遍历每一个起点
    start = 0
    current_gas = 0
    for i in range(len(gas)):
        current_gas += gas[i] - cost[i]
        # 如果当前油量变成负数，说明这个起点不可行
        if current_gas < 0:
            # 将起点移动到下一个位置
            start = i + 1
            current_gas = 0  # 重置当前油量
    return start  # 返回可行的起始下标  


def run_tests():
    assert can_complete_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
    assert can_complete_circuit([2, 3, 4], [3, 4, 3]) == -1
    assert can_complete_circuit([5], [4]) == 0
    assert can_complete_circuit([1], [2]) == -1
    assert can_complete_circuit([3, 1, 1], [1, 2, 2]) == 0
    assert can_complete_circuit([4, 5, 2, 6, 5, 3], [3, 2, 7, 3, 2, 9]) == -1
    assert can_complete_circuit([2, 0, 1, 2, 3, 4, 0], [0, 1, 0, 0, 0, 0, 11]) == 0

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
