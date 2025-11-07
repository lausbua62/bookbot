def get_book_text(path_to_file):
    with open(path_to_file) as f:
        # f is a file object, so:
        file_contents = f.read()
        return file_contents

def get_character_count(path_to_file):
    
    character_dict = {}
    text = get_book_text(path_to_file).lower()
    for char in text:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    #return character_dict
    return dict(sorted(character_dict.items(), key=lambda item: item[1], reverse=True))
    
def get_num_words(path_to_file):
    
    return f"Found {len(get_book_text(path_to_file).split())} total words"
