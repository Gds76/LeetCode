class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        maxx = nums[0] + nums[n-1]
        for i in range(1, n//2+1):
            maxx = max(maxx, nums[i] + nums[n-i-1])
        return maxx
        