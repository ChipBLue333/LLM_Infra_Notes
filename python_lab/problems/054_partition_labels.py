"""
Problem 054: Partition Labels

Difficulty:
Medium

Topic:
String / Hash Map / Greedy

Description:
给定一个字符串 s，请你把它划分成尽可能多的片段，使得每个字母最多只出现在一个片段中。

也就是说，同一个字符不能同时出现在两个不同的片段里。

请返回一个列表，表示每个片段的长度。

Input:
s: str - 只包含小写英文字母的字符串

Output:
list[int] - 每个划分片段的长度

Examples:
Example 1:
Input:
s = "ababcbacadefegdehijhklij"
Output:
[9, 7, 8]
Explanation:
划分结果为 "ababcbaca"、"defegde"、"hijhklij"。
每个字母都只出现在一个片段中。

Example 2:
Input:
s = "eccbbbbdec"
Output:
[10]
Explanation:
字符之间互相牵连，整个字符串只能作为一个片段。

Example 3:
Input:
s = "abc"
Output:
[1, 1, 1]
Explanation:
每个字符只出现一次，可以分成三个片段。

Constraints:
- 1 <= len(s) <= 500
- s 只包含小写英文字母

Task:
实现 partition_labels(s) 函数。

要求：
1. 返回每个片段的长度。
2. 推荐使用哈希表记录每个字符最后一次出现的位置。
3. 不要暴力枚举所有切分方式。

提示：
- 一个片段如果包含字符 c，那么这个片段必须覆盖到 c 最后一次出现的位置。
- 从左到右扫描时，维护当前片段必须到达的最远下标。
- 当当前位置等于这个最远下标时，说明当前片段可以结束。
"""

from typing import List


def partition_labels(s: str) -> List[int]:
    # TODO: implement here
    # 先确定每个字符最后一次出现的位置
    last = {}
    for i, char in enumerate(s):
        last[char] = i
    # 从左到右扫描，维护当前片段必须到达的最远下标
    partitions = []
    end = 0
    start = 0
    for i, char in enumerate(s):
        end = max(end, last[char])
        if i == end:
            partitions.append(end - start + 1)
            start = i + 1
    return partitions



def run_tests():
    assert partition_labels("ababcbacadefegdehijhklij") == [9, 7, 8]
    assert partition_labels("eccbbbbdec") == [10]
    assert partition_labels("abc") == [1, 1, 1]
    assert partition_labels("aaa") == [3]
    assert partition_labels("abac") == [3, 1]
    assert partition_labels("caedbdedda") == [1, 9]
    assert partition_labels("q") == [1]

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
