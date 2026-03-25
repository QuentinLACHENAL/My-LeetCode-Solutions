class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        sol = []
        numsSet = set(nums)
        for i in range(1, len(nums) + 1):
            if not i in numsSet:
                sol.append(i)
        return sol
