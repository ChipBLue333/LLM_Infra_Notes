"""
Problem 073: Implement Trie Prefix Tree

Difficulty:
Medium

Topic:
Trie / Design / String

Description:
实现一个 Trie，也叫前缀树。

Trie 是一种树形数据结构，常用于高效存储和查询字符串集合。它特别适合处理：
- 判断某个完整单词是否存在；
- 判断是否存在以某个字符串开头的单词；
- 自动补全、字典搜索等前缀相关问题。

你需要实现 Trie 类，支持以下三个操作：

1. insert(word)
   将字符串 word 插入 Trie。

2. search(word)
   如果字符串 word 已经作为完整单词插入过，返回 True；否则返回 False。

3. starts_with(prefix)
   如果 Trie 中存在任何一个已经插入的单词以 prefix 开头，返回 True；否则返回 False。

Input:
通过调用 Trie 类的方法进行输入。

Output:
每个 search 或 starts_with 调用返回 bool。

Examples:
Example 1:
Input:
trie = Trie()
trie.insert("apple")
trie.search("apple")
trie.search("app")
trie.starts_with("app")
trie.insert("app")
trie.search("app")

Output:
True
False
True
True

Explanation:
"apple" 插入后，"apple" 是完整单词。
"app" 虽然是 "apple" 的前缀，但还没有作为完整单词插入，所以 search("app") 返回 False。
插入 "app" 后，search("app") 返回 True。

Constraints:
- 1 <= len(word), len(prefix) <= 2000
- word 和 prefix 只包含小写英文字母
- insert、search 和 starts_with 总调用次数不超过 30000

Task:
实现 Trie 类。

要求：
1. 每个节点需要保存它的子节点映射。
2. 每个节点需要记录“从根到当前节点是否构成一个完整单词”。
3. insert 时，逐个字符向下走；没有对应子节点时创建新节点。
4. search 时，逐个字符向下走；如果中途缺字符，返回 False。
5. search 走完后，还要判断当前节点是否是完整单词结尾。
6. starts_with 只需要确认 prefix 的所有字符都能走完，不要求是完整单词。

提示：
- 可以用 dict 存储 children：字符 -> 子节点。
- 可以先写一个辅助方法，用来根据字符串走到最后一个节点。
- search 和 starts_with 的区别只在于最后是否检查 is_word。
"""


class TrieNode:
    def __init__(self):
        # children: dict
        self.children = {}
        # is_word: bool
        self.is_word = False


class Trie:
    def __init__(self):
        # root: TrieNode
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # 从root开始
        node = self.root
        for char in word:
            # 如果当前字符不在children里，创建新节点
            if char not in node.children:
                node.children[char] = TrieNode()
            # 移动到子节点
            node = node.children[char]
        # 最后一个节点标记为完整单词结尾
        node.is_word = True

    def search(self, word: str) -> bool:
        # 从root开始
        node = self.root
        for char in word:
            # 如果当前字符不在children里，返回False
            if char not in node.children:
                return False
            # 移动到子节点
            node = node.children[char]
        # 检查最后一个节点是否是完整单词结尾
        return node.is_word

    def starts_with(self, prefix: str) -> bool:
        # 从root开始
        node = self.root
        for char in prefix:
            # 如果当前字符不在children里，返回False
            if char not in node.children:
                return False
            # 移动到子节点
            node = node.children[char]
        # 如果能走到这里，说明prefix的所有字符都能走完
        return True 


def run_tests():
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.starts_with("app") is True
    trie.insert("app")
    assert trie.search("app") is True

    trie = Trie()
    trie.insert("cat")
    trie.insert("car")
    trie.insert("care")
    assert trie.search("cat") is True
    assert trie.search("car") is True
    assert trie.search("care") is True
    assert trie.search("ca") is False
    assert trie.starts_with("ca") is True
    assert trie.starts_with("caref") is False

    trie = Trie()
    trie.insert("a")
    assert trie.search("a") is True
    assert trie.starts_with("a") is True
    assert trie.search("b") is False
    assert trie.starts_with("b") is False

    trie = Trie()
    trie.insert("same")
    trie.insert("same")
    assert trie.search("same") is True
    assert trie.starts_with("sam") is True

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
