def reverseString(self, s: list[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    s[:] = [s[-i] for i in range(1, len(s) + 1)]