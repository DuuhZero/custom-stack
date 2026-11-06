import pytest

from src.custom_stack_class import *


def test_push_one_element_in_stack():
    element_value = 5.0

    cut = CustomStack(5)
    cut.push(element_value)

    assert cut.is_empty() == False
    assert element_value == cut.top()
    assert 1 == cut.size()


def test_new_stack_is_empty():
    cut = CustomStack(5)

    assert cut.is_empty() is True
    assert cut.size() == 0


def test_push_multiple_elements_increases_size():
    cut = CustomStack(5)

    cut.push(1)
    cut.push(2)
    cut.push(3)

    assert cut.size() == 3
    assert cut.is_empty() is False


def test_push_raises_stack_full_exception_when_limit_reached():
    cut = CustomStack(2)
    cut.push(10)
    cut.push(20)

    with pytest.raises(StackFullException):
        cut.push(30)

    assert cut.size() == 2


def test_push_raises_stack_full_exception_on_single_position_stack():
    cut = CustomStack(1)
    cut.push(10)

    with pytest.raises(StackFullException):
        cut.push(20)


def test_pop_returns_last_pushed_element():
    cut = CustomStack(5)
    cut.push(1)
    cut.push(2)
    cut.push(3)

    assert cut.pop() == 3
    assert cut.size() == 2


def test_pop_follows_lifo_order():
    cut = CustomStack(3)
    cut.push(1)
    cut.push(2)
    cut.push(3)

    assert cut.pop() == 3
    assert cut.pop() == 2
    assert cut.pop() == 1
    assert cut.is_empty() is True


def test_pop_raises_stack_empty_exception_when_empty():
    cut = CustomStack(5)

    with pytest.raises(StackEmptyException):
        cut.pop()


def test_top_returns_last_element_without_removing_it():
    cut = CustomStack(5)
    cut.push(1)
    cut.push(2)

    assert cut.top() == 2
    assert cut.size() == 2


def test_top_raises_stack_empty_exception_when_empty():
    cut = CustomStack(5)

    with pytest.raises(StackEmptyException):
        cut.top()
