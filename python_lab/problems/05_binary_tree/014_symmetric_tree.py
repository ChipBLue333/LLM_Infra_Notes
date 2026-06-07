"""
Problem 014: Symmetric Tree

Difficulty:
Easy

Topic:
Tree Traversal / DFS / Recursion / BFS

Description:
给定一个二叉树的根节点 root，判断这棵树是否是轴对称的。

如果一棵二叉树的左子树和右子树互为镜像，那么这棵树就是对称二叉树。

镜像关系不是简单地比较“左对左、右对右”，而是比较：
1. 左子树的根节点值 和 右子树的根节点值 是否相等；
2. 左子树的左孩子 和 右子树的右孩子 是否互为镜像；
3. 左子树的右孩子 和 右子树的左孩子 是否互为镜像。

Input:
root: Optional[TreeNode] - 二叉树的根节点

Output:
bool - 如果这棵树是轴对称的，返回 True；否则返回 False。

Examples:
Example 1:
Input:
root = [1,2,2,3,4,4,3]
Output:
True

Example 2:
Input:
root = [1,2,2,null,3,null,3]
Output:
False

Example 3:
Input:
root = []
Output:
True

Constraints:
- 树中节点数目在 [0, 1000] 区间内。
- -100 <= Node.val <= 100

Task:
实现 is_symmetric(root) 函数。
"""

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root: Optional[TreeNode]) -> bool:
    # TODO: implement here
    def is_mirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)
    if not root:
        return True
    return is_mirror(root.left, root.right)



def run_tests():
    # Example 1
    #        1
    #      /   \
    #     2     2
    #    / \   / \
    #   3   4 4   3
    root1 = TreeNode(1)
    root1.left = TreeNode(2, left=TreeNode(3), right=TreeNode(4))
    root1.right = TreeNode(2, left=TreeNode(4), right=TreeNode(3))
    assert is_symmetric(root1) is True

    # Example 2
    #      1
    #    /   \
    #   2     2
    #    \     \
    #     3     3
    root2 = TreeNode(1)
    root2.left = TreeNode(2, right=TreeNode(3))
    root2.right = TreeNode(2, right=TreeNode(3))
    assert is_symmetric(root2) is False

    # Empty tree
    assert is_symmetric(None) is True

    # Single node
    assert is_symmetric(TreeNode(1)) is True

    # Same values but not symmetric structure
    #      1
    #    /   \
    #   2     2
    #  /
    # 3
    root3 = TreeNode(1)
    root3.left = TreeNode(2, left=TreeNode(3))
    root3.right = TreeNode(2)
    assert is_symmetric(root3) is False

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
