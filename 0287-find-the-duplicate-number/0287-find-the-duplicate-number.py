class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        s = sum(nums)
        a = sum(set(nums))
        return int((s-a)/(len(nums)-len(set(nums))))
        # i = 0
        
        # while i < len(nums):
        #     if nums.index(nums[i]) != i:
        #         return nums[i]
        #     i+=1
                
        
        # while i < len(nums):
        #     for j in range(len(nums)):
        #         if i!=j and nums[i] - nums[j] == 0:
        #             return nums[i]
                
        #     i+=1
            
        