class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        def shift(a, k):
        
            a = char[(k + char.index(a))%26]
            return a
       
                       
        
        s = list(s)
        
        n = len(s) + 1
        prefix_sum = [0] * n
        
        
        for i in range(len(shifts)):
            if shifts[i][2] == 1:
                prefix_sum[shifts[i][0]] += 1
                if shifts[i][1] + 1 < len(prefix_sum):
                    prefix_sum[shifts[i][1] + 1] -= 1
            if shifts[i][2] == 0:
                prefix_sum[shifts[i][0]] -= 1
                if shifts[i][1] + 1 < len(prefix_sum):
                    prefix_sum[shifts[i][1] + 1] += 1
        
        for i in range(1, len(prefix_sum)):
            prefix_sum[i] += prefix_sum[i-1]
        
        for i in range(len(s)):
            
            
            s[i] = shift(s[i], prefix_sum[i])
        print(prefix_sum)
        return "".join(s)

        