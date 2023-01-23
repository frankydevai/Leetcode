def sortedSquares(self, nums: list[int]) -> list[int]:
    p_l = [i ** 2 for i in nums]

    return sorted(p_l)