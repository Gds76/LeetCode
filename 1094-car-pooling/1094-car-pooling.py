class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        maxx = 0
        for i in range(len(trips)):
            maxx = max(maxx, trips[i][2])
        n = maxx +1
        locations = [0]*n
        for i in range(len(trips)):
            locations[trips[i][1]] += trips[i][0]
            locations[trips[i][2]] -= trips[i][0]
        prefix_sum = [0]*n
        prefix_sum[0] += locations[0]
        for i in range(1, len(locations)):
            prefix_sum[i] += prefix_sum[i-1] + locations[i] 
        for i in range(len(locations)):
            if prefix_sum[i] > capacity:
                return False
        print(prefix_sum)
        print(locations)
        return True


        