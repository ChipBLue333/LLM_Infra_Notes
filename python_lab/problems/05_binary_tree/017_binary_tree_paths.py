"""
Problem 017: Binary Tree Paths

Difficulty:
Easy

Topic:
Tree Traversal / DFS / Recursion

Description:
给定一棵二叉树的根节点 root，返回所有从根节点到叶子节点的路径。

每条路径需要用字符串表示，节点值之间使用 "->" 连接。

叶子节点是指没有左孩子也没有右孩子的节点。

Input:
root: Optional[TreeNode] - 二叉树的根节点

Output:
List[str] - 所有从根节点到叶子节点的路径字符串

Examples:
Example 1:
Input:
root = [1,2,3,null,5]
Output:
["1->2->5", "1->3"]

Explanation:
原树：
      1
     / \
    2   3
     \
      5

从根到叶子的路径有两条：
1 -> 2 -> 5
1 -> 3

Example 2:
Input:
root = [1]
Output:
["1"]

Example 3:
Input:
root = []
Output:
[]

Constraints:
- 树中节点的数量在 [0, 100] 区间内。
- -100 <= Node.val <= 100

Task:
实现 binary_tree_paths(root) 函数。
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


def binary_tree_paths(root: Optional[TreeNode]) -> List[str]:
    # TODO: implement here
    # 空树 直接返回空列表
    if not root:
        return []
    # 当访问到叶子节点时
    if not root.left and not root.right:
        return [str(root.val)]  
    # 实际返回的就是叶子节点值的字符串形式 但是递归调用时会在列表后面添加上父节点的值和箭头

    # 递归访问左右子树
    paths = []  # 当前节点的路径列表
    left_paths = binary_tree_paths(root.left)
    right_paths = binary_tree_paths(root.right)
    # 将当前节点的值与子树路径连接起来
    for path in left_paths + right_paths: 
        paths.append(str(root.val) + "->" + path)
    return paths    



def run_tests():
    # Example 1
    #      1
    #     / \
    #    2   3
    #     \
    #      5
    root1 = TreeNode(1)
    root1.left = TreeNode(2, right=TreeNode(5))
    root1.right = TreeNode(3)
    assert sorted(binary_tree_paths(root1)) == sorted(["1->2->5", "1->3"])

    # Single node
    root2 = TreeNode(1)
    assert binary_tree_paths(root2) == ["1"]

    # Empty tree
    assert binary_tree_paths(None) == []

    # Only left chain
    # 1 -> 2 -> 3
    root3 = TreeNode(1, left=TreeNode(2, left=TreeNode(3)))
    assert binary_tree_paths(root3) == ["1->2->3"]

    # Negative values
    #     -1
    #    /  \
    #  -2   -3
    root4 = TreeNode(-1, left=TreeNode(-2), right=TreeNode(-3))
    assert sorted(binary_tree_paths(root4)) == sorted(["-1->-2", "-1->-3"])

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
