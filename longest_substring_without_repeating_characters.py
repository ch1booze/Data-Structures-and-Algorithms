# LeetCode 3: Longest Substring Without Repeating Characters

def lengthOfLongestSubstring(self, s):
    current_index = 0
    start_substr_index = 0
    char_position_hashmap = dict()
    longest_substr_len = 0

    while current_index < len(s):
        if char_position_hashmap.get(s[current_index]) is not None:
            start_substr_index = char_position_hashmap[s[current_index]] + 1
            char_position_hashmap = dict()
            current_index = start_substr_index
        
        char_position_hashmap[s[current_index]] = current_index
        current_index += 1
        
        if longest_substr_len < len(char_position_hashmap):
            longest_substr_len = len(char_position_hashmap)
        
    return longest_substr_len
        

if __name__ == "__main__":
    print(lengthOfLongestSubstring("", "anviaj"))
