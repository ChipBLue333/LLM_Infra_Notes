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

## 2026年5月12日: 回溯算法 (Backtracking) 核心模式

### 1. 隐式回溯 vs 显式回溯
- **隐式回溯**: `backtrack(path + [val])`
  - 依靠 Python 列表 `+` 产生全新对象传入下一层。
  - 优点：代码极简，无需手动 `pop` 和 `copy()`，不易出错。
  - 缺点：每次生成新列表，空间与时间开销较大。
- **显式回溯**: `path.append(val); backtrack(); path.pop()`
  - 依靠全局或闭包内唯一的列表对象维护状态。
  - 优点：极致的性能，省去不必要的内存分配。
  - 缺点：保存结果时必须深拷贝 `result.append(path.copy())`，且容易遗忘 `pop`。

### 2. 回溯中的去重 (Deduplication)
- **前提**: 遇到去重问题，第一步永远是 **排序 `nums.sort()`**。
- **组合去重 (Combination Sum II)**: 
  - `if i > start and candidates[i] == candidates[i - 1]: continue`
  - 只在“层级”上去重，放行“深度”上的重复元素。
- **排列去重 (Permutations II)**:
  - `if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]: continue`
  - 利用 `used` 数组或判断树状结构状态，区分同树枝的重复和同树层的重复。

## 2026年5月15日: 二维网格 DFS / 回溯

### 适用场景

当题目给出二维矩阵 / 网格，并要求从某个格子出发向上下左右搜索，例如 Word Search。

### 核心思想

- 递归状态通常包含当前位置和当前进度：`dfs(i, j, k)`。
- `i, j` 表示当前所在格子。
- `k` 表示当前要匹配目标字符串或目标路径的第几个元素。
- 每次进入一个格子前，先判断越界、重复访问、当前字符是否匹配。
- 如果当前格子合法，就标记访问，然后向四个方向递归。
- 递归结束后恢复访问状态。

### 代码骨架

```python
def dfs(i, j, k):
    if i < 0 or i >= m or j < 0 or j >= n:
        return False
    if board[i][j] != word[k]:
        return False
    if k == len(word) - 1:
        return True

    temp = board[i][j]
    board[i][j] = "#"

    found = (
        dfs(i + 1, j, k + 1)
        or dfs(i - 1, j, k + 1)
        or dfs(i, j + 1, k + 1)
        or dfs(i, j - 1, k + 1)
    )

    board[i][j] = temp
    return found
```

### 易错点

- 忘记恢复 `board[i][j]`，导致其他路径被错误影响。
- 只从一个起点开始搜索，忘记外层双循环枚举所有起点。
- 把“同一条路径不能重复访问”和“所有路径都不能重复访问”混淆。
- 终止条件放错位置：匹配完最后一个字符后应直接返回成功。

## 2026年5月19日: 二维路径 DP

### 适用场景

当题目给出二维网格、三角形数组或类似“只能从某些方向移动”的结构，并要求计算路径数量、最小路径和或最大路径和。

### 核心思想

- 第一步永远是定义状态，例如 `dp[i][j]` 表示到达位置 `(i, j)` 的路径数量或最优代价。
- 第二步处理边界初始化。第一行、第一列、三角形左右边界通常没有完整的两个来源。
- 第三步写状态转移。普通位置通常从若干合法来源中汇总答案。
- 最后确认答案位置。不是所有二维 DP 都返回右下角；Triangle 这类题返回最后一行的最小值。

### 常见转移

路径数量：

```python
dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
```

有障碍路径数量：

```python
if obstacle_grid[i][j] == 1:
    dp[i][j] = 0
else:
    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
```

矩形网格最小路径和：

```python
dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
```

三角形最小路径和：

```python
if j == 0:
    dp[i][j] = dp[i - 1][j] + triangle[i][j]
elif j == i:
    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
else:
    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
```

### 易错点

- 把“路径数量”题的相加逻辑误用到“路径代价最优”题。
- 第一行和第一列初始化时忘记障碍物或 cost 累加。
- Triangle 中误以为下一行可以任选数字；实际只能向下或向下向右。
- 最终答案位置判断错误：矩形路径题多是右下角，Triangle 是最后一行最小值。

## 2026年5月20日: 背包 DP

### 适用场景

当题目出现“从一组数中选择若干个”“每个数能否重复使用”“凑出某个目标和”“求最少数量 / 方案数量 / 是否可达”等描述时，优先考虑背包 DP。

### 核心判断顺序

1. 状态值是什么：
   - 最优值：例如最少硬币数，通常用 `min` 或 `max`。
   - 方案数：例如组合数量，通常用 `+=` 累加。
   - 可达性：例如能否凑出某个和，通常用布尔值和 `or`。
2. 物品能不能重复使用：
   - 可以重复使用：完全背包。
   - 只能使用一次：0/1 背包。
3. 是否关心顺序：
   - 不关心顺序：组合。
   - 关心顺序：排列。

### 完全背包

每个物品可以重复使用。

最少硬币数：

```python
dp = [amount + 1] * (amount + 1)
dp[0] = 0

for x in range(1, amount + 1):
    for coin in coins:
        if coin <= x:
            dp[x] = min(dp[x], dp[x - coin] + 1)
```

组合数量：

```python
dp = [0] * (amount + 1)
dp[0] = 1

for coin in coins:
    for x in range(coin, amount + 1):
        dp[x] += dp[x - coin]
```

### 0/1 背包

每个物品只能使用一次，因此容量通常倒序遍历，避免同一个物品在一轮中被重复使用。

可达性判断：

```python
dp = [False] * (target + 1)
dp[0] = True

for num in nums:
    for x in range(target, num - 1, -1):
        dp[x] = dp[x] or dp[x - num]
```

### 易错点

- 把不可达状态初始化成 0，导致程序误以为所有金额都已经可达。
- 方案数量题写成覆盖赋值，例如 `dp[x] = dp[x - coin]`，会丢掉已有方案。
- 0/1 背包正序遍历容量，导致同一个数字在一轮里被重复使用。
- 完全背包和 0/1 背包混淆：前者允许重复使用，后者只能使用一次。
- 组合和排列混淆：组合题通常先遍历物品，排列题通常先遍历容量。

## 2026年5月21日: 符号选择转子集和

### 适用场景

当题目要求给数组中的每个数字添加 `+` 或 `-`，并统计能否达到某个目标值，或者统计达到目标值的方案数量时，可以考虑把问题转换为子集和。

### 核心推导

设：

```text
positive = 所有加号数字的和
negative = 所有减号数字的和
total = sum(nums)
```

根据题意：

```text
positive - negative = target
positive + negative = total
```

两式相加：

```text
2 * positive = target + total
positive = (target + total) / 2
```

所以原问题变成：

```text
从 nums 中选若干个数字，使它们的和等于 positive，一共有多少种选法。
```

### DP 定义

```python
dp[x] = 凑出和 x 的方案数量
```

初始化：

```python
dp[0] = 1
```

转移：

```python
for num in nums:
    for x in range(positive, num - 1, -1):
        dp[x] += dp[x - num]
```

### 合法性判断

转换前要判断：

- `total + target` 不能是负数。
- `total + target` 必须是偶数。

否则 `positive` 不是合法容量，直接返回 `0`。

### 易错点

- 直接暴力枚举所有符号组合，这是 `O(2^n)`。
- 忘记 `positive` 是加号组的和，不是原始 `target`。
- 容量正序遍历，导致同一个数字在一轮中被重复使用。
- 忘记数组中 `0` 的特殊性：`+0` 和 `-0` 值一样，但属于两种不同符号方案。

## 2026年5月22日: 二维前缀 DP / Longest Common Subsequence

### 适用场景

当题目涉及两个序列之间的“最长共同部分”，并且要求保持原始相对顺序时，可以优先考虑 LCS 模式。

典型信号：

- 两个字符串 / 两个数组。
- 可以跳过元素，但不能改变顺序。
- 求最长公共子序列长度。
- 求最多不相交连线数量。

### 核心状态定义

```python
dp[i][j] = 第一个序列的前 i 个元素 和 第二个序列的前 j 个元素 的最优结果
```

通常把 DP 表开成：

```python
dp = [[0] * (n + 1) for _ in range(m + 1)]
```

第 0 行和第 0 列表示其中一个序列为空的情况，结果自然是 0。

### 为什么比较“末尾”

因为 `dp[i][j]` 讨论的是两个前缀：

```text
seq1[:i]
seq2[:j]
```

这两个前缀当前新增纳入考虑的元素分别是：

```python
seq1[i - 1]
seq2[j - 1]
```

它们就是当前两个前缀的末尾元素。

### 核心转移

如果当前两个末尾元素相等：

```python
dp[i][j] = dp[i - 1][j - 1] + 1
```

含义：这两个元素可以配成一对，答案来自更短前缀的结果再加 1。

如果当前两个末尾元素不相等：

```python
dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
```

含义：

- `dp[i - 1][j]`：跳过第一个序列当前末尾后的最优解。
- `dp[i][j - 1]`：跳过第二个序列当前末尾后的最优解。
- 当前两个末尾不能配对，所以继承这两个选择中更好的结果。

### 不相交线和 LCS 的关系

对于两条连接线：

```text
(i1, j1)
(i2, j2)
```

如果：

```text
i1 < i2
```

那么为了不相交，必须有：

```text
j1 < j2
```

所以不相交线的本质是：匹配对在两个数组中的下标序列都单调递增。这正好等价于“选出的公共元素必须保持两个序列中的相对顺序”，也就是 LCS。

### 代码骨架

```python
m = len(seq1)
n = len(seq2)
dp = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if seq1[i - 1] == seq2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

return dp[m][n]
```

### 易错点

- 忘记 `i` / `j` 是前缀长度，访问原序列时要用 `i - 1` / `j - 1`。
- 不理解不相等时为什么取 `max(dp[i - 1][j], dp[i][j - 1])`；本质是在比较“跳过左边当前元素”和“跳过右边当前元素”后的最优解。
- 在不相交线问题中，误比较单条线内部的 `i` 和 `j` 大小；正确做法是比较多条匹配之间的相对顺序。

## 2026年5月23日: 回文字符串 DP / 区间 DP

### 适用场景

当题目围绕一个字符串的某个连续区间或回文结构展开时，可以考虑区间 DP 或中心扩展。

典型信号：

- 求最长回文子序列。
- 求最长回文子串。
- 统计回文子串数量。
- 题目需要判断 `s[i:j+1]` 这一段是否满足某种性质。

### 子序列和子串的区别

```text
子序列：可以跳过字符，但不能改变相对顺序。
子串：必须连续。
```

例子：

```text
s = "bbbab"
```

- 最长回文子序列可以是 `"bbbb"`，可以跳过中间字符。
- 最长回文子串只能取连续片段，例如 `"bbb"`。

### 最长回文子序列

状态定义：

```python
dp[i][j] = s[i:j+1] 这个区间内的最长回文子序列长度
```

核心转移：

```python
if s[i] == s[j]:
    dp[i][j] = dp[i + 1][j - 1] + 2
else:
    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
```

初始化：

```python
dp[i][i] = 1
```

遍历顺序：

```python
for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
        ...
```

`i` 倒序的原因是：`dp[i][j]` 会依赖 `dp[i + 1][j]`，也就是下一行状态，所以必须先算更大的 `i`。

### 回文子串判断

状态定义：

```python
dp[i][j] = s[i:j+1] 是否是回文子串
```

状态值是布尔值，不是长度。

核心转移：

```python
if s[i] == s[j]:
    if j - i <= 2:
        dp[i][j] = True
    else:
        dp[i][j] = dp[i + 1][j - 1]
```

含义：

- 长度 1：单个字符一定是回文。
- 长度 2：两端相等就是回文。
- 长度 3：两端相等，中间单字符天然回文。
- 更长区间：两端相等后，还必须保证中间区间也是回文。

### 最长回文子串

在回文子串判断基础上，额外维护答案位置：

```python
start = 0
max_len = 1
```

每次发现 `dp[i][j] == True`，如果当前长度更长，就更新：

```python
start = i
max_len = j - i + 1
```

最终返回：

```python
return s[start:start + max_len]
```

### 回文子串计数

在回文子串判断基础上，额外维护计数：

```python
count = 0
```

每次发现一个位置区间 `[i, j]` 是回文子串：

```python
count += 1
```

注意：相同内容但位置不同的子串需要分别计数。

### 遍历顺序原则

不要死背循环方向，要看依赖项。

如果 `dp[i][j]` 依赖：

```python
dp[i + 1][j - 1]
```

那么需要保证这个更短的中间区间先算完。

常见合法顺序有两种：

```python
# i 倒序，j 正序
for i in range(n - 1, -1, -1):
    for j in range(i, n):
        ...
```

```python
# j 正序，i 正序
for j in range(n):
    for i in range(j + 1):
        ...
```

第一种常用于区间 DP；第二种常用于按右边界推进的回文子串判断。

### 易错点

- 把回文子序列和回文子串混在一起：子序列可以跳过字符，子串必须连续。
- 把回文子串的 `dp[i][j]` 写成长度；它通常应该是布尔值。
- 只判断 `s[i] == s[j]`，忘记中间区间也必须是回文。
- 忘记长度 1、2、3 的基础情况。
- 不理解为什么 `i` 要倒序：本质是为了先算依赖项，不是模板要求。
