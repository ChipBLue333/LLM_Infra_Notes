# 模式总结 (Patterns)

这里将记录你掌握和学习到的通用算法与工程化模式。

## 模式 1：哈希表边历边存 (Hash Map One-Pass Lookup)

**适用场景**：
当需要在数组中以较快速度寻找满足特定关系（例如两数之和等于 target）的两个元素时。

**核心思想**：
- 避免使用双重 `for` 循环向后盲目搜索（导致时间复杂度 $O(n^2)$）。
- 建立一个字典（哈希表）作为“记事本”，在一次遍历的过程中记录“已经看过的元素及其关联信息（如索引）”。
- 每次拿到一个新元素，计算出理论上与之匹配的“那一半”（`complement`），并直接在字典中查询。
- 由于字典的查询时间复杂度是 $O(1)$，通过这种**空间换时间**的手法，能将整体时间复杂度缩减至 $O(n)$。

**代码骨架**：
```python
seen_map = {}
for i, num in enumerate(nums):
    complement = target - num  # 计算需要的配对项
    if complement in seen_map:
        return [seen_map[complement], i]  # 找到配对，直接返回
    seen_map[num] = i  # 记录当前遇到的元素
```


## 模式 2：双指针 - 逆向填坑 (Two Pointers - Backward In-place)

**适用场景**：
在数组合并、字符串替换等场景中，要求**原地修改 (In-place)** 且目标数组的尾部有充足空间的情况。

**核心思想**：
- 如果从前往后遍历并修改，很容易把尚未读取的有效数据覆盖掉。如果想要避免被覆盖，就不得不把后面的元素全体平移，导致 $O(n^2)$ 的时间复杂度。
- 既然尾部是空的，不如直接**从后往前**遍历，谁应该排在最后，就把谁放进最后的“坑”里。这样完美避免了冲突。
- 空间复杂度降为 $O(1)$，时间复杂度为 $O(n)$。


## 模式 3：二分查找 - 找到位置或插入点 (Binary Search - Lower Bound)

**适用场景**：
当数组已经有序，需要在 O(log n) 时间内查找目标值，或者找到目标值应该插入的位置。

**核心思想**：
- 使用 `left` 和 `right` 维护搜索区间。
- 如果 `nums[mid] < target`，说明答案不可能在 `mid` 及其左侧，移动 `left = mid + 1`。
- 如果 `nums[mid] > target`，说明答案在左侧，移动 `right = mid - 1`。
- 如果相等，直接返回 `mid`。
- 如果循环结束仍未找到，`left` 就是 target 应该插入的位置。

**代码骨架**：
```python
left, right = 0, len(nums) - 1
while left <= right:
    mid = left + (right - left) // 2
    if nums[mid] == target:
        return mid
    if nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
return left
```


## 模式 4：链表反转 - 三指针迭代 (Linked List Reverse)

**适用场景**：
当需要原地反转单链表，或者在链表题中局部改变一段节点的方向。

**核心思想**：
- 单链表只能通过 `next` 往后走，所以修改 `current.next` 之前必须先保存原来的下一个节点。
- 使用 `previous` 表示已经反转好的部分。
- 使用 `current` 表示当前正在处理的节点。
- 使用 `next_node` 临时保存后续链表入口，避免断链。

**代码骨架**：
```python
previous = None
current = head

while current is not None:
    next_node = current.next
    current.next = previous
    previous = current
    current = next_node

return previous
```


## 模式 5：双树同步递归 (Two-Tree Synchronized Recursion)

**适用场景**：
当题目要求同时比较两棵树的结构和值，例如 Same Tree、Subtree of Another Tree 等。

**核心思想**：
- 每一层递归都同时拿到两个节点。
- 先处理空节点边界：
  - 两个都为空，通常表示当前部分相同。
  - 只有一个为空，表示结构不同。
- 两个节点都存在时，再比较节点值。
- 当前节点通过后，继续同方向递归比较左右子树。

**代码骨架**：
```python
def same(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False

    return same(p.left, q.left) and same(p.right, q.right)
```


## 模式 6：镜像递归 (Mirror Recursion)

**适用场景**：
当题目出现“对称”“镜像”“翻转后相同”等关键词，例如 Symmetric Tree。

**核心思想**：
- 镜像不是同方向比较，而是交叉方向比较。
- 左子树的左边，要和右子树的右边比较。
- 左子树的右边，要和右子树的左边比较。

**代码骨架**：
```python
def mirror(left, right):
    if not left and not right:
        return True
    if not left or not right:
        return False
    if left.val != right.val:
        return False

    return mirror(left.left, right.right) and mirror(left.right, right.left)
```


## 模式 7：根到叶路径递归 (Root-to-Leaf Path Recursion)

**适用场景**：
当题目要求判断或收集“从根节点到叶子节点”的路径，例如 Path Sum、Binary Tree Paths。

**核心思想**：
- 递归过程中携带路径状态，可以是“剩余目标值”，也可以是“当前累计和”。
- 空节点通常不是合法路径。
- 叶子节点是关键判断点，因为路径必须到叶子才算完整。
- 不能在中间节点提前判定成功。

**代码骨架**：
```python
def has_path(root, target):
    if not root:
        return False

    if not root.left and not root.right:
        return root.val == target

    remaining = target - root.val
    return has_path(root.left, remaining) or has_path(root.right, remaining)
```
