import random

import pytest

from src.custom_stack_class import CustomStack
from src.number_asc_order_class import NumberAscOrder


class TestNumberAscOrder:

    def test_sort_six_drawn_numbers_returns_ascending_order(self, mocker):
        drawn_numbers = [23, 60, 4, 17, 50, 8]
        mocker.patch("random.sample", return_value=drawn_numbers)

        stack = CustomStack(6)
        for number in random.sample(range(1, 61), 6):
            stack.push(number)

        result = NumberAscOrder().sort(stack)

        assert result == sorted(drawn_numbers)
        assert result == [4, 8, 17, 23, 50, 60]

    def test_sort_empty_stack_returns_empty_list(self):
        stack = CustomStack(6)

        result = NumberAscOrder().sort(stack)

        assert result == []
        assert stack.is_empty() is True

    def test_sort_uses_custom_stack_public_interface(self, mocker):
        mock_stack = mocker.MagicMock(spec=CustomStack)
        mock_stack.is_empty.side_effect = [False, False, False, True]
        mock_stack.pop.side_effect = [30, 10, 20]

        result = NumberAscOrder().sort(mock_stack)

        assert result == [10, 20, 30]
        assert mock_stack.pop.call_count == 3

    def test_sort_raises_type_error_for_invalid_input(self):
        with pytest.raises(TypeError):
            NumberAscOrder().sort(None)
