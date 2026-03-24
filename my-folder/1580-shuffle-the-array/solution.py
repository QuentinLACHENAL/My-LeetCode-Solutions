class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        array = [0] * (2 * n)
        array[::2] = nums[:n]
        array[1::2] = nums[n:]
        return array
