class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i = 0
        j = 1
        while i < j and j < len(nums):
            if nums[i] == nums[j]:
                nums[i], nums[j] = nums[i]*2, 0                        
            i +=1
            j+=1

        k = 0
        l = 1
        while k < l and l < len(nums):
            if nums[k] == 0 and nums[l] !=0:
                nums[k], nums[l] = nums[l], nums[k]
                k+=1
                l+=1
            elif nums[l] ==0 and nums[k]==0:
        
                l+=1
            else:
                k+=1
                l+=1
          
        return nums