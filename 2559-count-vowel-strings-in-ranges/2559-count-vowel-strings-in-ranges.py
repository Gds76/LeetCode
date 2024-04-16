class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        vowels = ["a", "e", "i", "o", "u"]
        pre = [0]*n
        for i in range(n):
            if words[i][0] in vowels and words[i][-1] in vowels:
                pre[i] += 1
        prefix_sum = [0]*(n+1)
        
        for i in range(1, n+1):
            prefix_sum[i] += prefix_sum[i-1] + pre[i-1]
        prefix_sum.remove(prefix_sum[0])
        lst = []
        for i in range(len(queries)):
            if queries[i][0] == 0:
                lst.append(prefix_sum[queries[i][1]])
            else:
                lst.append(prefix_sum[queries[i][1]] - prefix_sum[queries[i][0] - 1])
        # print(prefix_sum)
        return lst
            
            

        