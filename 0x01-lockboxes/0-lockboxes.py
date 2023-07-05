#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
    boxes (list): A list of lists representing the boxes and their corresponding keys.

    Returns:
        bool: True if all boxes can be opened, otherwise False.
    """

    n = len(boxes) # Declares Total number of boxes
    unlocked = {0} # Set to track all unlocked boxes
    keys = set(boxes[0]) # Set to store keys in the first box

    while keys:
        key = keys.pop()
        if key < n and key not in unlocked:
            unlocked.add(key)
            keys.update(boxes[key])


    return len(unlocked) == n
