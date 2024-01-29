```markdown
# Making Change

## Author
Samuel Mukosa Chibwe

## Description
This directory contains a Python implementation of an algorithm to determine the fewest number of coins needed to meet a given amount total, given a pile of coins of different values.

## Tasks
### Task 0: Change comes from within
Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

**Prototype:** 
```python
def makeChange(coins, total)
```

**Return:** 
- The fewest number of coins needed to meet the total
- If total is 0 or less, return 0
- If total cannot be met by any number of coins you have, return -1

**Parameters:**
- `coins`: a list of the values of the coins in your possession
  - The value of a coin will always be an integer greater than 0
- You can assume you have an infinite number of each denomination of coin in the list

**Note:** 
- Your solution’s runtime will be evaluated in this task

## Usage
```
makeChange(coins, total)
```

## Example
```python
print(makeChange([1, 2, 25], 37))  # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
```

## Testing
To test the implementation, run the following command in the terminal:
```
./0-main.py
```
