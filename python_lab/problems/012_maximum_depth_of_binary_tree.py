"""
Problem 012: Maximum Depth of Binary Tree

Difficulty:
Easy

Topic:
Tree Traversal / DFS / BFS

Description:
给定一个二叉树 root ，返回其最大深度。

二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。

提示：
你刚才已经掌握了 DFS（递归思路）和 BFS（层序遍历队列思路）。
这道题这两种方法都可以做！
- 如果用 DFS/递归：树的最大深度 = max(左子树最大深度, 右子树最大深度) + 1。
- 如果用 BFS/队列：树有几层，最大深度就是几。

本题请你选择一种你喜欢的方法来实现。

Input:
root: Optional[TreeNode] - 二叉树的根节点

Output:
int - 二叉树的最大深度

Examples:
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Constraints:
- 树中节点的数量在 [0, 10^4] 区间内。
- -100 <= Node.val <= 100

Task:
实现 max_depth(root) 函数。
"""

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: Optional[TreeNode]) -> int:
    # TODO: implement here
    if not root:
        return 0
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    return max(left_depth, right_depth) + 1


def run_tests():
    # Example 1
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20, left=TreeNode(15), right=TreeNode(7))
    assert max_depth(root1) == 3

    # Example 2
    #  1
    #   \
    #    2
    root2 = TreeNode(1, right=TreeNode(2))
    assert max_depth(root2) == 2

    # Example 3 (Empty tree)
    assert max_depth(None) == 0

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
