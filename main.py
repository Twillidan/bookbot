def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    character_count = count_character(text)
    print(text)
    print(f"This book contains {word_count} number of words")
    print(f"List of how often each character appears")
    print(character_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(string):
    words = string.split()
    count = len(words)
    return count

def count_character(string):
    lowercase_string = string.lower()
    characters = {}
    for c in lowercase_string:
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1
    return (characters)

if __name__ == "__main__":
    main()