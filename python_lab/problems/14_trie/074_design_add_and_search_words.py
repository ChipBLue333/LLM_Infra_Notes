"""
Problem 074: Design Add and Search Words Data Structure

Difficulty:
Medium

Topic:
Trie / DFS / Backtracking / Design / String

Description:
设计一个支持添加单词和搜索单词的数据结构。

这个数据结构需要支持两个操作：

1. add_word(word)
   将字符串 word 添加到数据结构中。

2. search(word)
   判断是否存在某个已经添加过的单词，可以和 word 匹配。

特殊规则：
- word 中可能包含小写英文字母；
- search 的参数中还可能包含字符 "."；
- "." 可以匹配任意一个小写英文字母，但只能匹配一个字符。

Input:
通过调用 WordDictionary 类的方法进行输入。

Output:
每个 search 调用返回 bool。

Examples:
Example 1:
Input:
word_dict = WordDictionary()
word_dict.add_word("bad")
word_dict.add_word("dad")
word_dict.add_word("mad")
word_dict.search("pad")
word_dict.search("bad")
word_dict.search(".ad")
word_dict.search("b..")

Output:
False
True
True
True

Explanation:
"pad" 没有被添加过，也无法匹配任何已添加单词。
"bad" 是完整添加过的单词。
".ad" 可以匹配 "bad"、"dad" 或 "mad"。
"b.." 可以匹配 "bad"。

Example 2:
Input:
word_dict = WordDictionary()
word_dict.add_word("a")
word_dict.add_word("ab")
word_dict.search("a")
word_dict.search(".")
word_dict.search("..")
word_dict.search("...")

Output:
True
True
True
False

Constraints:
- 1 <= len(word) <= 25
- add_word 中的 word 只包含小写英文字母
- search 中的 word 只包含小写英文字母和 "."
- 最多调用 add_word 和 search 共 10000 次

Task:
实现 WordDictionary 类。

要求：
1. 使用 Trie 存储添加过的单词。
2. add_word 的逻辑和普通 Trie 插入类似。
3. search 遇到普通字符时，只沿着对应子节点继续查找。
4. search 遇到 "." 时，需要尝试当前节点的所有子节点。
5. 搜索走到 word 末尾时，必须确认当前位置是完整单词结尾。

提示：
- search 可以写一个内部 DFS helper，例如 dfs(index, node)。
- index 表示当前要匹配 word 中的第几个字符。
- 如果当前字符是 "."，只要任意一个子分支匹配成功，就可以返回 True。
- 注意 "." 匹配的是一个字符，不是零个或多个字符。
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        # 写入单词
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word: str) -> bool:
        # 使用DFS搜索单词
        def dfs(index: int, node: TrieNode) -> bool:
            if index == len(word):
                return node.is_word

            char = word[index]
            if char == ".":
                # 尝试所有子节点
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                return False
            else:
                # 继续沿着对应子节点搜索
                if char not in node.children:
                    return False
                return dfs(index + 1, node.children[char])
        return dfs(0, self.root)


def run_tests():
    word_dict = WordDictionary()
    word_dict.add_word("bad")
    word_dict.add_word("dad")
    word_dict.add_word("mad")
    assert word_dict.search("pad") is False
    assert word_dict.search("bad") is True
    assert word_dict.search(".ad") is True
    assert word_dict.search("b..") is True

    word_dict = WordDictionary()
    word_dict.add_word("a")
    word_dict.add_word("ab")
    assert word_dict.search("a") is True
    assert word_dict.search(".") is True
    assert word_dict.search("..") is True
    assert word_dict.search("...") is False

    word_dict = WordDictionary()
    word_dict.add_word("at")
    word_dict.add_word("and")
    word_dict.add_word("an")
    word_dict.add_word("add")
    assert word_dict.search("a") is False
    assert word_dict.search(".at") is False
    word_dict.add_word("bat")
    assert word_dict.search(".at") is True
    assert word_dict.search("an.") is True
    assert word_dict.search("a.d.") is False
    assert word_dict.search("b.") is False
    assert word_dict.search("a.d") is True
    assert word_dict.search(".") is False

    word_dict = WordDictionary()
    word_dict.add_word("same")
    word_dict.add_word("same")
    assert word_dict.search("same") is True
    assert word_dict.search("s.me") is True
    assert word_dict.search("sam.") is True
    assert word_dict.search("same.") is False

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
