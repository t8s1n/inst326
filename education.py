import argparse
import sys
import pandas as pd


def most_educated(csv_read, state_abbreviation):
    df = pd.read_csv(csv_read)

    filtered_df = df[df['State'] == state_abbreviation]

    max_percentage = filtered_df['Percent of adults with a bachelor\'s degree or higher'].max()
    max_percentage_df = \
        filtered_df[filtered_df['Percent of adults with a bachelor\'s degree or higher'] == max_percentage]
    county_name = max_percentage_df['Area name'].iloc[0]
    return (county_name, max_percentage)


def parse_args(args):
    parser = argparse.ArgumentParser()

    parser.add_argument("csv_read", help="Path to the CSV file")
    parser.add_argument("state_code", help="Two-letter state code")

    return parser.parse_args(args)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])

    county, percentage = most_educated(args.csv_read, args.state_code)

    print(f"{percentage}% of adults in {county} have at least a bachelor’s degree")
