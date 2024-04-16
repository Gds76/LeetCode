class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        
        skill = sorted(skill)
        sum = skill[0] + skill[n-1]
        i = 1
        while i< n-1 and skill[i] + skill[n-i-1] == sum:
            i+=1
        total = 0
        if i == n-1:
            for i in range(n//2):
                total += skill[i] *skill[n-i-1]
            return total
        else:
            return -1
         
        