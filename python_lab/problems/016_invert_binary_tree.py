"""
Problem 016: Invert Binary Tree

Difficulty:
Easy

Topic:
Tree Traversal / DFS / Recursion

Description:
给定一棵二叉树的根节点 root，请翻转这棵二叉树，并返回翻转后的根节点。

翻转二叉树的含义是：
对树中的每一个节点，交换它的左子树和右子树。

Input:
root: Optional[TreeNode] - 二叉树的根节点

Output:
Optional[TreeNode] - 翻转后的二叉树根节点

Examples:
Example 1:
Input:
root = [4,2,7,1,3,6,9]
Output:
[4,7,2,9,6,3,1]

原树：
        4
      /   \
     2     7
    / \   / \
   1   3 6   9

翻转后：
        4
      /   \
     7     2
    / \   / \
   9   6 3   1

Example 2:
Input:
root = [2,1,3]
Output:
[2,3,1]

Example 3:
Input:
root = []
Output:
[]

Constraints:
- 树中节点的数量在 [0, 100] 区间内。
- -100 <= Node.val <= 100

Task:
实现 invert_tree(root) 函数。
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    # TODO: implement here
    # 空树直接返回 None
    if root is None:
        return None
    # 对于一个节点，交换它的左右子树 （孩子是树）
    root.left = invert_tree(root.left)
    root.right = invert_tree(root.right)

    # 交换左右节点
    temp = None
    temp = root.right
    root.right = root.left
    root.left = temp

    return root



def tree_to_level_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []

    result: List[Optional[int]] = []
    queue: List[Optional[TreeNode]] = [root]

    while queue:
        node = queue.pop(0)
        if node is None:
            result.append(None)
            continue

        result.append(node.val)
        queue.append(node.left)
        queue.append(node.right)

    while result and result[-1] is None:
        result.pop()

    return result


def run_tests():
    # Example 1
    #        4
    #      /   \
    #     2     7
    #    / \   / \
    #   1   3 6   9
    root1 = TreeNode(4)
    root1.left = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
    root1.right = TreeNode(7, left=TreeNode(6), right=TreeNode(9))
    assert tree_to_level_list(invert_tree(root1)) == [4, 7, 2, 9, 6, 3, 1]

    # Example 2
    root2 = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
    assert tree_to_level_list(invert_tree(root2)) == [2, 3, 1]

    # Empty tree
    assert tree_to_level_list(invert_tree(None)) == []

    # Single node
    root3 = TreeNode(1)
    assert tree_to_level_list(invert_tree(root3)) == [1]

    # Only left child
    root4 = TreeNode(1, left=TreeNode(2))
    assert tree_to_level_list(invert_tree(root4)) == [1, None, 2]

    # Only right child
    root5 = TreeNode(1, right=TreeNode(2))
    assert tree_to_level_list(invert_tree(root5)) == [1, 2]

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
