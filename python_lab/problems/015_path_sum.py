"""
Problem 015: Path Sum

Difficulty:
Easy

Topic:
Tree Traversal / DFS / Recursion

Description:
给定一个二叉树的根节点 root 和一个整数 target_sum，判断这棵树中是否存在一条从根节点到叶子节点的路径，使得路径上所有节点值的总和等于 target_sum。

叶子节点是指没有左孩子也没有右孩子的节点。

注意：
路径必须从根节点开始，并且必须到叶子节点结束。
不能只选树中的某一段路径。

Input:
root: Optional[TreeNode] - 二叉树的根节点
target_sum: int - 目标路径和

Output:
bool - 如果存在一条根到叶子的路径和等于 target_sum，返回 True；否则返回 False。

Examples:
Example 1:
Input:
root = [5,4,8,11,null,13,4,7,2,null,null,null,1]
target_sum = 22
Output:
True
Explanation:
路径 5 -> 4 -> 11 -> 2 的节点和为 22。

Example 2:
Input:
root = [1,2,3]
target_sum = 5
Output:
False

Example 3:
Input:
root = []
target_sum = 0
Output:
False

Constraints:
- 树中节点的数量在 [0, 5000] 区间内。
- -1000 <= Node.val <= 1000
- -1000 <= target_sum <= 1000

Task:
实现 has_path_sum(root, target_sum) 函数。
"""

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    # TODO: implement here
    if not root:
        return False
    # 递归检查左子树和右子树，更新 target_sum 减去当前节点的值
    has_path_sum_left = has_path_sum(root.left, target_sum - root.val)
    has_path_sum_right = has_path_sum(root.right, target_sum - root.val)
    result = has_path_sum_left or has_path_sum_right
    # 如果当前节点是叶子节点，检查路径和是否等于 target_sum
    if not root.left and not root.right:
        result = (root.val == target_sum)
    return result

def run_tests():
    # Example 1
    #          5
    #        /   \
    #       4     8
    #      /     / \
    #     11    13  4
    #    /  \        \
    #   7    2        1
    root1 = TreeNode(5)
    root1.left = TreeNode(4)
    root1.right = TreeNode(8)
    root1.left.left = TreeNode(11, left=TreeNode(7), right=TreeNode(2))
    root1.right.left = TreeNode(13)
    root1.right.right = TreeNode(4, right=TreeNode(1))
    assert has_path_sum(root1, 22) is True

    # Example 2
    #      1
    #     / \
    #    2   3
    root2 = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
    assert has_path_sum(root2, 5) is False

    # Empty tree
    assert has_path_sum(None, 0) is False

    # Single node equals target
    assert has_path_sum(TreeNode(1), 1) is True

    # Single node does not equal target
    assert has_path_sum(TreeNode(1), 2) is False

    # Negative values
    #      -2
    #        \
    #        -3
    root3 = TreeNode(-2, right=TreeNode(-3))
    assert has_path_sum(root3, -5) is True

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
