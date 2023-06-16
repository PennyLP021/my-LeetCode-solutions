class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]
        n = len(gain)
        i = 0
        for i in range(n):
            altitudes.append(gain[i] + altitudes[i])
            i += 1
        return max(altitudes)
        