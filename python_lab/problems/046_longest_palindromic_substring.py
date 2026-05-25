"""
Problem 046: Longest Palindromic Substring

Difficulty:
Medium

Topic:
String / Dynamic Programming / Two Pointers

Description:
给定一个字符串 `s`，返回 `s` 中最长的回文子串。

子串必须是原字符串中连续的一段。
回文字符串是指从左往右读和从右往左读都相同的字符串。

注意：
- 本题要求的是“子串”，必须连续。
- 上一题 Longest Palindromic Subsequence 求的是“子序列”，可以跳过字符。
- 不要把上一题的区间 DP 转移直接搬过来。

Input:
s: str - 一个字符串

Output:
str - `s` 中最长的回文子串

Examples:
Example 1:
Input:
s = "babad"
Output:
"bab"
Explanation:
"aba" 也是合法答案，因为长度同样为 3。

Example 2:
Input:
s = "cbbd"
Output:
"bb"

Example 3:
Input:
s = "a"
Output:
"a"

Constraints:
- 1 <= len(s) <= 1000
- s 只包含英文字母和数字

Task:
实现 longest_palindromic_substring(s) 函数。

要求：
1. 返回最长的回文子串本身，而不是长度。
2. 子串必须连续。
3. 如果存在多个最长答案，返回任意一个都可以。
4. 可以使用中心扩展，也可以使用动态规划。
5. 不要生成所有子串再逐个判断，这样复杂度太高。

提示：
- 回文子串有两种中心：
  1. 单个字符作为中心，例如 "aba"。
  2. 两个字符之间作为中心，例如 "abba"。
- 如果使用中心扩展，需要从中心向左右两边同时扩展。
- 如果使用 DP，可以令 `dp[i][j]` 表示 `s[i:j+1]` 是否是回文子串。
- 子串问题必须保证 `s[i:j+1]` 这一整段连续都是回文。
"""


def longest_palindromic_substring(s: str) -> str:
    # TODO: implement here
    # 定义dp[i][j] 表示s[i:j+1]这个区间内是否是回文子串
    n = len(s)
    dp = [[False] * n for _ in range(n)]    # 初始化都为否
    start = 0
    max_len = 1

    # 填表
    for i in range(n - 1, -1, -1):
        dp[i][i] = True  # 单个字符是回文
        for j in range(i + 1, n):
            if s[i] == s[j]:
                if j - i == 1 or dp[i + 1][j - 1]:  # 如果左右字符相同，并且它们之间的子串也是回文（或者它们相邻），那么s[i:j+1]也是回文
                    dp[i][j] = True
                    if j - i + 1 > max_len: # 如果当前回文子串长度大于之前记录的最大长度，更新最大长度和起始位置
                        max_len = j - i + 1
                        start = i

    return s[start:start + max_len]


def _is_palindrome(value: str) -> bool:
    return value == value[::-1]


def _assert_valid_answer(s: str, answer: str, expected_length: int) -> None:
    assert answer in s
    assert _is_palindrome(answer)
    assert len(answer) == expected_length


def run_tests():
    _assert_valid_answer("babad", longest_palindromic_substring("babad"), 3)
    assert longest_palindromic_substring("cbbd") == "bb"
    assert longest_palindromic_substring("a") == "a"
    _assert_valid_answer("aaaa", longest_palindromic_substring("aaaa"), 4)
    _assert_valid_answer("abcde", longest_palindromic_substring("abcde"), 1)
    _assert_valid_answer("forgeeksskeegfor", longest_palindromic_substring("forgeeksskeegfor"), 10)
    _assert_valid_answer("abacdfgdcaba", longest_palindromic_substring("abacdfgdcaba"), 3)

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
