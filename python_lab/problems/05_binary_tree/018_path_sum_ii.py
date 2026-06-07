"""
Problem 018: Path Sum II

Difficulty:
Medium

Topic:
Tree Traversal / DFS / Recursion / Backtracking

Description:
给定一棵二叉树的根节点 root 和一个整数 target_sum，返回所有从根节点到叶子节点的路径，
这些路径上的节点值之和必须等于 target_sum。

每条路径需要用一个整数列表表示。
路径必须从根节点开始，并且必须到叶子节点结束。

Input:
root: Optional[TreeNode] - 二叉树的根节点
target_sum: int - 目标路径和

Output:
List[List[int]] - 所有满足路径和等于 target_sum 的根到叶路径

Examples:
Example 1:
Input:
root = [5,4,8,11,null,13,4,7,2,null,null,5,1]
target_sum = 22
Output:
[[5,4,11,2], [5,8,4,5]]

Explanation:
原树：
          5
        /   \
       4     8
      /     / \
     11    13  4
    /  \      / \
   7    2    5   1

满足目标和 22 的根到叶路径有：
5 -> 4 -> 11 -> 2
5 -> 8 -> 4 -> 5

Example 2:
Input:
root = [1,2,3]
target_sum = 5
Output:
[]

Example 3:
Input:
root = []
target_sum = 0
Output:
[]

Constraints:
- 树中节点的数量在 [0, 5000] 区间内。
- -1000 <= Node.val <= 1000
- -1000 <= target_sum <= 1000

Task:
实现 path_sum(root, target_sum) 函数。
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


def path_sum(root: Optional[TreeNode], target_sum: int) -> List[List[int]]:
    # TODO: implement here
    # 空树返回空列表
    if not root:
        return []
    # 访问到叶子节点时 判断路径和是否等于目标值
    if not root.left and not root.right:
        if root.val == target_sum:
            return [[root.val]]  # 返回包含当前节点值的路径列表
        return []  # 不满足条件 返回空列表
    # 递归访问左右子树
    paths = []  # 当前节点的路径列表
    left_paths = path_sum(root.left, target_sum - root.val)
    right_paths = path_sum(root.right, target_sum - root.val)
    # 将当前节点的值与子树路径连接起来
    # 左右子树分别遍历
    for path in left_paths + right_paths:
        paths.append([root.val] + path)  # 将当前节点的值与子树路径连接起来
    return paths



def normalize(paths: List[List[int]]) -> List[List[int]]:
    return sorted(paths)


def run_tests():
    # Example 1
    #          5
    #        /   \
    #       4     8
    #      /     / \
    #     11    13  4
    #    /  \      / \
    #   7    2    5   1
    root1 = TreeNode(5)
    root1.left = TreeNode(4)
    root1.right = TreeNode(8)
    root1.left.left = TreeNode(11, left=TreeNode(7), right=TreeNode(2))
    root1.right.left = TreeNode(13)
    root1.right.right = TreeNode(4, left=TreeNode(5), right=TreeNode(1))
    assert normalize(path_sum(root1, 22)) == normalize([[5, 4, 11, 2], [5, 8, 4, 5]])

    # No valid path
    root2 = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
    assert path_sum(root2, 5) == []

    # Empty tree
    assert path_sum(None, 0) == []

    # Single node equals target
    root3 = TreeNode(1)
    assert path_sum(root3, 1) == [[1]]

    # Single node does not equal target
    root4 = TreeNode(1)
    assert path_sum(root4, 2) == []

    # Negative values
    #      -2
    #        \
    #        -3
    root5 = TreeNode(-2, right=TreeNode(-3))
    assert path_sum(root5, -5) == [[-2, -3]]

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
