class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_prod = [1]*(n+1)
        for i in range(1, len(prefix_prod)):
            prefix_prod[i] = prefix_prod[i-1]*nums[i-1]
        prefix_prod.pop()
        suffix_prod = [1]*(n+1)
        nums.reverse()
        for i in range(1, len(suffix_prod)):
            suffix_prod[i] = suffix_prod[i-1]*nums[i-1]
        suffix_prod.pop()
        suffix_prod.reverse()
        
        prod = [prefix_prod[i]*suffix_prod[i] for i in range(len(prefix_prod))]
        return prod
        