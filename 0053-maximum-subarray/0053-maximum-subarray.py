class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        prefix_sum = 0
        minn = 0
        res = -inf
        for i in range(len(nums)):
            prefix_sum += nums[i]
            
            
            
           
            curr_sum  = prefix_sum
           
            
            res = max(res, curr_sum - minn)
            minn = min(minn, curr_sum)
        print(prefix_sum)
        return res 

        

        
        