# Write a separate test script that imports your note positions script and tests the get_fret() and get_frets()
# functions. The name of your test script should contain the string "test" somewhere in the name.
# For get_fret():
# > test whether passing in the same value for target and string gives a return value of 0
# > test at least one case where target corresponds to a larger number in your dictionary than string
# (for example, if target is "A" and string is "C")
# > test at least one case where target corresponds to a smaller number in your dictionary than string
# (for example, if target is "C" and string is "A")
# > for a note that has two names, test whether the function returns the same value when target is the sharp as when
# target is the flat (for example, does "G#" give the same fret as "Ab"?)
# For get_frets():
# > test the function with a list consisting of a single string (e.g., ["G"]);
# check whether the function returns a dictionary with one key, and check whether the corresponding value is correct
# > test the function with a list consisting of multiple strings of different values[2] (e.g., ["G", "D", "A"]);
# check whether the function returns a dictionary with the same number of keys as the number of strings you passed in
# (assuming the strings are unique), and check whether the corresponding values are correct

from note_positions import get_fret, get_frets


def test_get_fret():
    assert get_fret('A', 'A') == 0  # passing in the same value for target and string gives a return value of 0
    assert get_fret('A', 'C') == 9  # at least one case where target corresponds to a > number in your dict than string
    assert get_fret('C', 'A') == 3  # at least one case where target corresponds to a < number in your dict than string
    assert get_fret('G#', 'A') == get_fret('Ab', 'A')  # note that has two names


def test_get_frets():
    single_string = get_frets('A',
                              ['G'])
    assert len(single_string) == 1
    assert single_string['G'] == 2

    multiple_strings = get_frets('A',
                                 ['G', 'D', 'A'])
    assert len(multiple_strings) == 3
    assert multiple_strings == {'G': 2,
                                'D': 7,
                                'A': 0}
