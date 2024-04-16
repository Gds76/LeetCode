class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1 = list(word1)
        word2 = list(word2)
        print(word2)
        n = min(len(word1), len(word2))
        word3 = []
        for i in range(n): 
            word3.append(word1[i])
            word3.append(word2[i])
        if n == len(word1):
            for i in range(n, len(word2)):
                word3.append(word2[i])
        elif n == len(word2):
            for i in range(n, len(word1)):
                word3.append(word1[i])
        return "".join(word3)

        # for i in range(len(word3)):
            
        
        return word


        