class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]: 
        res = []
        for i in range(len(temperatures)):
            streak = 0
            found = False
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    streak = j - i
                    found = True
                    break
            res.append(streak if found else 0)
        return res