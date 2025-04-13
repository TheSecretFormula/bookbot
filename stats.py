def word_count(text):
    words = text.split()
    word_count = len(words)
    return word_count

def character_count(text):
    character_count = {}
    for char in text:
        char = char.lower()
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

def sort_on(dict):
    return dict ["count"]

def sort_chars(char_dict):
    chars_list = []
    for char, count in char_dict.items():
        char_info = {"char": char, "count": count}
        chars_list.append(char_info)

    chars_list.sort(reverse=True, key=sort_on)
    return chars_list