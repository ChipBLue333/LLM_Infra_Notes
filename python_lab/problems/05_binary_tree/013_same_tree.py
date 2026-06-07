"""
Problem 013: Same Tree

Difficulty:
Easy

Topic:
Tree Traversal / DFS / Recursion

Description:
给定两棵二叉树的根节点 p 和 q，判断这两棵树是否完全相同。

如果两棵树在结构上完全一致，并且对应节点的值也完全相同，那么它们就是相同的二叉树。

这道题的关键不是只比较节点值，而是同时比较：
1. 当前节点是否都存在；
2. 当前节点的值是否相等；
3. 左子树是否相同；
4. 右子树是否相同。

Input:
p: Optional[TreeNode] - 第一棵二叉树的根节点
q: Optional[TreeNode] - 第二棵二叉树的根节点

Output:
bool - 如果两棵树完全相同，返回 True；否则返回 False。

Examples:
Example 1:
Input:
p = [1,2,3]
q = [1,2,3]
Output:
True

Example 2:
Input:
p = [1,2]
q = [1,null,2]
Output:
False

Example 3:
Input:
p = [1,2,1]
q = [1,1,2]
Output:
False

Constraints:
- 两棵树中的节点数都在 [0, 100] 区间内。
- -10^4 <= Node.val <= 10^4

Task:
实现 is_same_tree(p, q) 函数。
"""

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # TODO: implement here
    # 如果p树和q树都为空，说明它们相同
    if not p and not q:
        return True
    # 如果p树和q树其中一个为空，说明它们不相同
    if not p or not q:
        return False
    # 如果当前节点的值不相等，说明它们不相同
    if p.val != q.val:
        return False
    # 递归比较左子树和右子树
    is_left_same = is_same_tree(p.left, q.left)
    is_right_same = is_same_tree(p.right, q.right)
    return is_left_same and is_right_same


def run_tests():
    # Example 1
    # p:    1
    #      / \
    #     2   3
    # q:    1
    #      / \
    #     2   3
    p1 = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
    q1 = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
    assert is_same_tree(p1, q1) is True

    # Example 2
    # p:    1
    #      /
    #     2
    # q:    1
    #        \
    #         2
    p2 = TreeNode(1, left=TreeNode(2))
    q2 = TreeNode(1, right=TreeNode(2))
    assert is_same_tree(p2, q2) is False

    # Example 3
    # p:    1
    #      / \
    #     2   1
    # q:    1
    #      / \
    #     1   2
    p3 = TreeNode(1, left=TreeNode(2), right=TreeNode(1))
    q3 = TreeNode(1, left=TreeNode(1), right=TreeNode(2))
    assert is_same_tree(p3, q3) is False

    # Both empty trees
    assert is_same_tree(None, None) is True

    # One empty tree, one non-empty tree
    assert is_same_tree(TreeNode(0), None) is False

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
