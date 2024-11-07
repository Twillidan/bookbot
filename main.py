def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    print(text)
    print(word_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    count = len(words)
    return count

if __name__ == "__main__":
    main()