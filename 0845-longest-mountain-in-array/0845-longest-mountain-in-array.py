class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0

        longest = 0
        left = 0

        while left < n - 1:
            right = left + 1
            if right < n and arr[right] > arr[right - 1]:
                
                while right < n and arr[right] > arr[right - 1]:
                    right += 1
                peak = right - 1
                while right < n and arr[right] < arr[right - 1]:
                    right += 1
                if peak != left and peak != right - 1:
                    longest = max(longest, right - left)
                left = right - 1
            else:
                left += 1

        return longest



        