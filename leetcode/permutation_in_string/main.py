from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_letters = Counter(s1)
        s1_length = len(s1)
        
        substring_letters = Counter()
        
        for index, letter in enumerate(s2):
            if index >= s1_length:
                letter_to_decrement = s2[index - s1_length]
                substring_letters[letter_to_decrement] -= 1
                if substring_letters[letter_to_decrement] == 0:
                    del substring_letters[letter_to_decrement]
            
            substring_letters[letter] += 1
            
            if substring_letters == s1_letters:
                return True
        
        return False
