class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        max_rad = 0
        n = len(heaters)
        for house in houses:
            close_heater = inf
            l = 0
            r = n-1
            while l <= r:
                mid = (l+r)//2
                close_heater = min(close_heater, abs(house - heaters[mid]))
                if house <= heaters[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            max_rad = max(max_rad, close_heater)
        return max_rad
        