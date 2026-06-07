"""
Problem 009: Reverse Linked List

Difficulty:
Easy

Topic:
Linked List / Pointer

Description:
给定一个单链表的头节点 head，请你反转这个链表，并返回反转后的头节点。

单链表中的每个节点只有两个信息：
- val: 当前节点的值
- next: 指向下一个节点的指针

你需要通过修改节点之间的 next 指针来完成反转。

Input:
head: Optional[ListNode] - 一个单链表的头节点，可能为空

Output:
Optional[ListNode] - 反转后的链表头节点

Examples:
Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
- 链表中节点的数量范围是 [0, 5000]
- -5000 <= Node.val <= 5000

Task:
实现 reverse_list(head) 函数。
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    # TODO: implement here
    # 要实现链表反转
    # 输入是头节点 要找到尾部需要遍历一遍
    # 断开链表前先保存后路 next_node = current.next
    previous = None # 反转后当前节点的前一个节点
    current = head  # 反转前当前节点
    next_node = None    # 反转前当前节点的下一个节点
    while current is not None:
        next_node = current.next  # 保存当前节点的下一个节点
        current.next = previous   # 反转当前节点的指针  相当于本来在当前节点后面 但是现在放在当前节点前面
        previous = current        # 更新previous为当前节点  由于接下来要处理下一个节点 所以当前节点应该要变成前一个节点
        current = next_node       # 移动到下一个节点
    return previous  # 最后previous会指向新的头节点



def build_linked_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    values = []
    current = head
    while current is not None:
        values.append(current.val)
        current = current.next
    return values


def run_tests():
    head = build_linked_list([1, 2, 3, 4, 5])
    assert linked_list_to_list(reverse_list(head)) == [5, 4, 3, 2, 1]

    head = build_linked_list([1, 2])
    assert linked_list_to_list(reverse_list(head)) == [2, 1]

    head = build_linked_list([1])
    assert linked_list_to_list(reverse_list(head)) == [1]

    head = build_linked_list([])
    assert linked_list_to_list(reverse_list(head)) == []

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
