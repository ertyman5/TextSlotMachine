import random

MAX_LINES = 3   # Global constant variable
MAX_BET = 100
MIN_BET = 1

# 3x3 slot machine, if you get 3 in a row you win (simple as that), not balanced enough but it's fine for now

ROWS = 3
COLS = 3

# Dictionary for symbols
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

# Dictionary for symbols multiplier, rarity -> higher multiplier
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}
# -----------------------
# Check to see if every single symbol in the line is the same
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):  # Loop every row the user has a bet on:  0 -> 1line bet; 1 -> 2lines bet; 2->3lines bet
        symbol = columns[0][line]   # First column on the first row
        for column in columns:      # Loop trough every single column
            symbol_to_check = column[line]
            if symbol != symbol_to_check:   # If not the same, break and check the next line
                break
        else:                                   # This is a for else, my first time using it:
            winnings += values[symbol] * bet
            winning_lines.append(line+1)        # Index, so we add 1
    return winnings, winning_lines
#------------------------
# -----------------------
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():    # Using .items() gives me the key and the associate value with a dictionary
        for _ in range(symbol_count):   # loop through something when you don't care for the value
            all_symbols.append(symbol)

    #columns = [[], [], []]  -> each nested list is going to represent each value in our columns instead of a typical way of dealing with nested lists
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]    # [:] -> Copy instead of reference
        for _ in range(rows):
            value = random.choice(all_symbols)  # When we select a symbol we need to remove it from the OG list, preventing from adding more symbols that there were supposed to be
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns
# -------------------------
# Transposing:
def print_slot_machines(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):    # We only want the | in the middle, not in the last print
            if i != len(columns) - 1:           # Why the len(columns)-1? Because it's the max index possible
                print(column[row], end=" | ")    # end defaults to "\n" (new line), we want the '|' at the end
            else:
                print(column[row], end="")
                                                # Additional check for the next line
        print()
# --------------------------------------
def deposit():
    while True:
        amount = input("What would you like to deposit? €")
        if amount.isdigit():    # I need to first check this before int casting
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid amount of €.")

    return amount
# ------------------------
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():    # I need to first check this before int casting
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:     # Check if value is in between 2 values
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines
#-------------------------
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? €")
        if amount.isdigit():    # I need to first check this before int casting
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET}€ - {MAX_BET}€.")   # MIN_BET AND MAX_BET don´t need to be converted to string so this works fine using the f
        else:
            print("Please enter a valid amount of €.")

    return amount
#-------------------------
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: {balance}€")
        else:
            break

    print(f"You are betting on {bet}€ on {lines} lines. Total bet is equal to: {total_bet}€. ")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machines(slots)
    winnings, winning_lines = check_winnings(slots,lines,bet,symbol_value)
    print(f"!!!You won {winnings}€!!!")
    print(f"You won on lines:", *winning_lines)   # * -> Unpass operator

    return winnings - total_bet
def main():
    balance = deposit()
    while True:
        print(f"Current balance is : {balance}€")

        if balance <= 0:
            answer = input("You're out of money. Would you like to deposit more (d) or quit (q)?")
            if answer == "d":
                balance += deposit()
            elif answer == "q":
                break
            else:
                print("Invalid choice of input")
                continue
        else:
            answer = input("Press Enter to spin (q to quit).")
            if answer == "q":
                break
            balance += spin(balance)

    print(f" You are left with {balance}€.")


main()
# 1st Iteration
