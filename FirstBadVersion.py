def firstBadVersion(self, n: int) -> int:
    low = 1
    high = n
    r = 0
    while low < high:
        mid = (low + high) // 2
        guess = mid
        if isBadVersion(guess):
            r = guess

            high = mid - 1
        else:
            low = mid + 1

    if isBadVersion(low):
        return low
    else:
        r
