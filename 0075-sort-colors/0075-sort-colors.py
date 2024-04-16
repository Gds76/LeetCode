class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        j = 0
        k= 0
        for num in nums:
            if num == 0:
                l += 1
            elif num == 1:
                j += 1
            else:
                k += 1
        for i in range(len(nums)):
            if i < l:
                nums[i] = 0
            elif i < l + j:
                nums[i] = 1
            else:
                nums[i] = 2
        
        