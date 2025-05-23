def get_num_words(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    char_count = {}
    lowered_text = text.lower()
    
    for char in lowered_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count

def get_sorted_char_list(char_count_dict):
    char_list = []
    
    for char in char_count_dict:
        char_dict = {"char": char, "num": char_count_dict[char]}
        char_list.append(char_dict)
    
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list
