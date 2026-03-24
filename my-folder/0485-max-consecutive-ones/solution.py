class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum = 0
        tmp = 0
        for n in nums:
            if n == 1:
                tmp += 1
            else:
                if tmp > maximum:
                    maximum = tmp
                tmp = 0
        if tmp > maximum:
            return tmp
        return maximum

