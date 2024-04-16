class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        lst = []
        i = 0
        j = 1
        while j <= len(nums):
            lst.append(sum(nums[i:j]))
            j+=1
        return lst
        