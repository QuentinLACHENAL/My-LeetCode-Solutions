class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ref = set(range(1, n + 1))
        noDuplicate = set(nums)
        missing = list(ref - noDuplicate)[0]
        dup = sum(nums) - sum(noDuplicate)
        return [dup, missing]
