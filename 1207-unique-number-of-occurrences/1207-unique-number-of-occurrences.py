class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = dict()
        for num in arr:
            counts[num] = counts.get(num, 0) + 1   
        count = counts.values()
        return len(count) == len(set(count))
            
        
        
            


# occurrence = collections.Counter(arr) | from collections import Counter, occurrence = Counter(arr)
# count = occurrence.values()
# return len(count) == len(set(count))
                
                
                
            
        
        
                    
            