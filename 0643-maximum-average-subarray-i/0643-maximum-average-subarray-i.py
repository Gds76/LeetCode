class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current = sum(nums[:k])
        maxx = current
        n = len(nums)
        for i in range(k, n):
            current += nums[i] - nums[i - k]
            maxx = max(maxx, current)
        

       
    
    
        
        return maxx/k


        
