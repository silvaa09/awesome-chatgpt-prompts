"""Bit operation visualization helpers."""

from .bit_engine import check_bit, flip_bit, reverse_bits


def visualize_bit_operation(num: int, operation: str, n: int | None = None) -> str:
    """Visualize flip/reverse/check operations in a human-readable format."""
    if operation not in {"flip", "reverse", "check"}:
        raise ValueError("operation must be one of: flip, reverse, check")
    if not isinstance(num, int) or num < 0:
        raise ValueError("num must be a non-negative integer")

    width = max(4, num.bit_length(), (n + 1 if isinstance(n, int) and n >= 0 else 0))
    original = format(num, f"0{width}b")

    if operation == "flip":
        if n is None or not isinstance(n, int) or n < 0:
            raise ValueError("n must be a non-negative integer for flip")
        mask = format(1 << n, f"0{width}b")
        result_num = flip_bit(num, n)
        result = format(result_num, f"0{width}b")
        return f"Original:  {original}\nMask:      {mask}\nResult:    {result}"

    if operation == "reverse":
        result_num = reverse_bits(num, bits=width)
        result = format(result_num, f"0{width}b")
        return f"Original:  {original}\nMask:      {'-' * width}\nResult:    {result}"

    if n is None or not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer for check")
    mask = format(1 << n, f"0{width}b")
    result_bit = check_bit(num, n)
    return f"Original:  {original}\nMask:      {mask}\nResult:    {result_bit}"
