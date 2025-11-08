from stats import *
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(get_num_words(path))
    print("--------- Character Count -------")
    for key, value in get_character_count(path).items():
        print(f"{key}: {value}")
    #print(get_character_count(path))
    print("============= END ===============")


if __name__ == "__main__":
    main()