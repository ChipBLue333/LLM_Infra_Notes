"""
Problem 010: Binary Tree Inorder Traversal

Difficulty:
Easy

Topic:
Tree Traversal / DFS / Stack

Description:
给定一个二叉树的根节点 root，返回它的中序遍历（Inorder Traversal）。

中序遍历的访问顺序是：左子树 -> 根节点 -> 右子树。

推荐先尝试使用递归实现，然后再尝试使用迭代（栈）来实现。

Input:
root: Optional[TreeNode] - 二叉树的根节点

Output:
List[int] - 中序遍历得到的值列表

Examples:
Example 1:
Input: root = [1,null,2,3]
    1
     \
      2
     /
    3
Output: [1, 3, 2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Constraints:
- 树中节点数目在范围 [0, 100] 内
- -100 <= Node.val <= 100

Task:
实现 inorder_traversal(root) 函数。
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """
    # 递归解法（已注释）
    # 定义一个空列表来存储中序遍历的结果
    result = []
    # 如果是空树，直接返回空列表
    if root is None:
        return result
    # 非空树，递归遍历左子树
    result.extend(inorder_traversal(root.left))
    # 访问根节点
    result.append(root.val)
    # 递归遍历右子树
    result.extend(inorder_traversal(root.right))
    return result
    """
    
    # TODO: 使用 栈（迭代） 实现中序遍历
    # 提示：你可以用一个普通的 Python 列表当做栈 (stack = [])
    # 也可以用一个 current 变量记录当前遍历到的节点
    result = []
    stack = []
    current = root
    if current is None:
        return result
    while current is not None or stack:
        # 先一直往左子树走，直到没有左子树了
        while current is not None:
            stack.append(current)
            current = current.left
        # 现在 current 是 None，说明我们到了最左边的节点
        # 从栈顶弹出一个节点，这就是当前访问的节点
        current = stack.pop()
        result.append(current.val)  # 访问当前节点
        # 然后转向右子树继续遍历
        current = current.right
    return result

def run_tests():
    # Helper to build simple tree just for tests
    # root = [1,null,2,3]
    node3 = TreeNode(3)
    node2 = TreeNode(2, left=node3)
    root1 = TreeNode(1, right=node2)
    assert inorder_traversal(root1) == [1, 3, 2]

    # root = []
    assert inorder_traversal(None) == []

    # root = [1]
    assert inorder_traversal(TreeNode(1)) == [1]
    
    #     2
    #    / \
    #   1   3
    root2 = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
    assert inorder_traversal(root2) == [1, 2, 3]

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
