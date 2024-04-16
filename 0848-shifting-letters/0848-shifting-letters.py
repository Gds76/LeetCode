class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        def shift(a, k):
            a = char [char.index(a) + k] if char.index(a) + k < 26 else char[(k + char.index(a))%26]
            return a
        s = list(s)
        prefix_sum = [0] * len(shifts)
        shifts.reverse()
        prefix_sum[0] = shifts[0]
        for i in range(1, len(shifts)):
            prefix_sum[i] += prefix_sum[i-1] + shifts[i]
        prefix_sum.reverse()
        for i in range(len(shifts)):
                s[i] = shift(s[i], prefix_sum[i])
        print(prefix_sum)
        return "".join(s)

        