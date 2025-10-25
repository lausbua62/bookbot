def get_book_text(path_to_file):
    with open(path_to_file) as f:
        # f is a file object, so:
        file_contents = f.read()
        return file_contents
    
def get_num_words(path_to_file):
    return f"Found {len(get_book_text(path_to_file).split())} total words"
