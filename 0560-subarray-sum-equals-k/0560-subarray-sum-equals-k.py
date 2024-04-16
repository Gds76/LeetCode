class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res  = 0
        current_sum = 0
        dic = {0:1}
        for i in range(len(nums)):
            current_sum += nums[i]
            var = current_sum - k
            if var in dic:
                res += dic.get(var)
            dic[current_sum] = dic.get(current_sum, 0) + 1
            
        return res
        
            
            


        