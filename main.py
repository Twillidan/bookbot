def main ():
    # Specify the path to the book.
    file_path = 'books/frankenstein.txt'

    # Using a with block to open and read the books content into a string.
    with open(file_path, 'r') as book:
        book_content = book.read()  # Read entire content of the book into a string.

    # Now, book_contents contains the book's contents as a string.
    print(book_content)
# Only execute the code inside this block if this script is being run directly, not if it’s imported elsewhere.
if __name__ == "__main__":
    main()