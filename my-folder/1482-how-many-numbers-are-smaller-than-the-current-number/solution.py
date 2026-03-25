class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sol = [0] * len(nums)
        hashMap = {}
        sortedNums = sorted(nums)
        count = 0
        for i, n in enumerate(sortedNums):
            hashMap[n] = i
            while (i != 0 and sortedNums[i - 1] == sortedNums[i]):
                hashMap[n] -= 1
                i -= 1
        for i, n in enumerate(nums):
            sol[i] = hashMap[n]
        return sol
