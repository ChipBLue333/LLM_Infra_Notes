"""
Problem 075: Word Search II

Difficulty:
Hard

Topic:
Trie / DFS / Backtracking / Matrix

Description:
给定一个二维字符网格 board 和一个单词列表 words，找出所有能够在网格中组成的单词。

单词必须由水平或垂直相邻单元格中的字母按顺序组成。
同一个单元格在同一条搜索路径中不能被重复使用。

与逐个调用单词搜索不同，本题要求先把 words 存入 Trie，再结合网格 DFS，
利用 Trie 的前缀结构提前停止不可能匹配任何单词的搜索路径。

Input:
board: List[List[str]] - 只包含小写英文字母的二维字符网格
words: List[str] - 候选单词列表

Output:
List[str] - 所有能够在网格中找到的候选单词

返回顺序不限，但每个单词只能在结果中出现一次。

Examples:
Example 1:
Input:
board = [
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"],
]
words = ["oath", "pea", "eat", "rain"]

Output:
["oath", "eat"]

Example 2:
Input:
board = [
    ["a", "b"],
    ["c", "d"],
]
words = ["ab", "abc", "abcd", "ac", "bd"]

Output:
["ab", "ac", "bd"]

Constraints:
- 1 <= len(board) <= 12
- 1 <= len(board[0]) <= 12
- board 中只包含小写英文字母
- 1 <= len(words) <= 30000
- 1 <= len(words[i]) <= 10
- words 中的单词互不相同
- words[i] 只包含小写英文字母

Task:
实现 find_words(board, words) 函数。

要求：
1. 先把 words 中的所有单词插入 Trie。
2. Trie 节点需要保存子节点映射。
3. Trie 节点需要能够标记当前位置对应的完整单词。
4. 从 board 的每个格子尝试开始 DFS。
5. 如果当前字符不在 Trie 当前节点的 children 中，立即停止当前分支。
6. 同一个格子在同一条路径中不能重复使用。
7. DFS 返回前必须恢复 board 的原始字符或访问状态。
8. 同一个单词即使能由多条路径组成，也只能加入结果一次。
9. 不要对 words 中的每个单词分别调用一次普通 Word Search。

思考：
- DFS 的状态应该包含网格坐标和哪个 Trie 节点？
- 为什么 Trie 可以比“逐个搜索每个单词”减少大量重复工作？
- 找到完整单词后，为什么还不能立刻停止当前 DFS 分支？
- 可以怎样利用 Trie 节点本身完成结果去重？
- 可选优化：搜索结束后，能否删除已经没有用途的 Trie 分支？
"""

from typing import Dict, List


class TrieNode:
    def __init__(self) -> None:
        # words插入tire 每个节点保存children和word
        self.children: Dict[str, TrieNode] = {}
        self.word: str = ""  # 只有当这个节点是一个完整单词的结尾时，word才不为空
        # 单词结尾的节点的word属性保存完整单词，其他节点的word属性保持空字符串


def find_words(board: List[List[str]], words: List[str]) -> List[str]:
    # 1. 构建 Trie
    root = TrieNode()
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word  # 标记完整单词的结尾
    
    rows, cols = len(board), len(board[0])
    found_words = set()  # 用于存储找到的单词，自动去重
    # 2. 定义 DFS 函数
    def dfs(r: int, c: int, node: TrieNode) -> None:
        char = board[r][c]
        if char not in node.children:
            return  # 当前路径不可能匹配任何单词，立即停止
        
        next_node = node.children[char]
        if next_node.word:  # 找到一个完整单词
            found_words.add(next_node.word)  # 加入结果集合
        
        # 标记当前格子为访问过（可以用特殊字符或布尔数组）
        board[r][c] = "#"  # 临时修改为特殊字符表示访问过
        
        # 4 个方向的 DFS
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                dfs(nr, nc, next_node)
        
        # 恢复当前格子的原始字符
        board[r][c] = char
    # 3. 从每个格子开始 DFS
    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root)
    # 4. 返回找到的单词列表
    return list(found_words)  # 返回找到的单词列表



def assert_words(
    board: List[List[str]],
    words: List[str],
    expected: List[str],
) -> None:
    original_board = [row.copy() for row in board]
    result = find_words(board, words)

    assert set(result) == set(expected), (
        f"expected {set(expected)}, got {set(result)}"
    )
    assert len(result) == len(set(result)), f"结果中存在重复单词: {result}"
    assert board == original_board, "搜索结束后必须恢复 board"


def run_tests() -> None:
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    assert_words(board, ["oath", "pea", "eat", "rain"], ["oath", "eat"])

    board = [
        ["a", "b"],
        ["c", "d"],
    ]
    assert_words(
        board,
        ["ab", "abc", "abcd", "ac", "bd"],
        ["ab", "ac", "bd"],
    )

    board = [
        ["a", "b"],
        ["a", "a"],
    ]
    assert_words(board, ["a", "aa", "aaa", "aaaa", "aaaaa"], [
        "a",
        "aa",
        "aaa",
    ])

    assert_words([["a"]], ["a", "b", "aa"], ["a"])

    board = [
        ["c", "a", "t"],
        ["r", "r", "e"],
        ["t", "o", "n"],
    ]
    assert_words(
        board,
        ["cat", "car", "cart", "care", "tone", "not", "tree"],
        ["cat", "car", "care", "tone", "not"],
    )

    assert_words([["a", "b"]], ["aba"], [])

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
