import random

import pytest

from src.custom_stack_class import CustomStack
from src.number_asc_order import NumberAscOrder


def test_sort_six_random_numbers_from_full_stack(mocker):
    # Stub do sorteio: controla os 6 números "aleatórios" da Mega Sena.
    mocker.patch("random.randint", side_effect=[60, 6, 33, 1, 45, 22])

    cut = CustomStack(6)
    for _ in range(6):
        cut.push(random.randint(1, 60))

    result = NumberAscOrder().sort(cut)

    assert isinstance(result, list)
    assert result == [1, 6, 22, 33, 45, 60]
    assert cut.is_empty() is True


def test_sort_empty_stack_of_six_positions():
    cut = CustomStack(6)

    result = NumberAscOrder().sort(cut)

    assert result == []
    assert cut.is_empty() is True


def test_sort_observes_stack_interactions_with_mock(mocker):
    stack = mocker.MagicMock(spec=CustomStack)
    stack.is_empty.side_effect = [False, False, False, True]
    stack.pop.side_effect = [30, 10, 20]

    result = NumberAscOrder().sort(stack)

    assert result == [10, 20, 30]
    assert stack.is_empty.call_count == 4
    assert stack.pop.call_count == 3
    stack.pop.assert_has_calls([mocker.call(), mocker.call(), mocker.call()])


def test_sort_orders_ascending_keeping_duplicates():
    cut = CustomStack(6)
    for number in [6, 1, 6, 3, 2, 1]:
        cut.push(number)

    assert NumberAscOrder().sort(cut) == [1, 1, 2, 3, 6, 6]


def test_sort_none_stack_raises_value_error():
    with pytest.raises(ValueError):
        NumberAscOrder().sort(None)


def test_sort_non_stack_raises_type_error():
    with pytest.raises(TypeError):
        NumberAscOrder().sort([6, 5, 4, 3, 2, 1])
