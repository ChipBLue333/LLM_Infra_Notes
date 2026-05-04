"""
Problem 002: 有效的括号 (Valid Parentheses)

Difficulty:
Easy

Topic:
String / Stack / Hash Map

Description:
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 `s` ，判断字符串是否有效。

有效字符串需满足：
1. 左括号必须用相同类型的右括号闭合。
2. 左括号必须以正确的顺序闭合。
3. 每个右括号都有一个对应的相同类型的左括号。

Input:
- s: str，仅由括号字符组成的字符串。

Output:
- bool，表明字符串是否有效。

Examples:
Example 1:
Input: s = "()"
Output: True

Example 2:
Input: s = "()[]{}"
Output: True

Example 3:
Input: s = "(]"
Output: False

Example 4:
Input: s = "([)]"
Output: False

Example 5:
Input: s = "{[]}"
Output: True

Constraints:
- 1 <= s.length <= 10^4
- s 仅由括号 '()[]{}' 组成

Task:
实现 solution 函数。
"""

def solution(s: str) -> bool:
    # TODO: implement here
    my_list = []    # 用来模拟栈的列表
    seen_map = {"(": ")", "[": "]", "{": "}"}   # 定义一个字典来映射左括号到对应的右括号
    for char in s:
        if char in "([{":
            my_list.append(char)    # 如果是左括号，就入栈
        else:
            if not my_list: # 如果当前字符是右括号，但栈已经空了，说明没有匹配的左括号
                return False
            last_char = my_list.pop()   # 从栈顶弹出一个左括号，检查它是否与当前的右括号匹配
            if seen_map[last_char] != char:
                return False
    return not my_list


def run_tests():
    assert solution("()") == True, "Test case 1 failed"
    assert solution("()[]{}") == True, "Test case 2 failed"
    assert solution("(]") == False, "Test case 3 failed"
    assert solution("([)]") == False, "Test case 4 failed"
    assert solution("{[]}") == True, "Test case 5 failed"
    assert solution("[") == False, "Test case 6 failed"
    assert solution("]") == False, "Test case 7 failed"
    print("All test cases passed!")


if __name__ == "__main__":
    run_tests()
