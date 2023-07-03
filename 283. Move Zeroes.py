class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 1
        while i < len(nums) and j < len(nums):
            if nums[i] == 0:
                if j > i and nums[j] != 0:
                    nums[i] , nums[j] = nums[j], nums[i]
                else:
                    j += 1
                    continue
            i += 1
        
