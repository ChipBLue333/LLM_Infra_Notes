"""
Problem 072: Alien Dictionary

Difficulty:
Medium

Topic:
Graph / Topological Sort / String

Description:
某个外星语言使用英文字母小写字符，但字符之间的字典序规则和普通英语不同。

给定一个按外星语言字典序排序好的单词列表 words，请根据这些单词推断出一种可能的字符顺序。

如果存在多个合法字符顺序，返回任意一种即可。
如果无法推断出合法顺序，请返回空字符串 ""。

注意：
- 所有出现在 words 中的字符都必须出现在返回结果中。
- 如果一个较长单词排在它自己的前缀单词之前，例如 "abc" 在 "ab" 前面，
  那么这个输入是非法的，应返回 ""。

Input:
words: List[str] - 已经按照外星语言字典序排序的单词列表

Output:
str - 一种合法的外星字符顺序；如果不存在合法顺序，返回 ""

Examples:
Example 1:
Input:
words = ["wrt", "wrf", "er", "ett", "rftt"]
Output:
"wertf"
Explanation:
从 "wrt" 和 "wrf" 可知 t < f。
从 "wrf" 和 "er" 可知 w < e。
从 "er" 和 "ett" 可知 r < t。
从 "ett" 和 "rftt" 可知 e < r。
因此一种合法顺序是 "wertf"。

Example 2:
Input:
words = ["z", "x"]
Output:
"zx"
Explanation:
从两个单词可知 z < x。

Example 3:
Input:
words = ["z", "x", "z"]
Output:
""
Explanation:
可以推出 z < x，同时又推出 x < z，形成环，因此没有合法顺序。

Example 4:
Input:
words = ["abc", "ab"]
Output:
""
Explanation:
"ab" 是 "abc" 的前缀，但较长单词 "abc" 排在前面，输入非法。

Constraints:
- 1 <= len(words) <= 100
- 1 <= len(words[i]) <= 100
- words[i] 只包含小写英文字母

Task:
实现 alien_order(words) 函数。

要求：
1. 先收集所有出现在 words 中的字符。
2. 比较相邻两个单词，找到第一对不同字符 first 和 second。
3. 如果 first != second，说明 first 必须排在 second 前面，建立 first -> second 的边。
4. 使用入度 indegree 记录每个字符有多少前置依赖。
5. 使用拓扑排序生成字符顺序。
6. 如果最终结果长度不等于字符总数，说明存在环，返回 ""。

提示：
- 只需要比较相邻单词，不需要比较所有单词对。
- 对一对相邻单词，只看第一处不同字符，后面的字符不能提供顺序信息。
- 建图时要避免重复边，否则入度会被重复增加。
- 前缀非法情况需要在建边前单独判断。
"""

from collections import deque
from typing import List


def alien_order(words: List[str]) -> str:
    # 记录所有字符
    chars = set("".join(words))
    # 比较相邻单词，建立图和入度
    graph = {char: set() for char in chars}
    indegree = {char: 0 for char in chars} 
    for first_word, second_word in zip(words, words[1:]):
        min_len = min(len(first_word), len(second_word))
        # 前缀非法情况
        if len(first_word) > len(second_word) and first_word[:min_len] == second_word[:min_len]:
            return ""

        for i in range(min_len):
            if first_word[i] != second_word[i]:
                if second_word[i] not in graph[first_word[i]]:
                    graph[first_word[i]].add(second_word[i])
                    indegree[second_word[i]] += 1
                break
    # 拓扑排序
    queue = deque([char for char in chars if indegree[char] == 0])
    result = []
    while queue:
        char = queue.popleft()
        result.append(char)
        for neighbor in graph[char]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    # 如果结果长度不等于字符总数，说明存在环
    if len(result) != len(chars):
        return ""
    return "".join(result)  


def is_valid_alien_order(order: str, words: List[str]) -> bool:
    chars = set("".join(words))
    if set(order) != chars or len(order) != len(chars):
        return False

    rank = {char: index for index, char in enumerate(order)}

    for first_word, second_word in zip(words, words[1:]):
        min_len = min(len(first_word), len(second_word))

        if (
            len(first_word) > len(second_word)
            and first_word[:min_len] == second_word[:min_len]
        ):
            return False

        for i in range(min_len):
            if first_word[i] != second_word[i]:
                if rank[first_word[i]] > rank[second_word[i]]:
                    return False
                break

    return True


def run_tests():
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    assert is_valid_alien_order(alien_order(words), words)

    words = ["z", "x"]
    assert alien_order(words) == "zx"

    assert alien_order(["z", "x", "z"]) == ""
    assert alien_order(["abc", "ab"]) == ""

    words = ["za", "zb", "ca", "cb"]
    assert is_valid_alien_order(alien_order(words), words)

    words = ["abc"]
    assert is_valid_alien_order(alien_order(words), words)

    words = ["ab", "adc"]
    assert is_valid_alien_order(alien_order(words), words)

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
