"""Core bit and number helpers for BitLab QA Trainer."""


def _validate_non_negative_int(value: int, name: str) -> None:
    if not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if value < 0:
        raise ValueError(f"{name} must be non-negative")


def flip_bit(num: int, n: int) -> int:
    """Flip bit *n* in *num* using XOR."""
    _validate_non_negative_int(num, "num")
    _validate_non_negative_int(n, "n")
    return num ^ (1 << n)


def reverse_bits(num: int, bits: int = 32) -> int:
    """Reverse the lower *bits* bits in *num*."""
    _validate_non_negative_int(num, "num")
    _validate_non_negative_int(bits, "bits")
    if bits == 0:
        return 0

    result = 0
    working = num
    for _ in range(bits):
        result = (result << 1) | (working & 1)
        working >>= 1
    return result


def check_bit(num: int, n: int) -> int:
    """Return 1 if bit *n* is set in *num*, else 0."""
    _validate_non_negative_int(num, "num")
    _validate_non_negative_int(n, "n")
    return (num >> n) & 1


def reverse_number(n: int) -> int:
    """Reverse decimal digits in a non-negative integer."""
    _validate_non_negative_int(n, "n")

    result = 0
    working = n
    while working > 0:
        result = result * 10 + working % 10
        working //= 10
    return result
