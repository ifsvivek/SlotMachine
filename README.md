# Slot Machine Game

This is a simple slot machine game implemented in Python. The game is based on a 3x3 grid of symbols, and the player can bet on up to 3 lines.

<p align="center">
  <img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExeWE1Nnp2azVreXdsM2xobmZybXozeHNkeTVpbndmNm5nZTE1OThmeCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/dBHwHv1OVhtcLFHwrX/giphy.gif" alt="Your image" width="500">
</p>


## Code Structure

The code is structured as follows:

- `MAX_LINE`: The maximum number of lines a player can bet on.
- `MAX_BET`: The maximum amount a player can bet.
- `MIN_BET`: The minimum amount a player can bet.
- `ROW`, `COL`: The dimensions of the slot machine grid.
- `symbol_count`: A dictionary mapping each symbol to the number of times it appears on the slot machine.
- `symbol_values`: A dictionary mapping each symbol to its value in terms of winnings.

## Function

- `check_winnings(columns, line, bet, values)`: This function is used to calculate the winnings of a player. It takes in the following parameters:
  - `columns`: The current state of the slot machine.
  - `line`: The line the player has bet on.
  - `bet`: The amount the player has bet.
  - `values`: The values of the symbols.

The function is currently incomplete and will be updated in future versions of the game.

## How to Run

To run the game, you will need to have Python installed on your machine. You can then run the `slotmachine.py` script from your terminal.
