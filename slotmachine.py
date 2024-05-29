import random

MAX_LINE = 3
MAX_BET = 100
MIN_BET = 10

ROW = 3
COl = 3

# Symbols on the machine
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,

}

symbol_values = {
    "A": 8,
    "B": 6,
    "C": 4,
    "D": 2,

}


def check_winnings(columns, line, bet, values):
    win = 0
    win_line = []
    for line in range(line):
        symbols = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbols != symbol_to_check:
                break
        else:
            win += values[symbols] * bet
            win_line.append(line + 1)

    return win, win_line


# generating the Slot machine

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbol = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)

        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(column) - 1:
                print(column[row], end='|')
            else:
                print(column[row], end='')
        print()


# to get the Deposit amount

def deposit():
    while True:
        amount = input("Enter the deposit amount:")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Enter a valid amount")
        else:
            print("Enter a valid amount")
    return amount


# to get the number of lines to bet on

def get_line():
    while True:
        lines = input("Enter the number of line (1 -" + str(MAX_LINE) + ')?')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= 3:
                break
            else:
                print("Enter a valid lines")
        else:
            print("Enter a valid lines")
    return lines


# to get the bet amount

def get_bet():
    while True:
        amount = input("Enter the bet amount:")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} - {MAX_BET}")
        else:
            print("Enter a valid amount")
    return amount


def game(balance):
    lines = get_line()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print("not enough to bet")
            print(f"current Balance - {balance}")
        else:
            break

    print(f"Current balance - {balance}")
    print(f"You are betting - {bet}")
    print(f'Number of line - {lines}')
    print(f"Total bet - {total_bet}")

    slots = get_slot_machine_spin(ROW, COl, symbol_count)
    print_slot_machine(slots)
    win, win_line = check_winnings(slots, lines, bet, symbol_values)

    print(f"You have won {win}.")
    print(f"You have won on ", *win_line)

    return win - total_bet


def main():
    balance = deposit()

    while True:
        print(f"Current balance - {balance}")
        spin = input("Press enter to play, q to quit")

        if spin == 'q':
            break
        else:
            balance += game(balance)

    print(f"you are left with {balance}")


main()
