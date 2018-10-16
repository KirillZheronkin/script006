import pytest
from script006.labs.examples.lab2 import task1
fixtures = (
    (['1', '2', '1', '1', '2', '3'], ['1', '2', '3']),
    (['A', 'B', 'A', 'B', 'B', 'A'], ['A', 'B'])
)


@pytest.mark.parametrize('input, expected', fixtures)
def test_task1(input, expected):
    assert task1(input) == expected


@pytest.mark.parametrize('input, expected', fixtures)
def test_task_bit_more_complex(input, expected):
    task1(input)
    assert input is expected
