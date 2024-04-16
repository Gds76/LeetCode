class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        cum_sum = [self.nums[0]]
        j = 1
        while j < len(self.nums):
            cum_sum.append(cum_sum[j-1] + self.nums[j])
            j+=1
        return cum_sum[right] - cum_sum[left-1] if left > 0 else cum_sum[right]
        
        
[1, 2, 3, 4, 5, 6]
[1, 3, 6, 10,15, 21]


# Your NumArray object will be instantiated and called as such:

