"""
Problem 025: Generate Parentheses

Difficulty:
Medium

Topic:
Backtracking / DFS / String

Description:
给定一个整数 n，生成所有由 n 对括号组成的、合法的括号组合。

合法括号组合要求：
1. 每个左括号 '(' 都必须有一个对应的右括号 ')'。
2. 从左到右扫描任意前缀时，右括号数量不能超过左括号数量。

Input:
n: int - 括号对数

Output:
List[str] - 所有合法括号组合

Examples:
Example 1:
Input:
n = 3
Output:
["((()))", "(()())", "(())()", "()(())", "()()()"]

Example 2:
Input:
n = 1
Output:
["()"]

Constraints:
- 1 <= n <= 8

Task:
实现 generate_parenthesis(n) 函数。

要求：
1. 使用回溯算法。
2. 不要暴力生成所有长度为 2 * n 的括号字符串后再过滤。
3. 使用两个计数变量记录当前已经使用了多少个左括号和右括号。
4. 思考：
   - 什么时候可以添加左括号？
   - 什么时候可以添加右括号？
   - 什么时候说明一个结果已经完成？
"""

from typing import List


def generate_parenthesis(n: int) -> List[str]:
    # TODO: implement here
    result = []
    # 回溯函数，参数是当前生成的字符串、已经使用的左括号数量、已经使用的右括号数量
    def backtrack(current: str, left_count: int, right_count: int):
        # 如果当前字符串长度等于 2 * n，说明一个结果已经完成
        if len(current) == 2 * n:
            result.append(current)
            return
        
        # 如果左括号数量小于 n，可以添加左括号
        if left_count < n:
            backtrack(current + '(', left_count + 1, right_count)
        
        # 如果右括号数量小于左括号数量，可以添加右括号
        if right_count < left_count:
            backtrack(current + ')', left_count, right_count + 1)

    backtrack("", 0, 0)
    return result


def run_tests():
    assert sorted(generate_parenthesis(1)) == sorted(["()"])
    assert sorted(generate_parenthesis(2)) == sorted(["(())", "()()"])
    assert sorted(generate_parenthesis(3)) == sorted(
        ["((()))", "(()())", "(())()", "()(())", "()()()"]
    )
    assert len(generate_parenthesis(4)) == 14
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
