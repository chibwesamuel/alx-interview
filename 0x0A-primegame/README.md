# Prime Game

## Description

Maria and Ben are playing a game where they take turns choosing prime numbers from a set of consecutive integers starting from 1 up to and including n. They remove the chosen number and its multiples from the set. The player who cannot make a move loses the game. This program determines the winner of each game played over multiple rounds.

## Prototype

```python
def isWinner(x, nums)
```

## Parameters

- `x`: The number of rounds played.
- `nums`: An array of integers representing the value of n for each round.

## Returns

- The name of the player who won the most rounds.
- If the winner cannot be determined, returns `None`.

## Constraints

- `n` and `x` will not be larger than 10,000.
- No packages can be imported for this task.

## Example

```python
x = 3
nums = [4, 5, 1]
```

- First round: 4
  - Maria picks 2 and removes 2, 4, leaving 1, 3.
  - Ben picks 3 and removes 3, leaving 1.
  - Ben wins because there are no prime numbers left for Maria to choose.
- Second round: 5
  - Maria picks 2 and removes 2, 4, leaving 1, 3, 5.
  - Ben picks 3 and removes 3, leaving 1, 5.
  - Maria picks 5 and removes 5, leaving 1.
  - Maria wins because there are no prime numbers left for Ben to choose.
- Third round: 1
  - Ben wins because there are no prime numbers for Maria to choose.
  
Result: Ben has won the most rounds.
