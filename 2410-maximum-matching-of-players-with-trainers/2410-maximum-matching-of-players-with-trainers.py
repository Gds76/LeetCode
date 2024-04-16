class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players = sorted(players)
        trainers = sorted(trainers)
        i = 0
        j = 0
        k = 0
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                k+=1
                i+=1
                j+=1
            elif players[i] > trainers[j]:
                j+=1
        return k 
        