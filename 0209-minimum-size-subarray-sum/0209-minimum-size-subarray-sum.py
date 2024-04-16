class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_length = float('inf')
        
        
        i = 0
        window_sum = 0
        
        
        for j in range(n):
            window_sum += nums[j]  
            
            while window_sum >= target:
                min_length = min(min_length, j - i + 1)
                window_sum -= nums[i] 
                i += 1
        if min_length != float('inf'):
            return min_length
        else:
            return 0
        

        