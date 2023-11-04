""" Sort books by Library of Congress call number. """

from argparse import ArgumentParser
import re
import sys

# replace this comment with your implementation of the Book class
class Book:
    def __init__(self, callnum: str, title: str, author: str):
        """
        represents a book with a Library of Congress call number

        attributes:
            callnum: The call number for the book.
            title: The title of the book.
            author: The author of the book.
        """
        self.callnum = callnum
        self.title = title
        self.author = author

    def callnum_helper(self, callnum: str):
        """
        helper method that parses the given call number into its components

        params: callnum, the call number to be parsed

        returns: tuple, a tuple containing the parsed components of the call number

        possible errors: ValueError, If the provided call number is invalid
        """
        pattern = r'^(?P<subject_letters>[A-Z]{1,3})(?P<subject_number>\d+(\.\d+)?)(?:\s?\.(?P<cutter1_letter>[A-Z])(' \
                  r'?P<cutter1_number>\d+))?(?:\s?(?P<cutter2_letter>[A-Z])?(?P<cutter2_number>\d+))?\s?(?P<year>\d{' \
                  r'4})?$'
        match = re.match(pattern, callnum)
        if not match:
            raise ValueError(f"Invalid call number: {callnum}")
        components = match.groupdict()
        return (components['subject_letters'] or "",
                components['subject_number'] or "",
                (components['cutter1_letter'] or "",
                 int(components['cutter1_number']) if components['cutter1_number'] else 0),
                (components['cutter2_letter'] or "",
                 int(components['cutter2_number']) if components['cutter2_number'] else 0),
                int(components['year']) if components['year'] else -9999)  # default to a large negative value

    def __lt__(self, other):
        """
        determines if the current book's call number is less than the other book's call number.

        params: other, anOther Book instance

        returns: bool, True if the current book's call number is less than the other's, otherwise False if it isn't
        """
        self_components = self.callnum_helper(self.callnum)
        other_components = self.callnum_helper(other.callnum)
        self_tuple = (
            self_components[0],
            self_components[1],
            self_components[2][0],
            -self_components[2][1],
            self_components[3][0],
            -self_components[3][1],
            self_components[4]
        )
        other_tuple = (
            other_components[0],
            other_components[1],
            other_components[2][0],
            -other_components[2][1],
            other_components[3][0],
            -other_components[3][1],
            other_components[4]
        )
        return self_tuple < other_tuple

    def __repr__(self):
        """
        provides a string representation of a Book

        returns: str: a string that can be used to recreate a Book
        """
        escaped_title = self.title.replace('"', '\\"')
        escaped_author = self.author.replace("'", "\\'")
        return f"Book('{self.callnum}', \"{escaped_title}\", '{escaped_author}')"


# replace this comment with your implementation of the read_books() function
def read_books(file_path):
    """
    reads book details from a file and creates a list of Books

    params: filepath, The path to the file containing book details.

    returns: list, a list of Book instances based on the user file
    """
    books = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Splitting the line using tab character to get title, author, and call number
            title, author, callnum = line.strip().split('\t')

            # Create a Book object and add to the list
            books.append(Book(callnum, title, author))

    return books


def print_books(books):
    """ Print information about each book, in order. """
    for book in sorted(books):
        print(book)


def main(filename):
    """ Read book information from a file, sort the books by call number,
    and print information about each book. """
    books = read_books(filename)
    print_books(books)


def parse_args(arglist):
    """ Parse command-line arguments. """
    parser = ArgumentParser(arglist)
    parser.add_argument("filename", help="file containing book information")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filename)
