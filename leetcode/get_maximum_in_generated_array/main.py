class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n <= 1:
            return n

        array = [0 for _ in range(n + 1)]
        array[1] = 1
        max_element = 1

        for i in range(2, n + 1):

            if i % 2 == 0:
                array[i] = array[i // 2]
            else:
                half_index = i // 2
                array[i] = array[half_index] + array[half_index + 1]

            max_element = max(max_element, array[i])

        return max_element
