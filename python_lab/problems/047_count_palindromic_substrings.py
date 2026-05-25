"""
Problem 047: Count Palindromic Substrings

Difficulty:
Medium

Topic:
String / Dynamic Programming / Two Pointers

Description:
给定一个字符串 `s`，请返回 `s` 中回文子串的数量。

子串必须是原字符串中连续的一段。
回文字符串是指从左往右读和从右往左读都相同的字符串。

注意：
- 相同内容但位置不同的子串，需要分别计数。
- 本题统计的是回文子串数量，不是最长长度。

Input:
s: str - 一个字符串

Output:
int - 回文子串的数量

Examples:
Example 1:
Input:
s = "abc"
Output:
3
Explanation:
三个回文子串分别是 "a"、"b"、"c"。

Example 2:
Input:
s = "aaa"
Output:
6
Explanation:
六个回文子串分别是：
"a"、"a"、"a"、"aa"、"aa"、"aaa"。
注意位置不同的 "a" 和 "aa" 要分别计数。

Example 3:
Input:
s = "abba"
Output:
6
Explanation:
回文子串包括 "a"、"b"、"b"、"a"、"bb"、"abba"。

Constraints:
- 1 <= len(s) <= 1000
- s 只包含小写英文字母

Task:
实现 count_palindromic_substrings(s) 函数。

要求：
1. 返回回文子串数量。
2. 子串必须连续。
3. 相同内容但位置不同的子串要分别计数。
4. 可以使用中心扩展，也可以使用动态规划。
5. 不要生成所有子串再逐个反转判断。

提示：
- 如果使用 DP，可以令 `dp[i][j]` 表示 `s[i:j+1]` 是否是回文子串。
- 如果 `s[i] == s[j]`，还需要判断中间 `s[i+1:j]` 是否是回文。
- 每当发现一个新的回文子串，就把计数加 1。
- 如果使用中心扩展，记得处理奇数长度中心和偶数长度中心。
"""


def count_palindromic_substrings(s: str) -> int:
    # TODO: implement here
    # 定义dp[i][j]表示s[i:j+1]是否是回文子串
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    count = 0
    for j in range(n):
        for i in range(j + 1):
            if s[i] == s[j]:
                if j - i <= 2:  # 长度为1或2的子串，或者长度为3但两端相同
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]  # 中间部分也要是回文
            if dp[i][j]:
                count += 1
    return count


def run_tests():
    assert count_palindromic_substrings("abc") == 3
    assert count_palindromic_substrings("aaa") == 6
    assert count_palindromic_substrings("abba") == 6
    assert count_palindromic_substrings("a") == 1
    assert count_palindromic_substrings("abccba") == 9
    assert count_palindromic_substrings("racecar") == 10
    assert count_palindromic_substrings("aaaa") == 10

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
