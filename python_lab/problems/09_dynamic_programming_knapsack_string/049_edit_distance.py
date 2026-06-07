"""
Problem 049: Edit Distance

Difficulty:
Medium

Topic:
String / Dynamic Programming / 2D DP

Description:
给定两个字符串 `word1` 和 `word2`，请返回将 `word1` 转换成 `word2` 所需的最少操作次数。

你可以对 `word1` 执行以下三种操作：
1. 插入一个字符
2. 删除一个字符
3. 替换一个字符

Input:
word1: str - 原始字符串
word2: str - 目标字符串

Output:
int - 将 `word1` 转换成 `word2` 的最少操作次数

Examples:
Example 1:
Input:
word1 = "horse", word2 = "ros"
Output:
3
Explanation:
horse -> rorse  替换 'h' 为 'r'
rorse -> rose   删除 'r'
rose -> ros     删除 'e'

Example 2:
Input:
word1 = "intention", word2 = "execution"
Output:
5
Explanation:
可以通过 5 次操作将 "intention" 转换成 "execution"。

Example 3:
Input:
word1 = "abc", word2 = "abc"
Output:
0
Explanation:
两个字符串已经相同，不需要任何操作。

Constraints:
- 0 <= len(word1), len(word2) <= 500
- word1 和 word2 只包含小写英文字母

Task:
实现 min_edit_distance(word1, word2) 函数。

要求：
1. 返回最少操作次数。
2. 必须使用动态规划思路。
3. 不要使用暴力递归枚举所有操作路径。

提示：
- 可以令 `dp[i][j]` 表示：把 `word1` 的前 `i` 个字符转换成 `word2` 的前 `j` 个字符所需的最少操作次数。
- 当 `word1[i - 1] == word2[j - 1]` 时，当前字符不需要额外操作。
- 当两个当前字符不相等时，思考三种操作分别对应哪个前置状态：
  - 删除 `word1` 当前字符
  - 给 `word1` 插入一个字符来匹配 `word2` 当前字符
  - 替换 `word1` 当前字符为 `word2` 当前字符
"""


def min_edit_distance(word1: str, word2: str) -> int:
    # TODO: implement here
    # 定义dp[i][j] 表示将word1前i个字符转换成word2前j个字符的最少操作次数
    L1 = len(word1)
    L2 = len(word2)
    dp = [[0] * (L2 + 1) for _ in range(L1 + 1)]
    # 初始化 第一行和第一列
    # 第一列：将word1前i个字符转换成空字符串 需要删除i次
    for i in range(L1 + 1):
        dp[i][0] = i
    # 第一行：将空字符串转换成word2前j个字符 需要插入j次
    for j in range(L2 + 1):
        dp[0][j] = j
    # 填充dp表
    for i in range(1, L1 + 1):
        for j in range(1, L2 + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    return dp[L1][L2]

def run_tests():
    assert min_edit_distance("horse", "ros") == 3
    assert min_edit_distance("intention", "execution") == 5
    assert min_edit_distance("abc", "abc") == 0
    assert min_edit_distance("", "") == 0
    assert min_edit_distance("", "abc") == 3
    assert min_edit_distance("abc", "") == 3
    assert min_edit_distance("a", "b") == 1
    assert min_edit_distance("kitten", "sitting") == 3

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
