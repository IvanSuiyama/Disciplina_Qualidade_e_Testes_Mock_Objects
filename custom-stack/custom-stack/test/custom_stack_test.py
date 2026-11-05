import pytest

from src.custom_stack_class import (
    CustomStack,
    StackEmptyException,
    StackFullException,
)


def test_new_stack_starts_empty_and_respects_limit():
    cut = CustomStack(5)

    assert cut.limit == 5
    assert cut.elements == []
    assert cut.size() == 0
    assert cut.is_empty() is True


def test_push_one_element_into_stack():
    element_value = 5.0

    cut = CustomStack(5)
    cut.push(element_value)

    assert cut.is_empty() is False
    assert cut.size() == 1
    assert cut.top() == element_value


def test_push_elements_up_to_limit():
    cut = CustomStack(3)

    cut.push(1)
    cut.push(2)
    cut.push(3)

    assert cut.size() == 3
    assert cut.top() == 3


def test_push_over_limit_raises_stack_full_exception():
    cut = CustomStack(2)
    cut.push(1)
    cut.push(2)

    with pytest.raises(StackFullException):
        cut.push(3)

    assert cut.size() == 2
    assert cut.top() == 2


def test_push_into_zero_limit_stack_raises_stack_full_exception():
    cut = CustomStack(0)

    with pytest.raises(StackFullException):
        cut.push(1)

    assert cut.is_empty() is True


def test_pop_removes_and_returns_last_element_lifo():
    cut = CustomStack(3)
    cut.push(10)
    cut.push(20)
    cut.push(30)

    assert cut.pop() == 30
    assert cut.pop() == 20
    assert cut.size() == 1
    assert cut.top() == 10


def test_pop_empty_stack_raises_stack_empty_exception():
    cut = CustomStack(3)

    with pytest.raises(StackEmptyException):
        cut.pop()


def test_top_does_not_remove_element():
    cut = CustomStack(3)
    cut.push(7)
    cut.push(8)

    assert cut.top() == 8
    assert cut.size() == 2
    assert cut.pop() == 8


def test_top_empty_stack_raises_stack_empty_exception():
    cut = CustomStack(3)

    with pytest.raises(StackEmptyException):
        cut.top()
