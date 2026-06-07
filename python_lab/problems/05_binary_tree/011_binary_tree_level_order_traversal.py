"""
Problem 011: Binary Tree Level Order Traversal

Difficulty:
Medium

Topic:
Tree Traversal / BFS / Queue

Description:
给你二叉树的根节点 root ，返回其节点值的“层序遍历”（Level Order Traversal）。
（即逐层地，从左到右访问所有节点，将每一层的节点值放在一个单独的列表中，最终返回一个二维列表）。

树的层序遍历需要使用 广度优先搜索（BFS）。
为了实现高效的 BFS，建议在 Python 中使用 collections.deque 作为队列（Queue）。

Input:
root: Optional[TreeNode] - 二叉树的根节点

Output:
List[List[int]] - 按层分组的节点值列表

Examples:
Example 1:
    3
   / \
  9  20
    /  \
   15   7
Input: root = [3,9,20,null,null,15,7]
Output: [[3], [9, 20], [15, 7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
- 树中节点数目在范围 [0, 2000] 内
- -1000 <= Node.val <= 1000

Task:
实现 level_order(root) 函数。
"""

from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    # TODO: implement here
    if not root:
        return []
    result = []
    # 把原树放进一个双端队列中
    queue = deque([root])   
    # 只要队列不空，就继续处理
    while queue:
        level = []  # 存储当前层的节点值
        size = len(queue)  # 为什么这个是当前层的节点数？因为每次循环开始时，队列中只包含当前层的节点，下一层的节点还没有被加入队列，所以 size 就是当前层的节点数。
        # 处理当前层的所有节点
        for _ in range(size):
            node = queue.popleft()
            level.append(node.val)
            # 将下一层的节点加入队列
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result


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
    assert level_order(root1) == [[3], [9, 20], [15, 7]]

    # Example 2
    root2 = TreeNode(1)
    assert level_order(root2) == [[1]]

    # Example 3
    assert level_order(None) == []

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
