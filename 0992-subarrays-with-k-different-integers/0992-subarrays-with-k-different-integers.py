class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        res = 0
        freq = {}
        i = 0
        j = 0 
        for l in range(len(nums)):
            freq[nums[l]] = 1 + freq.get(nums[l], 0)



            while len(freq) > k:
                freq[nums[j]] -= 1
                if freq[nums[j]] == 0:
                    freq.pop(nums[j])
                j+=1
                i = j
                
            while freq[nums[j]] > 1:
                freq[nums[j]] -=1
                j+=1
            if len(freq) == k:
                res += j - i +1
            
            
        
        return res 
        