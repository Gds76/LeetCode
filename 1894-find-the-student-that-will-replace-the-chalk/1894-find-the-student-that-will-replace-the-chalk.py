class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        prefix_sum = [0]*(n+1)
        for i in range(1, n+1):
            prefix_sum[i] += prefix_sum[i-1] + chalk[i-1]
        prefix_sum.remove(prefix_sum[0])
        k = k%prefix_sum[-1]
        i = 0
        while i < n and prefix_sum[i%n] <= k:
            
            i+=1
            # elif i % n == 0:
            #     i+=1
            #     k = k - prefix_sum[-1]
        return i%n
        