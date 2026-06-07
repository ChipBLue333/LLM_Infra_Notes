"""
Problem 027: Palindrome Partitioning

Difficulty:
Medium

Topic:
Backtracking / DFS / String

Description:
给定一个字符串 s，将 s 分割成若干个非空子串，使得每个子串都是回文串。

返回所有可能的分割方案。

回文串指正着读和反着读都相同的字符串。例如：
- "a" 是回文串
- "aa" 是回文串
- "aba" 是回文串
- "ab" 不是回文串

Input:
s: str - 一个由小写英文字母组成的字符串

Output:
List[List[str]] - 所有可能的回文分割方案

Examples:
Example 1:
Input:
s = "aab"
Output:
[["a", "a", "b"], ["aa", "b"]]

Example 2:
Input:
s = "a"
Output:
[["a"]]

Example 3:
Input:
s = "efe"
Output:
[["e", "f", "e"], ["efe"]]

Constraints:
- 1 <= len(s) <= 16
- s 只包含小写英文字母

Task:
实现 partition(s) 函数。

要求：
1. 使用回溯算法。
2. 需要自己写一个辅助函数判断子串是否为回文串。
3. 不要使用动态规划预处理回文表，本题先训练基础切割型回溯。
4. 思考：
   - 当前递归状态应该表示“从 s 的哪个下标开始继续切割”？
   - 每一层可以选择哪些结束位置？
   - 什么时候说明整条切割路径已经完成？
"""

from typing import List



def partition(s: str) -> List[List[str]]:
    # TODO: implement here
    # 如果当前字符串为空，说明切割完成，返回一个包含空列表的列表
    if not s:
        return [[]]
    result = []

    def is_palindrome(text: str) -> bool:
        return text == text[::-1]

    def backtrack(start: int, path: List[str]):
        # 如果当前路径的起始位置已经超过字符串长度，说明切割完成，添加当前路径到结果中
        if start >= len(s):
            result.append(path.copy())
            return
        # 从当前起始位置继续切割到每个可能的位置
        for j in range(start + 1, len(s) + 1):
            next_substring = s[start:j]
            if is_palindrome(next_substring):
                path.append(next_substring)
                backtrack(j, path)
                path.pop()

    backtrack(0, [])
    return result





def run_tests():
    result = partition("aab")
    expected = [["a", "a", "b"], ["aa", "b"]]
    assert sorted(result) == sorted(expected)

    assert partition("a") == [["a"]]

    result = partition("efe")
    expected = [["e", "f", "e"], ["efe"]]
    assert sorted(result) == sorted(expected)

    result = partition("aaa")
    expected = [
        ["a", "a", "a"],
        ["a", "aa"],
        ["aa", "a"],
        ["aaa"],
    ]
    assert sorted(result) == sorted(expected)

    result = partition("abc")
    expected = [["a", "b", "c"]]
    assert sorted(result) == sorted(expected)

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
