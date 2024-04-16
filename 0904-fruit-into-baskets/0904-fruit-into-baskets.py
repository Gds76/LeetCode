class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits = 0
        count = {}
        i = 0

        for j in range(len(fruits)):
            fruit = fruits[j]
            count[fruit] = count.get(fruit, 0) + 1

            while len(count) > 2:
                left_fruit = fruits[i]
                count[left_fruit] -= 1
                if count[left_fruit] == 0:
                    del count[left_fruit]
                i += 1

            max_fruits = max(max_fruits, j - i + 1)

        return max_fruits
    

        