from app.models import Book, BookDisplay, BookPrint, BookSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    book_displays = BookDisplay(book)
    book_print = BookPrint(book)
    book_serialize = BookSerializer(book)
    for cmd, method_type in commands:
        if cmd == "display":
            book_displays.display(method_type)
        elif cmd == "print":
            book_print.print_book(method_type)
        elif cmd == "serialize":
            return book_serialize.serialize(method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
