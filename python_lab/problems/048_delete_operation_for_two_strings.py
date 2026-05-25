"""
Problem 048: Delete Operation for Two Strings

Difficulty:
Medium

Topic:
String / Dynamic Programming / Longest Common Subsequence

Description:
给定两个字符串 `word1` 和 `word2`，每次操作可以从任意一个字符串中删除一个字符。

请返回使 `word1` 和 `word2` 变成相同字符串所需的最少删除次数。

注意：
- 只能删除字符，不能插入、替换或交换字符。
- 删除后保留下来的字符顺序不能改变。
- 两个字符串最终可以变成空字符串。

Input:
word1: str - 第一个字符串
word2: str - 第二个字符串

Output:
int - 使两个字符串相同所需的最少删除次数

Examples:
Example 1:
Input:
word1 = "sea", word2 = "eat"
Output:
2
Explanation:
从 "sea" 中删除 "s"，得到 "ea"。
从 "eat" 中删除 "t"，得到 "ea"。
一共删除 2 次。

Example 2:
Input:
word1 = "leetcode", word2 = "etco"
Output:
4
Explanation:
可以删除若干字符，使两个字符串都变成 "etco"。

Example 3:
Input:
word1 = "abc", word2 = "abc"
Output:
0
Explanation:
两个字符串已经相同，不需要删除。

Constraints:
- 1 <= len(word1), len(word2) <= 500
- word1 和 word2 只包含小写英文字母

Task:
实现 min_delete_distance(word1, word2) 函数。

要求：
1. 返回最少删除次数。
2. 推荐使用动态规划。
3. 可以从“最长公共子序列”角度思考。
4. 不要使用暴力枚举所有删除方案。

提示：
- 如果两个字符串最终要相同，那么最终保留下来的部分一定是它们的公共子序列。
- 为了删除次数最少，应该尽量保留最长的公共子序列。
- 假设最长公共子序列长度是 `lcs`，思考答案和 `len(word1)`、`len(word2)`、`lcs` 的关系。
"""


def min_delete_distance(word1: str, word2: str) -> int:
    # TODO: implement here
    # 先求LCS长度
    # 再通过l1 + l2 - 2 * lcs计算删除次数
    L1 = len(word1)
    L2 = len(word2)
    # 定义dp[i][j]为word1前i个字符和word2前j个字符的最长公共子序列长度
    dp = [[0] * (L2 + 1) for _ in range(L1 + 1)]
    for i in range(1, L1 + 1):
        for j in range(1, L2 + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    lcs = dp[L1][L2]
    return L1 + L2 - 2 * lcs


def run_tests():
    assert min_delete_distance("sea", "eat") == 2
    assert min_delete_distance("leetcode", "etco") == 4
    assert min_delete_distance("abc", "abc") == 0
    assert min_delete_distance("abc", "def") == 6
    assert min_delete_distance("a", "b") == 2
    assert min_delete_distance("park", "spake") == 3

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
