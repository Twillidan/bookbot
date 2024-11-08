import argparse

def main():
    args = parser.parse_args()
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    character_count = count_character(text, args.order)
    print(text)
    print(f"--- Begining report for {book_path} ---")
    print(f"{word_count} Words found in this book")
    print(f"List of how often each character appears")
    for c in character_count:
        print(f"The letter {c} appears {character_count[c]} times")
    #print(character_count)
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(string):
    words = string.split()
    count = len(words)
    return count

def count_character(string, order=1):
    lowercase_string = string.lower()
    characters = {}
    reverse_sort = order == 1
    for c in lowercase_string:
        if c.isalpha():
            characters[c] = characters.get(c, 0) + 1
    #sorted_characters = dict(sorted(characters.items()))
    sorted_characters = dict(sorted(characters.items(), key=lambda item: item[order], reverse=reverse_sort))
    return (sorted_characters)

if __name__ == "__main__":
        # Setup the argument parser
    parser = argparse.ArgumentParser(description='Sort character frequency.')
    parser.add_argument('order', type=int, choices=[0, 1], help='0 for alphabetical, 1 for frequency')
    main()