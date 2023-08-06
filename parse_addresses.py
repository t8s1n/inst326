from argparse import ArgumentParser
import re
import sys


# replace this comment with your implementation of the parse_address()
def parse_address(address):
    """
    Parse one address string per line into a dictionary of its components

    :param address (str):
        a single line address string that will contain the format "house_number", "street", "city", "state", and "zip"

    :return:
        a dictionary with keys "house_number", "street", "city", "state", and "zip",
        if the regular expression is unsuccessful return None
    """
    address_expression = r"(\d+[\s\-\d]*)([\D]+),\s([A-Za-z\s]+)\s([A-Z]{2})\s(\d{5})"
    match = re.search(address_expression, address)

    if match:
        return {
            "house_number": match.group(1),
            "street": match.group(2).strip(),
            "city": match.group(3).strip(),
            "state": match.group(4),
            "zip": match.group(5)
        }
    else:
        return None


# and parse_addresses() functions.
def parse_addresses(file_path):
    """
    Parse addresses from a file into a list of dictionaries

    :param file_path (str):
        a path to a file containing one address per line

    :return:
        a list of dictionaries
    """
    with open(file_path, 'r') as file:
        addresses = file.readlines()
    return [parse_address(address) for address in addresses]


def parse_args(arglist):
    """ Parse command-line arguments. """
    parser = ArgumentParser()
    parser.add_argument("file",
                        help="file containing one address per line")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    for address in parse_addresses(args.file):
        print(address)
