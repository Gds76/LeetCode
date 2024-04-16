class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        lst = [0, gain[0]]
        
        for i in range(1, len(gain)):
            lst.append(lst[i] + gain[i])
        return max(lst)
            
        