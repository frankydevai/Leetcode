def moveZeroes(self, nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    new_l = [i for i in nums if i == 0]
    n = [i for i in nums if i != 0]
    nums[:] = n + new_l
