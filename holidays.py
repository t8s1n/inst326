import argparse
import requests
import sys


def get_holidays(country_code, year):
    api_url = f"https://date.nager.at/Api/v1/Get/{country_code}/{year}"
    request_response = requests.get(api_url)
    holidays = request_response.json()

    for holiday in holidays:
        print(f'{holiday["date"]}: {holiday["name"]}')


def parse_args(args):
    parser = argparse.ArgumentParser(description="fetch holidays for a given country and year")
    parser.add_argument("country_code", help="two-letter country code")
    parser.add_argument("year", help="four-digit year")
    return parser.parse_args(args)


if __name__ == "__main__":
    parsed_args = parse_args(sys.argv[1:])
    get_holidays(parsed_args.country_code, parsed_args.year)
