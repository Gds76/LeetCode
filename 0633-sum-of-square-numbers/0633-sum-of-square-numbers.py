class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i, j = 0, int(c ** 0.5)

        while i <= j:
            sum_of_squares = i ** 2 + j ** 2
            if sum_of_squares == c:
                return True
            elif sum_of_squares < c:
                i += 1
            else:
                j -= 1

        return False
        