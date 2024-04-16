class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        if len(s) == 0:
            return None
        
        for _ in range(len(s)):
            if "" in s:
                s.remove("")
        s.reverse()
        
        return " ".join(s)
        

        