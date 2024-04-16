class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.cum_sum = [self.nums[0]]
        
        j = 1
        while j < len(self.nums):
            self.cum_sum.append(self.cum_sum[j-1] + self.nums[j])
            j+=1

    def sumRange(self, left: int, right: int) -> int:
        
        return self.cum_sum[right] - self.cum_sum[left-1] if left > 0 else self.cum_sum[right]


        
        



# Your NumArray object will be instantiated and called as such:

