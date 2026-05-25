"""
Problem 045: Longest Palindromic Subsequence

Difficulty:
Medium

Topic:
Dynamic Programming / String / Interval DP

Description:
给定一个字符串 `s`，返回 `s` 的最长回文子序列长度。

子序列可以通过删除字符串中的某些字符得到，但不能改变剩余字符的相对顺序。
回文字符串是指从左往右读和从右往左读都相同的字符串。

注意：
- 子序列不要求连续。
- 子串要求连续，本题不是求子串。

Input:
s: str - 一个只包含小写英文字母的字符串

Output:
int - 最长回文子序列的长度

Examples:
Example 1:
Input:
s = "bbbab"
Output:
4
Explanation:
最长回文子序列之一是 "bbbb"，长度为 4。

Example 2:
Input:
s = "cbbd"
Output:
2
Explanation:
最长回文子序列之一是 "bb"，长度为 2。

Example 3:
Input:
s = "abcde"
Output:
1
Explanation:
任意单个字符都是长度为 1 的回文子序列。

Constraints:
- 1 <= len(s) <= 1000
- s 只包含小写英文字母

Task:
实现 longest_palindromic_subsequence(s) 函数。

要求：
1. 使用动态规划。
2. 建议使用二维 DP 表。
3. 不要生成所有子序列。
4. 不要把题目当成“最长回文子串”。

提示：
- 可以令 `dp[i][j]` 表示 `s[i:j+1]` 这个区间内的最长回文子序列长度。
- 当 `i == j` 时，单个字符本身就是回文，长度为 1。
- 如果 `s[i] == s[j]`，可以考虑把左右两个字符同时加入答案。
- 如果 `s[i] != s[j]`，需要考虑跳过左边字符或跳过右边字符。
- 注意填表顺序：`dp[i][j]` 可能依赖更短区间。
"""


def longest_palindromic_subsequence(s: str) -> int:
    # TODO: implement here
    # 定义dp[i][j] 表示s[i:j+1]这个区间内的最长回文子序列长度
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    # 填表
    for i in range(n - 1, -1, -1):
        dp[i][i] = 1  # 单个字符是回文，长度为1
        for j in range(i + 1, n):
            if s[i] == s[j]:    # 如果左右字符相同，可以把它们都加入回文子序列
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][n - 1] # 最终答案是整个字符串的最长回文子序列长度 区间最大时


def run_tests():
    assert longest_palindromic_subsequence("bbbab") == 4
    assert longest_palindromic_subsequence("cbbd") == 2
    assert longest_palindromic_subsequence("abcde") == 1
    assert longest_palindromic_subsequence("a") == 1
    assert longest_palindromic_subsequence("aaaa") == 4
    assert longest_palindromic_subsequence("agbdba") == 5
    assert longest_palindromic_subsequence("character") == 5

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
