# Prime Game

In this project, I demonstrate an algorithmic solution to the Prime Game, a game played by Maria and Ben. The goal is to determine the winner of each round of the game, given a set of consecutive integers starting from 1 up to and including n. They take turns choosing a prime number from the set and removing that number and its multiples from the set. The player who cannot make a move loses the game.

## Tasks

### Task 0: Prime Game

The main task is to implement a Python function called `isWinner` with the following signature:

```python
def isWinner(x, nums):
```

- `x` is the number of rounds they play.
- `nums` is an array of integers representing `n` for each round.
- The function should return the name of the player who won the most rounds.
- If the winner cannot be determined, it should return `None`.
- You can assume that `n` and `x` will not be larger than 10,000.
- You cannot import any external packages for this task.

## Example

Suppose we have three rounds with the following parameters:

```python
x = 3
nums = [4, 5, 1]
```

### First round: n = 4

- Maria picks 2 and removes 2, 4, leaving [1, 3].
- Ben picks 3 and removes 3, leaving [1].
- Ben wins because there are no prime numbers left for Maria to choose.

### Second round: n = 5

- Maria picks 2 and removes 2, 4, leaving [1, 3, 5].
- Ben picks 3 and removes 3, leaving [1, 5].
- Maria picks 5 and removes 5, leaving [1].
- Maria wins because there are no prime numbers left for Ben to choose.

### Third round: n = 1

- Ben wins because there are no prime numbers for Maria to choose.

Result: Ben has the most wins.

## Usage

You can use the provided Python script to test the `isWinner` function. Simply run the following command:

```bash
./main_0.py
```

This script imports the `isWinner` function and demonstrates its usage for a sample input.

## Repository

This project is part of the GitHub repository: [chibwesamuel/alx-interview](https://github.com/chibwesamuel/alx-interview)

### Directory and File

- Directory: 0x0A-primegame
- File: 0-prime_game.py

Feel free to explore the code in the repository for the complete implementation of the `isWinner` function and other related files.

If you have any questions or need further assistance, please don't hesitate to contact me. Happy coding!
