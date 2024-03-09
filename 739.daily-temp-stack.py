class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # [temp, index]
        res = [0] * len(temperatures)

        for i, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                stackT, stackIndex = stack.pop()
                res[stackIndex] = i - stackIndex

            stack.append([temperature, i])

        return res