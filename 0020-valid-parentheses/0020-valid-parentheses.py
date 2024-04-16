class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {
            "(": ")",
            "[": "]",
            "{": "}"

        }
        
        lst = []
        for i in range(len(s)):
            if s[i] in parentheses.keys():
                lst.append(s[i])
            if s[i] in parentheses.values():
                if len(lst) == 0:
                    return False
                left = lst.pop()
                if parentheses[left] != s[i]:
                    return False
        return len(lst) == 0
                    
