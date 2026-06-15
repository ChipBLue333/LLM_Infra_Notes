"""
Problem 076: Vector Basics

Difficulty:
Easy / Medium

Topic:
Python Class / Vector / Linear Algebra / LLM Inference Basics

Description:
实现一个简单的 Vector 类，用 Python 列表保存一维向量中的数值。

这道题是大模型推理框架基础训练的第一步。后续实现 Matrix、Tensor、
MatMul 和 Attention 时，都需要先理解数据封装、形状检查和数值运算。

本题不允许使用 NumPy。所有运算都需要使用 Python 基础语法完成。

Input:
values: List[float] - 向量中的元素

Output:
根据调用的方法返回：
- 向量长度
- 向量元素的列表副本
- 新的 Vector
- 两个向量的点积
- 向量的 L2 范数

Examples:
Example 1:
Input:
v1 = Vector([1.0, 2.0, 3.0])
v2 = Vector([4.0, 5.0, 6.0])

Output:
v1.add(v2).to_list() == [5.0, 7.0, 9.0]
v1.dot(v2) == 32.0

Example 2:
Input:
v = Vector([3.0, 4.0])

Output:
v.scalar_multiply(2.0).to_list() == [6.0, 8.0]
v.l2_norm() == 5.0

Constraints:
- 0 <= len(values) <= 10^4
- values 中的元素均为 int 或 float
- 不允许使用 NumPy

Task:
实现 Vector 类中的所有 TODO。

要求：
1. 构造函数必须保存传入数据的副本，不能直接持有调用者的原列表。
2. len(vector) 返回向量的元素数量。
3. to_list() 返回内部数据的副本，调用者修改返回值时不能影响 Vector。
4. add(other) 返回一个新 Vector，不能修改原来的两个向量。
5. dot(other) 返回两个向量的点积。
6. scalar_multiply(scalar) 返回一个新 Vector，不能修改原向量。
7. l2_norm() 返回向量的 L2 范数。
8. add 和 dot 遇到长度不同的向量时，必须抛出 ValueError。
9. 空向量是合法输入：长度、点积和 L2 范数都应得到合理结果。

思考：
- 为什么构造函数和 to_list() 都需要复制列表？
- 哪些方法应该返回新对象，哪些方法应该返回单个数值？
- 维度检查应该发生在运算前还是运算过程中？
- L2 范数的数学定义是什么？
"""

from __future__ import annotations

from typing import Callable, List


class Vector:
    def __init__(self, values: List[float]) -> None:
        # TODO: 保存 values 的副本
        pass

    def __len__(self) -> int:
        # TODO: 返回向量长度
        pass

    def to_list(self) -> List[float]:
        # TODO: 返回内部数据的副本
        pass

    def add(self, other: Vector) -> Vector:
        # TODO: 检查维度并返回相加后的新 Vector
        pass

    def dot(self, other: Vector) -> float:
        # TODO: 检查维度并返回点积
        pass

    def scalar_multiply(self, scalar: float) -> Vector:
        # TODO: 返回数乘后的新 Vector
        pass

    def l2_norm(self) -> float:
        # TODO: 返回 L2 范数
        pass


def assert_close(actual: float, expected: float) -> None:
    tolerance = 1e-9
    assert abs(actual - expected) <= tolerance, (
        f"expected {expected}, got {actual}"
    )


def assert_raises_value_error(operation: Callable[[], object]) -> None:
    try:
        operation()
    except ValueError:
        return
    raise AssertionError("expected ValueError")


def run_tests() -> None:
    vector = Vector([1.0, 2.0, 3.0])
    assert len(vector) == 3
    assert vector.to_list() == [1.0, 2.0, 3.0]

    original_values = [2.0, 4.0]
    copied_vector = Vector(original_values)
    original_values[0] = 100.0
    assert copied_vector.to_list() == [2.0, 4.0]

    exposed_values = copied_vector.to_list()
    exposed_values[1] = 200.0
    assert copied_vector.to_list() == [2.0, 4.0]

    left = Vector([1.0, 2.0, 3.0])
    right = Vector([4.0, 5.0, 6.0])
    result = left.add(right)
    assert result.to_list() == [5.0, 7.0, 9.0]
    assert left.to_list() == [1.0, 2.0, 3.0]
    assert right.to_list() == [4.0, 5.0, 6.0]

    assert_close(left.dot(right), 32.0)

    scaled = Vector([1.5, -2.0, 0.0]).scalar_multiply(2.0)
    assert scaled.to_list() == [3.0, -4.0, 0.0]

    assert_close(Vector([3.0, 4.0]).l2_norm(), 5.0)
    assert_close(Vector([]).l2_norm(), 0.0)
    assert len(Vector([])) == 0
    assert_close(Vector([]).dot(Vector([])), 0.0)

    assert_raises_value_error(
        lambda: Vector([1.0, 2.0]).add(Vector([3.0]))
    )
    assert_raises_value_error(
        lambda: Vector([1.0]).dot(Vector([2.0, 3.0]))
    )

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
