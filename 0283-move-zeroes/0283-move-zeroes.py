class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        
        lst = []
        
        for j in range(n):
            if nums[j] == 0:
                lst.append(nums[j])
        for i in range(len(lst)):
            nums.remove(lst[i])
            nums.append(0)
        
        