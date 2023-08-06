""" Find cities near a specified location. """

from argparse import ArgumentParser
import sys

from haversine import haversine


# Replace this comment with your implementation of the Cities class.
class Cities:
    """
    A "Cities" class, a class that represents a collection of cities.

    Attributes:
        cities: a dictionary of cities, each key is a tuple consisting of the state and the city, and each value is a
        tuple consisting of the latitude and longitude of the city.
    """
    def __init__(self, filename):
        """
        Reads the contents of a file and gathers attributes for the "cities" object.

        :param
            filename (str): path to a file containing city data

        """

        self.cities = {}

        with open(filename, 'r') as f:
            for line in f:
                state, city, lat, lon = line.strip().split(',')
                self.cities[(state, city)] = (float(lat), float(lon))

    def nearest(self, point):
        """
        Finds the nearest five closest cities to the point specified in the input.

        :param
            point (tuple): tuple consisting of longitude and latitude as floats

        :return:
            a list of the first five cities
        """
        sort_cities_distance = sorted(self.cities.items(), key=lambda x: haversine(point, x[1]))

        return [city[0] for city in sort_cities_distance[:5]]


def main(filename, arg1, arg2):
    """ Read city data from a file and find the closest cities to a
    specified location (either an area and city from filename or a
    latitude and longitude which may or may not be in the file).
    
    Args:
        filename (str): path to a file containing city data. Each line
            in the file should consist of four values, separated by
            commas: area (e.g., state or country), city, latitude in
            decimal degrees, longitude in decimal degrees.
        arg1 (str): either the name of an area in the file, or a string
            representation of a latitude.
        arg2 (str): either the name of a city in the file, or a string
            representation of a longitude.
    
    Side effects:
        Writes to stdout.
    """
    cities = Cities(filename)
    try:
        lat = float(arg1)
        lon = float(arg2)
        point = (lat, lon)
    except ValueError:
        try:
            point = cities.cities[arg1, arg2]
        except KeyError:
            sys.exit(f"Error: could not look up {arg1}, {arg2}")
    print(f"For {arg1}, {arg2}, the nearest cities from the file are")
    for result in cities.nearest(point):
        print("    " + ", ".join(result))


def parse_args(arglist):
    """ Process command-line arguments and return the parsed values as a
    namespace. """
    parser = ArgumentParser()
    parser.add_argument("filename", help="file containing city data")
    parser.add_argument("arg1",
                        help="a latitude expressed in decimal degrees"
                             " or an area (state, country) from the"
                             " file")
    parser.add_argument("arg2",
                        help="a longitude expressed in decimal degrees"
                             " or a city name from the file")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filename, args.arg1, args.arg2)
