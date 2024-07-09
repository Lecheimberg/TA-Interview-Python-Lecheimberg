import subprocess
import pytest
from bank_account import BankAccount

# Define the command to execute your Python script
command = ["python", "nature_of_numbers.py"]

# Define the input data for all test cases
input_data = "24\nY\n225\nN\n"

# Function to execute the command and capture output
def run_program(input_data):
    result = subprocess.run(command, input=input_data, text=True, capture_output=True)
    return result.stdout

# Write your tests here
def testcase_01():
    assert True


if __name__ == "__main__":
    pytest.main()