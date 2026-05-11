"""
Problem 005: Longest Substring Without Repeating Characters

Difficulty:
Medium

Topic:
Hash Map / Sliding Window / String

Description:
给定一个字符串 `s` ，请你找出其中不含有重复字符的最长子串的长度。

Input:
s: str

Output:
int

Examples:
示例 1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
请注意，你的答案必须是子串的长度，"pwke" 是一个子序列，不是子串。

Constraints:
- 0 <= s.length <= 5 * 10^4
- `s` 由英文字母、数字、符号和空格组成

Task:
Implement length_of_longest_substring(s).
"""

def length_of_longest_substring(s: str) -> int:
    # TODO: implement here
    # 滑动窗口 + 哈希表
    # 用一个哈希表记录当前窗口内每个字符最后一次出现的位置
    # 用两个指针表示当前窗口的左右边界，初始时都指向字符串的开头
    # 右指针向右移动，遇到一个字符如果它已经在哈希表中，并且它的最后一次出现位置在当前窗口内，则左指针移动到该字符最后一次出现位置的下一位
    # 同时更新该字符在哈希表中的位置为当前右指针的位置
    # 每次右指针移动后，计算当前窗口的长度，并更新最大长度
    char_index = {} # 字典根据值查找位置
    left = 0
    max_length = 0
    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left: # 在当前记录元素的位置的右侧 如果找到重复元素 则更新左指针位置
            left = char_index[s[right]] + 1
        # 如果没重复或者重复元素在左指针的左侧 就不更新左指针位置
        char_index[s[right]] = right    # 添加当前元素的位置
        max_length = max(max_length, right - left + 1)
    return max_length   


def run_tests():
    assert length_of_longest_substring("abcabcbb") == 3, "Test Case 1 Failed"
    assert length_of_longest_substring("bbbbb") == 1, "Test Case 2 Failed"
    assert length_of_longest_substring("pwwkew") == 3, "Test Case 3 Failed"
    assert length_of_longest_substring("") == 0, "Test Case 4 Failed"
    assert length_of_longest_substring(" ") == 1, "Test Case 5 Failed"
    assert length_of_longest_substring("au") == 2, "Test Case 6 Failed"
    assert length_of_longest_substring("dvdf") == 3, "Test Case 7 Failed"
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
