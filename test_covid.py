# Background
# One of the scientists in your lab recently discovered that the threshold for the sample quality rate has been set too
# low. This has resulted in some samples being contaminated by other nearby samples during the RT-PCR amplification
# process, which in turn has led to a higher rate of false positives.
#
# You may remember that any sample quality value above .9 should be accepted, but now the threshold should be raised to
# greater than or equal to .95. The scientist has recommended that the data entry program for test results that you’ve
# developed be adjusted accordingly.
#
# Because your program is now being used on hundreds of workstations throughout the lab the Director would like you to
# create some unittests for the program to ensure that the correct version is installed on each workstation.
# The operators can periodically run the test suite to make sure their program is working correctly.
#
# The Director anticipates that the calibration rate threshold might need to be adjusted in the future.
# So she would like you to test that as well.
#
# Instructions
# Update the is_valid_sample function to use the new threshold of greater than or equal to .95. (2 points)
#
# Write a test script using pytest that imports and tests the is_valid_sample and is_valid_calibration functions.
# Your tests should test for acceptable and unacceptable levels. (4 points)
#
# In no less than 150 words reflect on how effective this approach will be. For example are there other parts of
# covid_testing.py that should be tested? Why? How easy will it be to make sure this program is deployed to all the
# workstations and that the tests are run? (4 points)

import pytest
from covid_testing import is_valid_sample, is_valid_calibration


def test_is_valid_sample():
    assert is_valid_sample(0.9) == False
    assert is_valid_sample(0.95) == True
    assert is_valid_sample(0.98) == True


def test_is_valid_calibration():
    assert is_valid_calibration(8) == False
    assert is_valid_calibration(4) == True
    assert is_valid_calibration(5) == False
