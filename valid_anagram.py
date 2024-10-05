# LeetCode 242: Valid Anagram

def isAnagram(self, s, t):
    def letter_counter(word):
        counter = dict()
        for l in word:
            if counter.get(l) is None:
                counter[l] = 1
            else:
                counter[l] += 1
                
        return counter
    
    s_counter = letter_counter(s)
    t_counter = letter_counter(t)

    return s_counter == t_counter
        
if __name__ == "__main__":
    print(isAnagram("", "car", "rat"))