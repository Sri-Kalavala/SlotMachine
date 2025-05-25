import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COlS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    # Start by defining our columns list
    columns = []
    # Then, we are going to generate a column for every single column we have
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


# A good place to start is collecting some user input.
# We need to get the user's deposit and then their bet to be able to start
# The first input we want from the code is the user's deposit
def deposit():
    # We can make a loop that asks the user for how much they want to deposit, but we also
    # have to account for the fact that they might not enter a valid number. We need to make
    # sure that their number is actually a number and that it is greater than 0.
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            # Once we find that the value is greater than 0, we have to change it from a string to an integer
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0. ")
        else:
            print("Please enter a number. ")
    return amount


def get_number_of_lines():
    while True:
        # Because the value has to be from 1 to 3, we can start them off by writing 1-
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            # Once we find that the value is greater than 0, we have to change it from a string to an integer
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines. ")
        else:
            print("Please enter a number. ")
    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            # Once we find that the value is greater than 0, we have to change it from a string to an integer
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print("Amount must be between " + str(MIN_BET) + "- " + str(MAX_BET))
                # Can also be written as:
                # print(f"Amount must be between {MIN_BET} - {MAX_BET}")
        else:
            print("Please enter a number. ")
    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        # Need to make sure that your total bet is not more than your balance
        bet = get_bet()
        total_bet = lines * bet
        if total_bet < balance:
            break;
        else:
            print(f"Please enter a bet that is within your balance amount. Your current balance is {balance}: ")

    print(f"You are betting ${bet} on {lines} lines. Your total bet is ${total_bet}")

main()