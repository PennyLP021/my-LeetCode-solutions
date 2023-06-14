class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        n = len(candies)
        i = 0
        while i < n:
            result.append((candies[i] + extraCandies) >= max(candies))
            i += 1
            
        return result
                