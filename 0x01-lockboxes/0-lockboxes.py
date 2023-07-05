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
    unlocked.add(0)  # Add the first box (box 0) as unlocked

    for box in unlocked:
        keys = boxes[box]  # Get the keys in the current box
        unlocked.update(keys)  # Update the unlocked set with the new keys

    return len(unlocked) == n
