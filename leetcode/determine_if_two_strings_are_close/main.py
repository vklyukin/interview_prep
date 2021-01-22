from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1) != len(word2):
            return False
        
        if set(word1) != set(word2):
            return False
        
        word1_letters = Counter(word1)
        word2_letters = Counter(word2)
        
        word1_distribution = sorted(word1_letters.values())
        word2_distribution = sorted(word2_letters.values())
        
        return word1_distribution == word2_distribution
