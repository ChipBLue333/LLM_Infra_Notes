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


## 模式 8：跳跃游戏 - 覆盖范围贪心 (Jump Game Greedy Coverage)

**适用场景**：
数组中每个位置表示可以向前扩展的最大距离，题目要求判断能否到达终点，或求到达终点的最少跳跃次数。

### Jump Game I：判断能否到达

核心变量：

```python
farthest = 0
```

含义：当前已经能够到达的最远下标。

核心更新：

```python
if i > farthest:
    return False

farthest = max(farthest, i + nums[i])
```

解释：
- `i + nums[i]` 表示从当前位置出发，最远可以跳到哪里。
- `max(...)` 表示最远可达范围只能扩大，不能倒退。
- 如果 `i > farthest`，说明当前位置本身不可达，后续也无法继续推进。

成功条件：

```python
farthest >= len(nums) - 1
```

含义：最远可达范围已经覆盖最后一个下标。

### Jump Game II：计算最少跳跃次数

核心变量：

```python
jumps = 0
current_end = 0
farthest = 0
```

含义：
- `jumps`：已经跳了几次。
- `current_end`：当前跳跃次数能够覆盖到的最右边界。
- `farthest`：在当前覆盖范围内，下一跳能够到达的最远位置。

核心骨架：

```python
for i in range(len(nums) - 1):
    farthest = max(farthest, i + nums[i])

    if i == current_end:
        jumps += 1
        current_end = farthest
```

关键点：
- 不遍历最后一个下标，因为到达终点后不需要再从终点起跳。
- 只有当 `i == current_end` 时，才说明当前这一层覆盖范围扫描完，需要增加一次跳跃。
- `current_end = farthest` 表示进入下一跳可以覆盖的新区间。

### 易错点

- 把 `farthest` 直接赋值成 `i + nums[i]`，导致最远范围可能倒退。
- 在 Jump Game II 中遍历到最后一个下标，导致多计一次跳跃。
- 每走一步就 `jumps += 1`，把“经过一个下标”和“跳跃一次”混在一起。
- 没区分 `current_end` 和 `farthest`：前者是当前层边界，后者是下一层最远边界。


## 模式 9：贪心 - 全局可行与局部重置 (Global Feasibility + Local Reset)

**适用场景**：
题目存在一个整体资源约束，同时需要找到一个起点、分界点或候选方案。局部尝试失败后，可以证明一整段候选都不可能成功。

典型题目：
- Problem 053: Gas Station

### 核心思想

先判断全局是否可行：

```python
if sum(gas) < sum(cost):
    return -1
```

如果全局资源不足，任何局部策略都救不了。

然后从左到右扫描，维护当前候选起点下的局部状态：

```python
start = 0
current_gas = 0

for i in range(len(gas)):
    current_gas += gas[i] - cost[i]

    if current_gas < 0:
        start = i + 1
        current_gas = 0
```

### 为什么这是贪心

当从 `start` 走到 `i` 时出现亏空：

```text
sum(start..i) < 0
```

说明 `start` 不可能作为答案。

更重要的是，`start` 到 `i` 中间的所有位置也都不可能作为答案。因为在第一次亏空之前，从 `start` 到中间位置之前的累计值都没有亏空；如果从中间某个位置重新开始，只会少掉前面那段非负收益，走到 `i` 时更不可能不亏。

所以可以直接跳到：

```python
start = i + 1
```

这一步“一次性排除一整段候选”，就是贪心决策。

### 易错点

- 误以为这只是普通遍历，忽略了“跳过一整段候选”的证明。
- 只判断局部油量，不判断总油量，导致总资源不足时仍返回某个起点。
- `current_gas < 0` 后忘记重置局部油量。
- 把 `start` 设成 `i`，正确应该是 `i + 1`。


## 模式 10：贪心 - 边界闭合切分 (Boundary Closure Partition)

**适用场景**：
题目要求把序列切成尽可能多的合法片段，而片段内的元素会对片段右边界提出约束。

典型题目：
- Problem 054: Partition Labels

### 核心思想

先预处理每个元素最后一次出现的位置：

```python
last = {}
for i, char in enumerate(s):
    last[char] = i
```

再从左到右扫描，维护当前片段必须覆盖到的最远边界：

```python
start = 0
end = 0
parts = []

for i, char in enumerate(s):
    end = max(end, last[char])

    if i == end:
        parts.append(end - start + 1)
        start = i + 1
```

### 为什么这是贪心

当前片段里出现过的所有字符，都必须被当前片段完整包含。

因此 `end` 表示：

```text
当前片段内所有字符最后出现位置的最大值
```

当 `i == end` 时，说明当前片段内的所有字符都已经完整覆盖。如果此时不切，而是继续往后扩展，只会让当前片段变长、片段数量变少，不会带来更优解。

所以边界一闭合就立刻切分。

### 易错点

- 不先记录最后出现位置，导致不知道当前片段必须延伸到哪里。
- 看到一个重复字符就切分，忽略它后面可能还有更晚的位置。
- 忘记更新 `start`，导致片段长度计算错误。
- 把 `end` 理解成当前字符的最后位置，而不是当前片段内所有字符最后位置的最大值。


## 2026年5月27日: 贪心 - 区间调度 (Interval Scheduling)

### 适用场景

当题目要求从一组区间中保留尽可能多的互不重叠区间，或删除尽可能少的区间时，可以考虑区间调度贪心。

典型题目：
- Problem 055: Non-overlapping Intervals

### 核心思想

把“删除最少区间”转换成：

```text
保留最多的互不重叠区间
```

为了保留更多区间，每次应优先选择结束位置更早的区间。结束越早，留给后面区间的空间越大。

核心骨架：

```python
intervals.sort(key=lambda x: x[1])

removed = 0
prev_end = float("-inf")

for start, end in intervals:
    if start >= prev_end:
        prev_end = end
    else:
        removed += 1

return removed
```

### 为什么这是贪心

在所有当前可选区间中，选择结束最早的区间不会让答案变差。因为它占用的右边界最小，给后续区间留下的可用范围最大。

如果当前区间与已保留区间重叠，由于区间已经按结束位置升序排列，已保留区间一定不会比当前区间更晚结束。因此保留已选区间、移除当前区间是安全的。

### 易错点

- 按开始位置排序后直接贪心，容易保留一个很长的区间，挡住后面多个短区间。
- 把边界相接误判成重叠。本题中 `[1, 2]` 和 `[2, 3]` 不重叠，所以条件是 `start >= prev_end`。
- 忘记 `list.sort()` 会原地修改输入；如果不能修改原列表，应使用 `sorted(...)`。


## 2026年5月29日: 贪心 - 射击点覆盖区间 (Arrow Coverage)

### 适用场景

当题目要求用尽可能少的点、箭、会议室资源或操作次数覆盖一组区间时，可以考虑按结束位置排序，并把当前资源放在当前区间的右边界。

典型题目：
- Problem 056: Minimum Number of Arrows to Burst Balloons

### 核心思想

按区间结束位置排序：

```python
points.sort(key=lambda x: x[1])
```

维护当前箭的位置：

```python
arrows = 0
arrow_pos = float("-inf")

for start, end in points:
    if start > arrow_pos:
        arrows += 1
        arrow_pos = end

return arrows
```

### 为什么这是贪心

当前未被射爆的气球必须用一支箭处理。把箭射在它的结束位置，仍然可以射爆当前气球，同时这个位置在当前气球内部尽可能靠右，更有机会覆盖后面起点更大的气球。

如果后续气球满足：

```text
start <= arrow_pos
```

说明它也能被当前箭射爆。

如果：

```text
start > arrow_pos
```

说明当前箭已经够不到它，必须新增一支箭。

### 易错点

- 把条件写成 `start >= arrow_pos`，会把边界相接误判为需要新箭。
- 忘记边界相接时同一支箭可以同时射爆两个气球。
- 不理解为什么箭放在右边界：不是随便选点，而是在不失去当前气球的前提下尽量靠右。


## 2026年5月29日: 区间 - 合并区间 (Merge Intervals)

### 适用场景

当题目要求把所有重叠区间合并成若干个不重叠区间时，通常按起点排序，然后从左到右维护结果列表。

典型题目：
- Problem 057: Merge Intervals

### 核心思想

按起点排序：

```python
intervals.sort(key=lambda x: x[0])
```

维护结果列表：

```python
merged = []

for start, end in intervals:
    if not merged or merged[-1][1] < start:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)

return merged
```

### 为什么按起点排序

按起点排序后，从左到右扫描时，当前区间只需要和 `merged` 的最后一个区间比较。

如果当前区间和最后一个区间不重叠，那么它也不会和更早的区间重叠；因为更早区间的起点更小，并且已经被合并进结果列表。

### 合并判断

不重叠条件：

```text
last_end < current_start
```

合并条件：

```text
current_start <= last_end
```

本题中边界相接也要合并，所以 `[1, 4]` 和 `[4, 5]` 会合并成 `[1, 5]`。

### 易错点

- 写成嵌套循环，重复扫描所有区间；排序后只需要一次线性遍历。
- 遍历时删除原列表，容易造成下标混乱。
- 把边界相接误判成不重叠。
- 忘记合并时右边界要取最大值，而不是直接覆盖成当前区间的结束位置。


## 2026年5月29日: Python 语法 - sort key 与 lambda

### `sort(key=...)`

`list.sort()` 会原地排序原列表。

```python
points.sort(key=lambda x: x[1])
```

含义：
- `points` 是要排序的列表。
- `key` 指定每个元素用什么值参与比较。
- `x` 是列表中的每一个元素。
- `x[1]` 表示取元素的第二项作为排序依据。

### `lambda`

`lambda` 是匿名函数，适合写很短、只用一次的函数。

基本格式：

```python
lambda 参数: 返回值表达式
```

例如：

```python
lambda x: x[1]
```

等价于：

```python
def get_second(x):
    return x[1]
```

### 常见写法

按区间起点排序：

```python
intervals.sort(key=lambda x: x[0])
```

按区间终点排序：

```python
intervals.sort(key=lambda x: x[1])
```

如果不想修改原列表，使用 `sorted`：

```python
sorted_intervals = sorted(intervals, key=lambda x: x[0])
```

## 2026年5月30日: 区间插入三段式

### 适用场景

当区间列表已经按起点升序排列，且内部无重叠，需要插入一个新区间并合并重叠区间。

### 核心思想

把每个旧区间和 `new_interval` 的关系分成三类：

- 旧区间完全在新区间左边：直接加入结果。
- 旧区间和新区间重叠：只更新新区间的左右边界。
- 旧区间完全在新区间右边：先把合并后的新区间加入结果，再加入右侧区间。

因为新区间只能插入一次，需要用状态变量记录它是否已经进入结果。

### 关键判断

```text
interval_end < new_start      -> 完全在左边
interval_start > new_end      -> 完全在右边
否则                          -> 重叠或边界相接
```

如果题目要求边界相接也合并，那么左边和右边判断必须分别使用 `<` 和 `>`。

### 代码骨架

```python
result = []
inserted = False

for interval in intervals:
    if interval[1] < new_interval[0]:
        result.append(interval)
    elif interval[0] > new_interval[1]:
        if not inserted:
            result.append(new_interval)
            inserted = True
        result.append(interval)
    else:
        new_interval[0] = min(new_interval[0], interval[0])
        new_interval[1] = max(new_interval[1], interval[1])

if not inserted:
    result.append(new_interval)
```

## 2026年5月30日: 最小堆管理资源

### 适用场景

当题目需要动态维护“当前最小值”，例如：

- 最早结束的会议室；
- 最小的任务结束时间；
- Top K 问题中的候选值；
- 多路有序列表合并。

### 核心思想

最小堆可以快速拿到当前最小值：

```python
heap[0]
```

Python 中使用 `heapq`：

```python
import heapq

heapq.heappush(heap, value)
smallest = heapq.heappop(heap)
```

### Meeting Rooms II 模式

堆里保存会议室当前占用到的结束时间。

```python
intervals.sort(key=lambda x: x[0])
rooms = []

for start, end in intervals:
    if rooms and rooms[0] <= start:
        heapq.heappop(rooms)
    heapq.heappush(rooms, end)

return len(rooms)
```

### 关键点

- 排序负责按时间顺序处理会议。
- `rooms[0]` 表示最早空出来的会议室。
- `rooms[0] <= start` 表示当前会议可以复用这个会议室。
- `heappush` 表示当前会议占用一个会议室直到 `end`。

## 2026年6月2日: Top K 最小堆

### 适用场景

当题目要求找：

- 第 `k` 大元素；
- 前 `k` 大元素；
- 出现频率最高的 `k` 个元素；
- 评分最高、距离最近、优先级最高的 `k` 个对象。

只要目标是从大量候选中保留最强的 `k` 个，就可以考虑大小为 `k` 的最小堆。

### 核心思想

用最小堆保存当前见过的 top k 候选。

堆顶 `heap[0]` 表示当前 top k 里最弱的那个元素：

- 找第 `k` 大元素时，堆顶是当前前 `k` 大中的最小值。
- 找前 `k` 个高频元素时，堆顶是当前 top k 里频率最低的元素。

当新元素强于堆顶时，用新元素替换堆顶；否则忽略。

### 第 K 大元素代码骨架

```python
import heapq


heap = []

for num in nums:
    if len(heap) < k:
        heapq.heappush(heap, num)
    elif num > heap[0]:
        heapq.heapreplace(heap, num)

return heap[0]
```

### 前 K 个高频元素代码骨架

```python
import heapq


freq = {}
for num in nums:
    freq[num] = freq.get(num, 0) + 1

heap = []
for num, count in freq.items():
    if len(heap) < k:
        heapq.heappush(heap, (count, num))
    elif count > heap[0][0]:
        heapq.heapreplace(heap, (count, num))

return [num for count, num in heap]
```

### 关键点

- Python 的 `heapq` 是最小堆。
- 堆大小保持为 `k`，空间复杂度是 `O(k)`。
- 不要把“排序列表”误认为堆；每次 `sort()` 虽然能得到正确顺序，但复杂度更高。
- 堆中可以保存元组，例如 `(frequency, num)`；Python 会先按第一个元素比较。
- 返回结果顺序如果题目说不限，就不需要额外排序。

## 2026年6月3日: 负数模拟最大堆与 Tuple 状态

### 适用场景

当题目要求找：

- 距离最近的 `k` 个点；
- 数值最小的 `k` 个元素；
- 代价最低的 `k` 个候选；
- 但又需要快速淘汰当前候选中“最大 / 最远 / 最差”的那个元素。

可以维护大小为 `k` 的最大堆。

### Python 中的问题

Python 的 `heapq` 默认是最小堆：

```python
heap[0]
```

永远是当前堆里最小的元素。

如果想模拟最大堆，可以把比较值变成负数：

```python
heapq.heappush(heap, -value)
```

真实值越大，负数越小，因此会出现在最小堆堆顶。

### K Closest Points 模式

找距离原点最近的 `k` 个点时，堆里保存：

```python
(-distance_squared, x, y)
```

含义是：

- `-distance_squared`：用于堆排序。
- `x`：点的 x 坐标。
- `y`：点的 y 坐标。

代码骨架：

```python
import heapq


heap = []

for x, y in points:
    dist = x * x + y * y

    if len(heap) < k:
        heapq.heappush(heap, (-dist, x, y))
    elif dist < -heap[0][0]:
        heapq.heapreplace(heap, (-dist, x, y))

return [[x, y] for _, x, y in heap]
```

### 关键点

- 最大堆的堆顶表示当前最大元素。
- 在本题中，堆顶表示当前保留的 `k` 个点里距离最远的点。
- `heap[0][0]` 是负距离，`-heap[0][0]` 才是真实距离平方。
- `(-dist, x, y)` 是一个三元组 tuple。
- Python 比较 tuple 时从左到右比较，通常先看第一个元素。
- `for _, x, y in heap` 是 tuple 解包；`_` 表示这个值不关心。

## 2026年6月4日: 最小堆多路合并与提前停止

### 适用场景

当输入包含多条已经有序的序列，需要：

- 合并所有序列；
- 找所有序列中的第 `k` 小元素；
- 按顺序持续取出全局最小元素。

可以使用最小堆进行多路合并。

### 核心不变量

堆中只保存每条序列当前还未处理的最小候选。

堆元素通常保存：

```python
(value, sequence_index, element_index)
```

- `value`：参与堆排序的当前候选值。
- `sequence_index`：候选来自哪条序列。
- `element_index`：候选在该序列中的位置。

每次弹出全局最小候选后，只推进它所属的序列。其他序列的当前候选仍然有效。

### 完整多路合并

```python
heap = []
result = []

for sequence_index, sequence in enumerate(sequences):
    if sequence:
        heapq.heappush(heap, (sequence[0], sequence_index, 0))

while heap:
    value, sequence_index, element_index = heapq.heappop(heap)
    result.append(value)

    next_index = element_index + 1
    if next_index < len(sequences[sequence_index]):
        next_value = sequences[sequence_index][next_index]
        heapq.heappush(heap, (next_value, sequence_index, next_index))
```

设所有元素总数为 `N`，序列数量为 `m`：

- Time: `O(N log m)`
- Space: `O(m)`，不计算返回结果

### 第 K 小：提前停止

如果只需要第 `k` 小元素，不需要生成完整合并结果：

```text
初始化候选堆
弹出并推进 k - 1 次
返回下一次弹出的值
```

这样只处理前 `k` 个元素，工作量由完整合并的 `N` 降低到 `k`。

### 矩阵题中的额外优化

对于行和列都按非递减顺序排列的 `n x n` 矩阵：

- 可以把每一行视为一条有序序列。
- 查找第 `k` 小时，只需要初始化前 `min(k, n)` 行。
- 原因是第一列也有序，第 `k` 行之后的首元素不可能成为严格更早的候选。

该优化依赖列有序。如果只有每行有序，就必须初始化所有行。

复杂度：

- Time: `O(k log(min(k, n)))`
- Space: `O(min(k, n))`

### 关键辨析

- 序列是否等长不是多路合并的核心要求。
- 核心要求是每条序列内部有序。
- 完整合并和第 `k` 小使用相同推进方式，主要区别是停止条件。

## 2026年6月5日: 双堆维护数据流中位数

### 适用场景

当数据不断到来，并且需要随时查询当前中位数时，可以使用两个堆。

典型问题：

- 数据流中的中位数；
- 动态加入数字后查询中间值；
- 需要把数据动态分成较小一半和较大一半。

如果每次查询都重新排序，代价会很高。双堆可以让插入为 `O(log n)`，查询中位数为 `O(1)`。

### 核心不变量

维护两个堆：

```python
small = []  # 较小的一半，用负数模拟最大堆
large = []  # 较大的一半，正常最小堆
```

需要始终保证：

- `small` 中所有真实值都小于等于 `large` 中所有值。
- `len(small) == len(large)` 或 `len(small) == len(large) + 1`。

堆顶含义：

- `-small[0]` 是较小一半中的最大值。
- `large[0]` 是较大一半中的最小值。

### 插入逻辑

新数字先根据左半边最大值判断放入哪个堆：

```python
if not small or num <= -small[0]:
    heapq.heappush(small, -num)
else:
    heapq.heappush(large, num)
```

这里的重点是：

```python
num <= -small[0]
```

含义是：新数字是否小于等于较小一半中的最大值。

`small[0]` 本身是负数，`-small[0]` 才是还原后的真实数字。

### 平衡逻辑

插入后需要恢复大小不变量：

```python
if len(small) > len(large) + 1:
    heapq.heappush(large, -heapq.heappop(small))
elif len(large) > len(small):
    heapq.heappush(small, -heapq.heappop(large))
```

移动元素时要注意符号转换：

- 从 `small` 弹出时，先取负号还原真实值，再放入 `large`。
- 从 `large` 弹出时，放入 `small` 前要取负号。

### 查询中位数

如果 `small` 多一个元素：

```python
return float(-small[0])
```

如果两个堆一样大：

```python
return (-small[0] + large[0]) / 2.0
```

如果实现允许 `large` 多一个，也可以额外处理：

```python
return float(large[0])
```

### 复杂度

- 插入：`O(log n)`
- 查询中位数：`O(1)`
- 空间：`O(n)`

### 关键辨析

- 两个堆大小只差 0 或 1，是代码主动平衡出来的，不是堆自动保证的。
- `small` 是用负数模拟最大堆；任何时候看真实值都要记得取负号。
- 双堆模式的核心不是“把数据装进两个容器”，而是每次操作后恢复顺序和大小两个不变量。

## Heap: 数对空间的 K-Way Merge

### 适用场景

当题目要求从两个有序数组形成的所有组合中，找和最小的前 `k` 个数对时，可以把组合空间拆成多条有序序列，而不是生成所有组合。

典型问题：

- K Pairs with Smallest Sums；
- 两个有序数组的前 `k` 个最小组合；
- 能按某个维度固定后形成有序序列的二维候选空间。

### 核心视角

固定 `nums1[i]`，让它依次搭配 `nums2[j]`：

```text
nums1[i] + nums2[0]
nums1[i] + nums2[1]
nums1[i] + nums2[2]
...
```

因为 `nums2` 非递减，所以这一行也是非递减序列。

### 堆中保存的状态

```python
(nums1[i] + nums2[j], i, j)
```

含义：

- 第一个值是排序依据；
- `i` 和 `j` 用来还原数对 `[nums1[i], nums2[j]]`；
- `j` 用来决定同一行下一步是否推进到 `j + 1`。

### 推进逻辑

初始化：

```python
for i in range(min(k, len(nums1))):
    heappush(heap, (nums1[i] + nums2[0], i, 0))
```

循环：

```python
while heap and len(result) < k:
    _, i, j = heappop(heap)
    result.append([nums1[i], nums2[j]])

    if j + 1 < len(nums2):
        heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
```

### 关键辨析

- 这不是双指针配对，也不是两个数组按下标一一配对。
- 每次只推进被弹出元素所在的那一行。
- 堆里始终保存的是“每一行当前暴露出来的最小候选”。
- 如果只需要前 `k` 个结果，达到 `k` 后立即停止。

### 复杂度

- 时间：`O(k log(min(k, len(nums1))))`
- 堆空间：`O(min(k, len(nums1)))`
- 返回结果：`O(k)`

## Union Find: 连通分量与集合合并

### 适用场景

当题目关心“两个元素是否属于同一组”或“合并两个集合后还有多少组”时，可以优先考虑并查集。

典型问题：

- 无向图连通分量数量；
- 判断两个节点是否连通；
- 冗余连接；
- 朋友圈 / 省份数量；
- 等式方程可满足性。

### 核心状态

```python
parent = list(range(n))
count = n
```

含义：

- `parent[x]` 表示节点 `x` 当前指向的父节点。
- 如果 `parent[x] == x`，说明 `x` 是一个集合的根节点。
- `count` 表示当前连通分量数量。

### find

`find(x)` 的目标是找到 `x` 所属集合的根节点。

路径压缩的关键是：查找根节点时，顺手缩短路径，让后续查找更快。

```python
while x != parent[x]:
    parent[x] = parent[parent[x]]
    x = parent[x]
return x
```

### union

`union(a, b)` 的目标是合并两个节点所在的集合。

关键判断：

```python
root_a = find(a)
root_b = find(b)
```

- 如果 `root_a == root_b`，说明已经在同一个集合，不需要合并。
- 如果 `root_a != root_b`，说明连接了两个不同集合，可以合并，连通分量数量减少 1。

### 关键辨析

- 自环不会改变连通分量数量。
- 重复边不会改变连通分量数量。
- `count -= 1` 必须只发生在两个根节点不同的时候。
- 并查集解决的是“动态合并集合”，不是遍历图上的所有路径。

### 复杂度

带路径压缩时，单次 `find` / `union` 的均摊复杂度接近 O(1)。

整体：

- 时间：近似 `O(n + e)`
- 空间：`O(n)`

## Union Find: 无向图判环与树判定

### 适用场景

当题目给出无向图边列表，并要求判断是否成环、是否是一棵树、或者找出造成环的边时，可以优先考虑并查集。

典型问题：

- Graph Valid Tree；
- Redundant Connection；
- 无向图动态加边判环；
- 判断新增边是否连接了两个已经连通的节点。

### 核心判断

对于一条边 `[a, b]`：

```python
root_a = find(a)
root_b = find(b)
```

- 如果 `root_a != root_b`，说明 `a` 和 `b` 原本不连通，这条边可以合并两个集合。
- 如果 `root_a == root_b`，说明 `a` 和 `b` 已经连通，再加这条边会形成环。

### 判断无向图是否为树

一棵包含 `n` 个节点的无向树必须满足：

```text
边数 == n - 1
没有环
```

常用结构：

```python
if len(edges) != n - 1:
    return False

parent = list(range(n))

for a, b in edges:
    if not union(a, b):
        return False

return True
```

这里边数正确加上没有环，已经足够推出图连通。

### 找冗余连接

如果题目要求返回造成环的那条边，可以按输入顺序处理：

```python
for a, b in edges:
    if not union(a, b):
        return [a, b]
```

`union` 返回 `False` 的含义是：这两个节点已经属于同一个集合，当前边是多余边。

### 关键辨析

- 环不是重复边。
- 重复边是完全相同的边再次出现。
- 环是两个已经连通的节点之间又出现一条边。
- 判断连通性要比较根节点：`find(a) == find(b)`。
- 对于节点编号从 `1` 开始的题，`parent` 通常写成 `list(range(n + 1))`。

### 复杂度

带路径压缩时：

- 单次 `find` / `union` 均摊近似 O(1)
- 总时间：`O(e * α(n))`
- 空间：`O(n)`

## 2026年6月10日: Topological Sort / Kahn Algorithm

### 适用场景

当题目给出一组有向依赖关系，并要求判断是否能完成、返回一种合法顺序、或者检测有向图中是否存在环时，可以考虑拓扑排序。

典型问题：

- Course Schedule；
- Course Schedule II；
- Alien Dictionary；
- 任务调度；
- 有向依赖关系排序。

### 核心思想

拓扑排序要解决的是：对于每条有向边 `a -> b`，结果中 `a` 必须出现在 `b` 前面。

Kahn 算法的核心是入度：

- 入度表示一个节点还有多少个未处理的前置依赖。
- 入度为 `0` 的节点当前可以被处理。
- 处理完一个节点后，它指向的后继节点少了一个前置依赖，所以后继节点入度减 1。
- 如果某个后继节点入度变成 `0`，它也可以进入队列。

### 代码骨架

```python
from collections import deque


graph = [[] for _ in range(num_nodes)]
indegree = [0] * num_nodes

for node, prereq in dependencies:
    graph[prereq].append(node)
    indegree[node] += 1

queue = deque([i for i in range(num_nodes) if indegree[i] == 0])
order = []

while queue:
    current = queue.popleft()
    order.append(current)

    for neighbor in graph[current]:
        indegree[neighbor] -= 1
        if indegree[neighbor] == 0:
            queue.append(neighbor)

if len(order) == num_nodes:
    return order
return []
```

### 判断能否完成

如果题目只要求返回 `True / False`，不需要保存完整顺序，只需要统计处理过的节点数量：

```python
processed = 0

while queue:
    current = queue.popleft()
    processed += 1
    ...

return processed == num_nodes
```

### 返回合法顺序

如果题目要求返回具体顺序，就保存 `order`：

```python
order.append(current)
```

最后：

```python
return order if len(order) == num_nodes else []
```

### 关键辨析

- 有向依赖题最重要的是先确定边方向。
- 课程表里 `[course, prereq]` 表示 `prereq -> course`。
- 拓扑排序结果可能不唯一。
- 测试返回顺序时，应验证依赖关系是否满足，而不是只比较某一个固定数组。
- 如果最后没有处理完全部节点，说明剩余节点在环里互相等待。

### 复杂度

- 时间：`O(V + E)`，其中 `V` 是节点数，`E` 是边数。
- 空间：`O(V + E)`，主要来自邻接表、入度数组和队列。

## 2026年6月11日: Alien Dictionary / 字符依赖建图

### 适用场景

当题目给出一组已经按某种未知字典序排好的字符串，并要求推断字符之间的顺序时，可以把字符看成节点，把“某字符必须排在另一个字符前面”看成有向边。

典型问题：

- Alien Dictionary；
- 从排序字符串中恢复字符顺序；
- 从局部有序样本中推导全局依赖关系。

### 核心思想

字典序比较只由第一处不同字符决定。

例如：

```text
"wrt"
"wrf"
```

前两个字符都相同，第一处不同是：

```text
t != f
```

因此可以推出：

```text
t -> f
```

意思是 `t` 必须排在 `f` 前面。后面的字符不能再提供新的顺序信息。

### 代码骨架

```python
from collections import deque


chars = set("".join(words))
graph = {char: set() for char in chars}
indegree = {char: 0 for char in chars}

for first_word, second_word in zip(words, words[1:]):
    min_len = min(len(first_word), len(second_word))

    if (
        len(first_word) > len(second_word)
        and first_word[:min_len] == second_word[:min_len]
    ):
        return ""

    for i in range(min_len):
        if first_word[i] != second_word[i]:
            first_char = first_word[i]
            second_char = second_word[i]

            if second_char not in graph[first_char]:
                graph[first_char].add(second_char)
                indegree[second_char] += 1

            break

queue = deque([char for char in chars if indegree[char] == 0])
order = []

while queue:
    char = queue.popleft()
    order.append(char)

    for neighbor in graph[char]:
        indegree[neighbor] -= 1
        if indegree[neighbor] == 0:
            queue.append(neighbor)

return "".join(order) if len(order) == len(chars) else ""
```

### 前缀非法

如果前面的单词更长，并且后面的单词是它的前缀，则输入非法：

```text
["abc", "ab"]
```

原因是如果前缀完全相同，短单词应该排在长单词前面。

这类情况需要在建边阶段单独判断，不能只依赖最后的环检测。

### 重复边去重

邻接表建议用 `set`：

```python
graph = {char: set() for char in chars}
```

只有当边第一次出现时才增加入度：

```python
if second_char not in graph[first_char]:
    graph[first_char].add(second_char)
    indegree[second_char] += 1
```

否则同一条依赖被重复统计，会导致入度错误，拓扑排序可能误判。

### 关键辨析

- 比较相邻单词即可，不需要比较所有单词对。
- 每对相邻单词只根据第一处不同字符建一条边。
- 所有出现过的字符都必须进入节点集合，即使它没有任何边。
- 拓扑排序答案可能不唯一。
- 如果题目要求字典序最小的合法答案，可以用最小堆替代普通队列。

### 复杂度

设 `C` 是所有单词字符总数，`V` 是不同字符数量，`E` 是依赖边数量：

- 时间：`O(C + V + E)`
- 空间：`O(V + E)`
