class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        cum_sum = [0]*(n+1)
        
        
        for j in range(1, len(nums)+1):
            cum_sum[j] = cum_sum[j-1] + nums[j-1]
            
       
        for i in range(1, len(cum_sum)):
            if cum_sum[i-1] == cum_sum[len(cum_sum)-1] - cum_sum[i]:
            
                return i-1
        print(cum_sum)
        return -1
        