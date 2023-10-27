class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        i = 0
        for i in range(len(ransomNote)):
            if ransomNote[i] in magazine:
                magazine = magazine.replace(ransomNote[i], "", 1)
                i += 1
            else:
                break
        return i == len(ransomNote)

# strings are immutable so needs to assign a new value
# .replace() method replace the 1st argument with the 2nd argument for the 3rd argument's times  
# how about that        
