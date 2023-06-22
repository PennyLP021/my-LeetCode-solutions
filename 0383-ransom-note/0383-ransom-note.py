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
        