class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        i = 0
        j = n-1
        while i <= j:
            k = (i+j)//2
            if citations[k] == n-k:
                
                return n-k
            elif citations[k] < n-k:
                i+=1
            else:
                j-=1
        return n-i
        