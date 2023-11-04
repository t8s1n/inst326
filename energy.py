""" Build a database of energy sources in the US. """
import csv
from argparse import ArgumentParser
import sqlite3
import sys


# replace this comment with your implementation of the EnergyDB class
class EnergyDB:
    """
    provides an interface to read data from a CSV file into an in-memory SQLite database
        and query the data based on source and year.

    attributes:
        conn (sqlite3 connection): connection to the in-memory SQLite database
    """
    def __init__(self, filename):
        """
        initializes an EnergyDB object and reads the data from the given CSV file.

        args:
            filename (str): path to the CSV file

        side effects:
            creates an in-memory SQLite database and populates it with the data from the CSV file
        """
        self.conn = sqlite3.connect(':memory:')
        self.read(filename)

    def __del__(self):
        """
        destructor for the EnergyDB object

        side effects:
            closes the SQLite database connection
        """
        try:
            self.conn.close()
        except:
            pass

    def read(self, filename):
        """
        reads energy production data from a CSV file and populates the SQLite database.

        args:
            filename (str): path to the CSV file

        side effects:
            populates the SQLite database with the data from the CSV
        """
        cursor = self.conn.cursor()
        cursor.execute(
            "CREATE TABLE production "
            "(year integer, state text, source text, mwh real)"
            ""
        )

        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                year = int(row[0])
                mwh = float(row[3])
                cursor.execute(
                    "INSERT INTO production VALUES (?, ?, ?, ?)",
                    (year, row[1], row[2], mwh)
                )

        self.conn.commit()

    def production_by_source(self, source, year):
        """
        retrieves the total energy production for a given source and year.

        Args:
            source (str): the type of energy source
            year (int): the year of interest

        Returns:
            float: total energy production in Megawatt-hours (MWh) for the given source and year.
        """
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT mwh FROM production WHERE source=? AND year=?",
            (source, year)
        )
        rows = cursor.fetchall()
        total = sum([row[0] for row in rows])
        return total


def main(filename):
    """ Build a database of energy sources and calculate the total production
    of solar and wind energy.
    
    Args:
        filename (str): path to a CSV file containing four columns:
            Year, State, Energy Source, Megawatthours.
    
    Side effects:
        Writes to stdout.
    """
    e = EnergyDB(filename)
    sources = [("solar", "Solar Thermal and Photovoltaic"),
               ("wind", "Wind")]
    for source_lbl, source_str in sources:
        print(f"Total {source_lbl} production in 2017: ",
              e.production_by_source(source_str, 2017))


def parse_args(arglist):
    """ Parse command-line arguments. """
    parser = ArgumentParser()
    parser.add_argument("file", help="path to energy CSV file")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)
