class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
       
        n = len(nums)
    
    
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        
        for i in range(k, n):
            current_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, current_sum)
        
        
        max_average = max_sum / k
        
        return max_average


        
