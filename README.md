[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/AU2_f2-C)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=19296804)
# Banking Application

## Overview

This Banking Application simulates a basic banking system allowing the creation and management of bank accounts. Users can create multiple accounts, transfer funds between them, and view account balances, providing a hands-on experience with a simple financial system.

## Features

- **Account Creation**: Users can create between 1 to 5 bank accounts at the beginning, specifying the account holder's name, account number, and initial balance.
- **Fund Transfers**: The application supports unlimited transfers between accounts, prompting users for the source, destination, and amount for each transfer.
- **Balance Display**: Displays the starting and ending balances of both the source and destination accounts before and after each transfer.

## Getting Started

To run the application, follow these steps:

1. Ensure you have Python and pip installed on your system.
2. Clone the repository to your local machine.
3. Navigate to the project directory.
4. Execute `python main.py` to start the application. The program will guide you through creating accounts and performing transfers.

## Testing

This project supports testing with the Python's `pytest` framework. You must to crete the file `test_bank_account.py` to add the testcases and requirements to run the tests, Here are suggested test scenarios:

### Account Creation

- As a start point you can create the `test_create_account()` method in `test_bank_account.py` to verify if a new `BankAccount` object is created with the correct details.

### Fund Transfer

- Test the `test_perform_transfer()` method in `test_bank_account.py` to ensure correct fund transfer between accounts. Include tests for edge cases, such as transferring more than the available balance.

### Balance Display

- Verify that the application correctly displays account balances before and after transfers.

To add a test, create a new file named `test_bank_application.py` and use `pytest` framework to write your tests. Use assertions to validate the outcomes.

## Autograding Setup

For GitHub Classroom autograding, follow these steps:

1. Create a new file named `autograding.json` in the `.github/classroom` directory of your repository.
2. Populate the file with your test configurations. Here's a template you can start with:

```json
{
  "tests": [
    {
      "name": "Test Account Creation",
      "setup": "pip install -r requirements.txt",
      "run": "pytest test_file_example.py::test_case",
      "input": "",
      "output": "",
      "comparison": "exact",
      "timeout": 10,
      "points": 10
    }
  ]
}