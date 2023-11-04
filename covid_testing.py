def is_valid_sample(sample_quality):
    """
    Test if the sample quality is acceptable.

    Returns True if the sample quality is high enough for valid test results
    and, False if it is not.
    """

    if sample_quality > .9:
        return True
    else:
        return False

    # if sample_quality >= .95:
    #     return True
    # else:
    #     return False


def is_valid_calibration(calibration_time):
    """
    Test if the calibration is acceptable.

    Returns True if the calibration time is low enough for valid results, and
    False if it is not.
    """

    if calibration_time < 5:
        return True
    else:
        return False


def main():
    total_tests = 0
    positive_tests = 0
    negative_tests = 0

    while True:
        demographics = []
        race_factor = input("Enter race: ")
        gender_factor = input("Enter gender: ")
        income_factor = input("Enter income: ")
        demographic_data = {
            "race": race_factor,
            "gender": gender_factor,
            "income": income_factor
        }
        demographics.append(demographic_data)

        answer = input("Test positive? [y,n or stop]: ")

        if answer == "y" or answer == "n":
            total_tests += 1
        else:
            break

        q = float(input("Sample quality: "))
        t = int(input("Hours since last calibration: "))  # changed this from MINUTES to HOURS

        if not is_valid_sample(q) or not is_valid_calibration(t):
            print()
            print("Error: invalid sample quality or calibration time.")
            print("Total tests: ", total_tests)
            print("Positive: ", positive_tests)
            print("Negative: ", negative_tests)
            print(demographics)
            return

        if is_valid_sample(q) and is_valid_calibration(t):  # changed this from or to and
            positive_tests += 1
        else:
            negative_tests += 1

    print()
    print("Total tests: ", total_tests)
    print("Positive: ", positive_tests)
    print("Negative: ", negative_tests)
    print(demographics)


main()
