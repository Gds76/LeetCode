class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1
        while l <= r:
            j = (r+l)//2
            if target == nums[j]:
                return j
            if target < nums[j]:
                r = j-1
            else:
                l = j+1
        return -1
        