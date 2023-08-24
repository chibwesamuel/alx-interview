# 0x08. Making Change

## Tasks

### 0. Change comes from within (mandatory)

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

- **Prototype:** `def makeChange(coins, total)`
- **Return:** The fewest number of coins needed to meet the total
  - If the total is 0 or less, return 0
  - If the total cannot be met by any number of coins you have, return -1
- `coins` is a list of the values of the coins in your possession
- The value of a coin will always be an integer greater than 0
- You can assume you have an infinite number of each denomination of coin in the list
- Your solution’s runtime will be evaluated in this task

### Example Usage

```python
makeChange([1, 2, 25], 37)  # Output: 7
makeChange([1256, 54, 48, 16, 102], 1453)  # Output: -1
```

## Repository

- **GitHub repository:** alx-interview
- **Directory:** 0x08-making_change
- **File:** 0-making_change.py

Feel free to explore and implement the provided tasks within this repository.
