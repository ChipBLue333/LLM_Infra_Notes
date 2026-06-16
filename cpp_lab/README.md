# C++ Algorithm Review Lab

这个目录用于用 C++ 复习已经学过的算法模式，同时补齐 C++ 基础和 STL 使用。

训练与 review 规则见 [CODING_COACH_SKILL.md](CODING_COACH_SKILL.md)。

## 当前阶段

暂缓进入大模型推理框架训练，先进行一轮 C++ 算法复习。

复习不会机械重做全部 Python 题目，而是为每种算法模式选择代表题：

1. Array / Hash Map
2. Stack / Queue
3. Two Pointers / Sliding Window / Binary Search
4. Linked List
5. Binary Tree
6. Backtracking
7. Graph / BFS / DFS
8. Dynamic Programming
9. Greedy / Intervals
10. Heap
11. Union Find
12. Topological Sort / Trie

## 训练重点

每道题除了算法，还需要关注：

- `std::vector`、`std::string`、`std::unordered_map`
- `const` 与引用
- 值传递和拷贝成本
- 迭代器和范围 `for`
- 类、结构体与资源生命周期
- 时间复杂度和空间复杂度
- 使用编译器警告检查代码

## 工作方式

1. Codex 创建只有题目、函数签名和测试的 `.cpp` 文件。
2. 你独立完成 `TODO`。
3. 编译并运行测试。
4. Codex review 正确性、复杂度和 C++ 写法。
5. 完成后将复盘追加到 `notes/review_log.md`。

除非你明确要求“请给我参考答案”，否则不会提供完整实现。
