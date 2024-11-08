import argparse

def main():
    args = parser.parse_args()
    #file_path = "books/frankenstein.txt"
    text = get_book_text(args.file_path)
    word_count = count_words(text)
    character_count = count_character(text, args.order)
    print(text)
    print(f"--- Begining report for {args.file_path} ---")
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

def count_character(string, order='alpha'):
    lowercase_string = string.lower()
    characters = {}
    reverse_sort = order == 'num'
    sort_key = 1 if order == 'num' else 0
    for c in lowercase_string:
        if c.isalpha():
            characters[c] = characters.get(c, 0) + 1
    sorted_characters = dict(sorted(characters.items(), key=lambda item: item[sort_key], reverse=reverse_sort))
    return (sorted_characters)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Sort character frequency.')
    parser.add_argument('file_path', type=str, help='Path to the text file')
    parser.add_argument('-o', '--order', type=str, choices=['alpha', 'num'], default='alpha', help='alpha for alphabetical (default), num for frequency')
    main()