"""
Problem 050: Decode Ways

Difficulty:
Medium

Topic:
String / Dynamic Programming

Description:
一条包含字母 A-Z 的消息可以通过以下规则编码成数字：

"A" -> "1"
"B" -> "2"
...
"Z" -> "26"

给定一个只包含数字字符的字符串 `s`，请返回它有多少种不同的解码方式。

注意：
- 字符 `'0'` 不能单独解码。
- `'10'` 和 `'20'` 可以分别解码为 `'J'` 和 `'T'`。
- `'06'` 不能解码为 `'F'`，因为数字编码不能有前导零。

Input:
s: str - 一个只包含数字字符的字符串

Output:
int - 不同解码方式的数量

Examples:
Example 1:
Input:
s = "12"
Output:
2
Explanation:
可以解码为 "AB" 或 "L"。

Example 2:
Input:
s = "226"
Output:
3
Explanation:
可以解码为 "BZ"、"VF" 或 "BBF"。

Example 3:
Input:
s = "06"
Output:
0
Explanation:
不能把 "06" 当成 "6"，因为有前导零。

Constraints:
- 1 <= len(s) <= 100
- s 只包含数字字符

Task:
实现 num_decodings(s) 函数。

要求：
1. 返回字符串 `s` 的解码方式数量。
2. 推荐使用动态规划。
3. 不要递归枚举所有可能字符串。

提示：
- 可以令 `dp[i]` 表示 `s` 的前 `i` 个字符有多少种解码方式。
- 每个位置可以考虑两种来源：
  - 如果 `s[i - 1]` 可以单独解码，那么可以从 `dp[i - 1]` 转移。
  - 如果 `s[i - 2:i]` 可以作为 10 到 26 的两位数解码，那么可以从 `dp[i - 2]` 转移。
- 重点注意字符 `'0'` 的处理。
"""


def num_decodings(s: str) -> int:
    # TODO: implement here
    # 定义dp[i] 表示s的前i个字符的解码方式数量
    n = len(s)
    dp = [0] * (n + 1)
    # 初始化 dp[0] = 1 表示空字符串有一种解码方式
    dp[0] = 1
    # dp[1] 根据s[0]是否为'0'来初始化
    dp[1] = 0 if s[0] == '0' else 1
    # 状态转移 一位解码和两位解码分别考虑
    for i in range(2, n + 1):
        # 单独解码 s[i - 1]
        if s[i - 1] != '0':  # 一位数字只要不是0 就必有解码方式
            dp[i] += dp[i - 1]
        # 两位数解码 s[i - 2:i]
        two_digit = int(s[i - 2:i])
        if 10 <= two_digit <= 26:   # 两位数字必须在10到26之间才有解码方式
            dp[i] += dp[i - 2]
    return dp[n]


def run_tests():
    assert num_decodings("12") == 2
    assert num_decodings("226") == 3
    assert num_decodings("06") == 0
    assert num_decodings("0") == 0
    assert num_decodings("10") == 1
    assert num_decodings("20") == 1
    assert num_decodings("27") == 1
    assert num_decodings("101") == 1
    assert num_decodings("11106") == 2

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
