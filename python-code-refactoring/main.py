"""Readable version of a small book-summary helper."""


def format_book_summary(title: str, author: str, pages: int) -> str:
    """Build a consistent one-line summary for a book."""
    clean_title = title.strip()
    clean_author = author.strip()

    if not clean_title:
        raise ValueError("Book title cannot be empty.")
    if not clean_author:
        clean_author = "Unknown author"
    if pages < 1:
        raise ValueError("Page count must be positive.")

    return f'"{clean_title}" by {clean_author} ({pages} pages)'


def main() -> None:
    try:
        print(format_book_summary("  Atomic Habits  ", "James Clear", 320))
    except ValueError as error:
        print(f"Could not create summary: {error}")


if __name__ == "__main__":
    main()
