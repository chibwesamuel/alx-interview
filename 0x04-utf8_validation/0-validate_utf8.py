#!/usr/bin/python3
"""
Determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    This function checks if the provided data set contains valid UTF-8
    encoded characters. A character in UTF-8 can be 1 to 4 bytes long,
    and each byte is represented as an integer in the data list. The
    function verifies whether the data set forms valid UTF-8 characters.

    Args:
        data (list[int]): A list of integers representing a data set
        containing UTF-8 encoded characters. Each integer represents 1
        byte of data (8 least significant bits).

    Returns:
        bool: True if the data set is a valid UTF-8 encoding,
        False otherwise.

    Example:
        >>> data = [65]
        >>> validUTF8(data)
        True

        >>> data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32,
        99, 111, 111, 108, 33]
        >>> validUTF8(data)
        True

        >>> data = [229, 65, 127, 256]
        >>> validUTF8(data)
        False
    """
    num_bytes = 0

    for byte in data:
        # Check if the byte is a continuation byte (i.e., starts
        # with 10xxxxxx)
        if num_bytes == 0:
            if (byte & 0b10000000) == 0:
                num_bytes = 1
            else:
                # Determine the number of leading 1 bits in the byte
                while (byte & 0b10000000) != 0:
                    byte <<= 1
                    num_bytes += 1

                # The first byte should have the correct number of leading 1s
                if num_bytes < 2 or num_bytes > 4:
                    return False

            # If the character has only one byte, no need to check further
            if num_bytes == 1:
                continue

        else:
            # If the byte is a continuation byte, should start with 10xxxxxx
            if (byte & 0b11000000) != 0b10000000:
                return False

        # Decrease the number of remaining bytes to complete the character
        num_bytes -= 1

    # If there are remaining bytes to complete the character, it's invalid
    return num_bytes == 0

if __name__ == "__main__":
    # The code below is for testing the function, as described in the task

    data = [65]
    print(validUTF8(data))

    data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99,
            111, 111, 108, 33]
    print(validUTF8(data))

    data = [229, 65, 127, 256]
    print(validUTF8(data))
