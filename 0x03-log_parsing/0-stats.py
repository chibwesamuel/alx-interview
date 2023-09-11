#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics.
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>
Return status codes in ascending order
"""

import sys
from collections import defaultdict
import signal
from typing import Dict, Tuple, Optional

# Global variables to store statistics
total_size: int = 0
status_counts: Dict[int, int] = defaultdict(int)


def print_stats() -> None:
    """
    Print the computed statistics.

    Args: None

    Return: none
    """
    print("File size:", total_size)
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")


def parse_line(line: str) -> Tuple[Optional[int], Optional[int]]:
    """
    Parse the line and extract file size and status code.

    Args:
        line (str): The input line to parse.

    Returns:
        Tuple[Optional[int], Optional[int]]: A tuple containing the status
        code and file size.
        Returns (None, None) if parsing fails.
    """
    parts = line.strip().split()
    if len(parts) < 8 or parts[-4] != "GET" or not parts[-2].isdigit():
        return None, None

    status_code = int(parts[-2])
    file_size = int(parts[-1])
    return status_code, file_size


def handle_interrupt(signum: int, frame) -> None:
    """
    Handle KeyboardInterrupt by printing statistics and exiting.

    Args:
        signum (int): The signal number (e.g., SIGINT).
        frame: The current execution frame.
    """
    print_stats()
    sys.exit(0)

# Register the signal handler for KeyboardInterrupt (CTRL + C)
signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line_counter, line in enumerate(sys.stdin, 1):
        status_code, file_size = parse_line(line)
        if status_code is not None and file_size is not None:
            total_size += file_size
            status_counts[status_code] += 1

        if line_counter % 10 == 0:
            print_stats()


except KeyboardInterrupt:
    """
    The signal handler will print statistics and exit

    Args: None

    Return: None
    """
    pass

# Print final statistics if the loop ends without KeyboardInterrupt
print_stats()


if __name__ == "__main__":
    """main function"""
    main()
