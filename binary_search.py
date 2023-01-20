def search(self, nums: list[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    t = target
    while low < high:
        mid = (low + high) // 2
        guess = nums[mid]
        if t not in nums:
            return -1
        if guess == t:
            return mid
        if guess > t:
            high = mid - 1
        else:
            low = mid + 1
    if nums[high] == t:
        return high
    else:
        return -1