"""
Problem 043: Longest Common Subsequence

Difficulty:
Medium

Topic:
Dynamic Programming / String / 2D DP

Description:
给定两个字符串 `text1` 和 `text2`，请返回它们的最长公共子序列的长度。

子序列是指从原字符串中删除若干个字符（也可以不删除），
但不改变剩余字符相对顺序后得到的新字符串。

公共子序列是指同时是两个字符串子序列的字符串。

Input:
text1: str - 第一个字符串
text2: str - 第二个字符串

Output:
int - 两个字符串的最长公共子序列长度

Examples:
Example 1:
Input:
text1 = "abcde", text2 = "ace"
Output:
3
Explanation:
最长公共子序列是 "ace"，长度为 3。

Example 2:
Input:
text1 = "abc", text2 = "abc"
Output:
3
Explanation:
两个字符串完全相同，最长公共子序列是 "abc"。

Example 3:
Input:
text1 = "abc", text2 = "def"
Output:
0
Explanation:
两个字符串没有公共字符。

Constraints:
- 1 <= len(text1), len(text2) <= 1000
- text1 和 text2 只包含小写英文字母

Task:
实现 longest_common_subsequence(text1, text2) 函数。

要求：
1. 使用动态规划。
2. 不要使用递归暴力枚举所有子序列。
3. 建议先使用二维 DP 表完成。
4. `dp[i][j]` 可以表示 text1 的前 i 个字符和 text2 的前 j 个字符的最长公共子序列长度。
5. 注意 i、j 和字符串下标之间差 1 的关系。

思考：
- 如果 text1[i - 1] == text2[j - 1]，当前字符能否接在更短前缀的答案后面？
- 如果两个当前字符不相等，应该从哪两个子问题里取较大值？
- 为什么 DP 表通常开成 (len(text1) + 1) * (len(text2) + 1)？
"""


def longest_common_subsequence(text1: str, text2: str) -> int:
    # TODO: implement here
    # 定义dp[i][j] 表示text1的前i个字符和text2的前j个字符的最长公共子序列长度
    m = len(text1)
    n = len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)] # 0行和0列表示空字符串的情况
    # 填充dp表
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]: # 当前字符相等，可以接在前面最长公共子序列后面
                dp[i][j] = dp[i - 1][j - 1] + 1
            else: # 当前字符不相等，取去掉text1当前字符或text2当前字符的较大值
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n] # 最终答案在dp表的右下角


def run_tests():
    assert longest_common_subsequence("abcde", "ace") == 3
    assert longest_common_subsequence("abc", "abc") == 3
    assert longest_common_subsequence("abc", "def") == 0
    assert longest_common_subsequence("bsbininm", "jmjkbkjkv") == 1
    assert longest_common_subsequence("ezupkr", "ubmrapg") == 2
    assert longest_common_subsequence("pmjghexybyrgzczy", "hafcdqbgncrcbihkd") == 4

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
