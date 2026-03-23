import pytest

from bitlab_qa_trainer.bit_engine import check_bit, flip_bit, reverse_bits, reverse_number


def test_flip_bit_expected_output():
    assert flip_bit(10, 1) == 8


def test_reverse_bits_expected_output():
    assert reverse_bits(13, 8) == 176


def test_check_bit_expected_output():
    assert check_bit(10, 1) == 1


def test_reverse_number_expected_output():
    assert reverse_number(1234) == 4321


def test_reverse_number_zero():
    assert reverse_number(0) == 0


@pytest.mark.parametrize("func,args", [
    (flip_bit, (-1, 1)),
    (flip_bit, (10, -1)),
    (check_bit, (5, -2)),
    (reverse_bits, (-5, 8)),
    (reverse_number, (-1,)),
])
def test_invalid_inputs_raise(func, args):
    with pytest.raises((TypeError, ValueError)):
        func(*args)
