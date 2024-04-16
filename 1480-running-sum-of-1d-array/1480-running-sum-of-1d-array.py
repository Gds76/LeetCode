class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        lst = [nums[0]]
        
        j = 1

        while j <len(nums):
            lst.append(lst[j-1] + nums[j])
            j+=1
        return lst
        