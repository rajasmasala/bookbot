def get_num_words(book_string):
	return len(book_string.split())

def get_char_nums(book_string):
    char_dict = {}
    for char in book_string:
        if char.isalnum():
            char = char.lower()
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def sort_on(items):
    #print(ord(items["name"]))
    #print(items["num"])
    return items["num"]

def sorted_char_stats(dict_to_sort):
    sorted_dict = []

    for item in dict_to_sort:
        sorted_dict.append({"char": item,"num": dict_to_sort[item]})
    
    #print(sorted_dict.sort(key=sort_on))
    sorted_dict.sort(reverse=True, key=sort_on)

    return sorted_dict
