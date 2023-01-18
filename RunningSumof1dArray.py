def runningSum(self, nums: list[int]) -> list[int]:
    ans = []
    l = []
    for i in nums:
        ans.append(i)
        l.append(sum(ans))
    return l