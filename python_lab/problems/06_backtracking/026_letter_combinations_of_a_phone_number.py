"""
Problem 026: Letter Combinations of a Phone Number

Difficulty:
Medium

Topic:
Backtracking / DFS / String / Hash Map

Description:
给定一个只包含数字 2-9 的字符串 digits，返回它能表示的所有字母组合。

数字到字母的映射与电话按键相同：
2 -> abc
3 -> def
4 -> ghi
5 -> jkl
6 -> mno
7 -> pqrs
8 -> tuv
9 -> wxyz

如果 digits 为空字符串，返回空列表。

Input:
digits: str - 只包含 '2' 到 '9' 的字符串

Output:
List[str] - 所有可能的字母组合

Examples:
Example 1:
Input:
digits = "23"
Output:
["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

Example 2:
Input:
digits = ""
Output:
[]

Example 3:
Input:
digits = "2"
Output:
["a", "b", "c"]

Constraints:
- 0 <= digits.length <= 4
- digits[i] 是范围 ['2', '9'] 的数字字符

Task:
实现 letter_combinations(digits) 函数。

要求：
1. 使用回溯算法。
2. 使用字典保存数字到字母的映射关系。
3. 不要使用 itertools.product。
4. 思考：
   - 当前递归层对应 digits 的哪个下标？
   - 当前数字能选择哪些字母？
   - 什么时候形成一个完整组合？
"""

from typing import List


def letter_combinations(digits: str) -> List[str]:
    # TODO: implement here
    # 创建字典
    digit_to_char = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    result = []
    # 如果输入为空，直接返回 []
    if not digits:
        return []
    # 回溯函数
    path = []
    def backtrack(index: int):
        # 如果当前路径长度等于 digits 长度，说明一个组合完成
        if index == len(digits):
            result.append(''.join(path))    # join 将字符列表转换为字符串
            return
        
        # 获取当前数字对应的字符
        current_digit = digits[index]
        possible_chars = digit_to_char[current_digit]
        
        for char in possible_chars:
            path.append(char)
            backtrack(index + 1)
            path.pop()

    backtrack(0)
    return result


def run_tests():
    assert sorted(letter_combinations("23")) == sorted(
        ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    )
    assert letter_combinations("") == []
    assert sorted(letter_combinations("2")) == sorted(["a", "b", "c"])
    assert len(letter_combinations("79")) == 16
    assert sorted(letter_combinations("22")) == sorted(
        ["aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb", "cc"]
    )
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
