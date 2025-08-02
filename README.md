# MilitaryEnlistment
A simple Python script that calculates a user's age to determine their military enlistment status based on their birth year.

# 🎖️ Military Enlistment Checker

This is a command-line program written in Python that checks a person's military enlistment status based on their age. The program assumes an enlistment age of 18.

The script prompts the user for their birth year and the current year. It then calculates their age and provides one of three outcomes:
* It's time to enlist.
* How many years are left until enlistment.
* How many years have passed since they should have enlisted.

This project is a good exercise in handling user input, performing basic date/age calculations, and using conditional `if/elif/else` logic to provide different user feedback.

## How to Use

1.  Make sure you have Python installed on your system.
2.  Save the code as a `.py` file (e.g., `MilitaryEnlistment.py`).
3.  Open your terminal or command prompt.
4.  Navigate to the directory where the file is located and run the script:
    ```sh
    python MilitaryEnlistment.py
    ```
5.  Enter your birth year when prompted and press Enter.
6.  Enter the current year and press Enter to see your enlistment status.

## Logic

The program operates with the following logic:
* It calculates the user's `age` by subtracting the `birth_year` from the `enlistment_year`.
* It compares the calculated `age` to the standard enlistment age of 18.
* An `if/elif/else` block checks three conditions:
    * If `age` is exactly 18, it prints a message that it's time to enlist.
    * If `age` is less than 18, it calculates and displays how many years are left.
    * If `age` is greater than 18, it calculates and displays how many years have passed since the enlistment year.
