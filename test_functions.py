import pytest
import tempfile
import os
from functions import dice_roll, csv_list

# Testing the dice roll function works as needed by checking if it correctly removes the 1 dice roll value
# and therefore the end roll is between 3 and 18 inlcusive
def test_dice_roll():
    for i in range(100): # runs test 100 times to make sure
        rolls = dice_roll(4)
        assert 3 <= rolls <= 18

# Had to create this test with no files to run properly, not sure how to fix yet
# This test will create a temp csv file before it then checks my csv_list function is working correctly
# it will then remove the file as it won't be necessary after testing.
def test_csv_list():
    # create a temporary file
    with open("test_file.csv", "w") as f:
        f.write("testing")

    # call csv_list() function
    expected_output = ["test_file.csv"]
    assert csv_list() == expected_output

    # removes temp file after test finishes
    os.remove("test_file.csv")

