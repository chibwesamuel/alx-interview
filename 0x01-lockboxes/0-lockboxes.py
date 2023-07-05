#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list): A list of lists representing the boxes and their corresponding keys.

    Returns:
        bool: True if all boxes can be opened, otherwise False.
    """

    n = len(boxes)  # Total number of boxes
    unlocked = [False] * n  # List to track the unlocked status of each box
    unlocked[0] = True  # The first box (box 0) is unlocked

    keys_stack = boxes[0]  # Stack to store keys found while traversing

    while keys_stack:
        key = keys_stack.pop()
        if 0 <= key < n and not unlocked[key]:
            unlocked[key] = True
            keys_stack.extend(boxes[key])

    return all(unlocked)
