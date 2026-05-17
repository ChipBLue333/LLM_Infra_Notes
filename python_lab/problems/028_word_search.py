"""
Problem 028: Word Search

Difficulty:
Medium

Topic:
Backtracking / DFS / Matrix

Description:
给定一个二维字符网格 board 和一个字符串 word，判断 word 是否存在于网格中。

word 必须由相邻单元格中的字母按顺序组成，其中“相邻”表示水平或垂直相邻。
同一个单元格在同一次搜索路径中不能被重复使用。

Input:
board: List[List[str]] - 二维字符网格
word: str - 需要查找的单词

Output:
bool - 如果 word 存在于网格中，返回 True；否则返回 False

Examples:
Example 1:
Input:
board = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"],
]
word = "ABCCED"
Output:
True

Example 2:
Input:
board = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"],
]
word = "SEE"
Output:
True

Example 3:
Input:
board = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"],
]
word = "ABCB"
Output:
False

Constraints:
- 1 <= len(board) <= 6
- 1 <= len(board[0]) <= 6
- board 中只包含英文字母
- 1 <= len(word) <= 15
- 同一个格子在同一条路径中不能重复使用

Task:
实现 exist(board, word) 函数。

要求：
1. 使用 DFS / 回溯。
2. 从网格中的每个位置都可以作为搜索起点。
3. 搜索过程中需要标记当前路径已经访问过的格子。
4. 递归返回后必须恢复访问状态。
5. 不要把 board 转成字符串，也不要使用正则。

思考：
- 当前递归状态应该包含哪些信息？
- 如何表示“已经匹配到 word 的第几个字符”？
- 越界、字符不匹配、重复访问，分别应该在什么时候判断？
- 为什么找到一个可行路径后可以立刻返回 True？
"""

from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    # TODO: implement here
    m, n = len(board), len(board[0])
    # dfs
    def dfs(i: int, j: int, k: int) -> bool:
        # 越界
        if i < 0 or i >= m or j < 0 or j >= n:
            return False
        # 字符不匹配
        if board[i][j] != word[k]:
            return False
        # 已经匹配到 word 的最后一个字符了
        if k == len(word) - 1:
            return True

        # 标记当前格子为访问过
        temp = board[i][j]
        board[i][j] = "#"

        # 四个方向继续搜索
        found = (
            dfs(i + 1, j, k + 1)
            or dfs(i - 1, j, k + 1)
            or dfs(i, j + 1, k + 1)
            or dfs(i, j - 1, k + 1)
        )

        # 恢复访问状态
        board[i][j] = temp

        return found

    for i in range(m):
        for j in range(n):
            if dfs(i, j, 0):
                return True
    return False    



def run_tests():
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]
    assert exist(board, "ABCCED") is True
    assert exist(board, "SEE") is True
    assert exist(board, "ABCB") is False

    assert exist([["A"]], "A") is True
    assert exist([["A"]], "B") is False

    board = [
        ["A", "A"],
        ["A", "A"],
    ]
    assert exist(board, "AAAA") is True
    assert exist(board, "AAAAA") is False

    board = [
        ["C", "A", "A"],
        ["A", "A", "A"],
        ["B", "C", "D"],
    ]
    assert exist(board, "AAB") is True

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
