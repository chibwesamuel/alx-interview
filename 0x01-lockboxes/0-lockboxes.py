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
    unlocked = set()  # Set to track the unlocked boxes
    keys = set(boxes[0])  # Set to store the keys in the first box

    for box in range(n):
        if box in unlocked or box == 0:
            unlocked.update(boxes[box])

    return len(unlocked) == n
