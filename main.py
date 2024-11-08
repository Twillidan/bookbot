def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    character_count = count_character(text)
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

def count_character(string):
    lowercase_string = string.lower()
    characters = {}
    for c in lowercase_string:
        if c.isalpha():
            characters[c] = characters.get(c, 0) + 1
    #sorted_characters = dict(sorted(characters.items()))
    sorted_characters = dict(sorted(characters.items(), key=lambda item: item[1], reverse=True))
    return (sorted_characters)

if __name__ == "__main__":
    main()