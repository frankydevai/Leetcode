def decompressRLElist(self, nums: list[int]) -> list[int]:
    n = []

    for i in range(0, len(nums) - 1, 2):
        n = n + nums[i] * [nums[i + 1]]
    return n