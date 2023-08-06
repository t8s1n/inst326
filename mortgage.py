# Template
"""Perform fixed-rate mortgage calculations."""

from argparse import ArgumentParser
import math
import sys


# replace this comment with your implementation of get_min_payment(),
# interest_due(), remaining_payments(), and main()

def get_min_payment(principal, annual_interest_rate, mortgage_term=30, payments_per_year=12):
    r = annual_interest_rate / payments_per_year

    n = mortgage_term * payments_per_year

    minimum_mortgage_payment = (principal * r * (1 + r) ** n) / ((1 + r) ** n - 1)

    minimum_mortgage_payment = math.ceil(minimum_mortgage_payment)

    return minimum_mortgage_payment


def interest_due(mortgage_balance, annual_interest_rate, payments_per_year=12):
    r = annual_interest_rate / payments_per_year

    amount_interest_due = mortgage_balance * r

    return amount_interest_due


def remaining_payments(mortgage_balance, annual_interest_rate, target_payment, payments_per_year=12):
    payments_to_be_made = 0

    while mortgage_balance > 0:
        interest_payment = interest_due(mortgage_balance, annual_interest_rate, payments_per_year)
        principal_balance_payment = target_payment - interest_payment

        if principal_balance_payment < 0:
            return -1

        mortgage_balance -= principal_balance_payment
        # increase the counter
        payments_to_be_made += 1

    return payments_to_be_made


def main(principal, annual_interest_rate, mortgage_term=30, payments_per_year=12, target_payment=None):
    minimum_payment = get_min_payment(principal, annual_interest_rate, mortgage_term, payments_per_year)

    print(f'the minimum payment for this mortgage is ${minimum_payment}')

    if target_payment is None:
        target_payment = minimum_payment

    if target_payment < minimum_payment:
        print("Your target payment is less than the minimum payment for this mortgage.")
        return

    total_payments = remaining_payments(principal, annual_interest_rate, target_payment, payments_per_year)

    if total_payments == -1:
        print("You're going to go bankrupt!")
    else:
        print(f"If you make payments of ${target_payment}, you will pay off the mortgage in {total_payments} payments.")


def parse_args(arglist):
    """Parse and validate command-line arguments.

    Args:
        arglist (list of str): list of command-line arguments.

    Returns:
        namespace: the parsed arguments (see argparse documentation for
        more information)

    Raises:
        ValueError: encountered an invalid argument.
    """
    # set up argument parser
    parser = ArgumentParser()
    parser.add_argument("mortgage_amount", type=float,
                        help="the total amount of the mortgage")
    parser.add_argument("annual_interest_rate", type=float,
                        help="the annual interest rate, as a float"
                             " between 0 and 1")
    parser.add_argument("-y", "--years", type=int, default=30,
                        help="the term of the mortgage in years (default: 30)")
    parser.add_argument("-n", "--num_annual_payments", type=int, default=12,
                        help="the number of payments per year (default: 12)")
    parser.add_argument("-p", "--target_payment", type=float,
                        help="the amount you want to pay per payment"
                             " (default: the minimum payment)")
    # parse and validate arguments
    args = parser.parse_args()
    if args.mortgage_amount < 0:
        raise ValueError("mortgage amount must be positive")
    if not 0 <= args.annual_interest_rate <= 1:
        raise ValueError("annual interest rate must be between 0 and 1")
    if args.years < 1:
        raise ValueError("years must be positive")
    if args.num_annual_payments < 0:
        raise ValueError("number of payments per year must be positive")
    if args.target_payment and args.target_payment < 0:
        raise ValueError("target payment must be positive")

    return args


if __name__ == "__main__":
    try:
        args = parse_args(sys.argv[1:])
    except ValueError as e:
        sys.exit(str(e))
    main(args.mortgage_amount, args.annual_interest_rate, args.years,
         args.num_annual_payments, args.target_payment)
