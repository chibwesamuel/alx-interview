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
import re

# Global variables to store statistics
total_size: int = 0
status_counts: Dict[int, int] = defaultdict(int)

# Regular expression to match the expected input format
log_pattern = re.compile(r'(\S+) - \[.+\] "GET .+ (\d+) (\d+)"')


def print_stats() -> None:
    """
    Print the computed statistics.

    Args: None

    Returns: None
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
    match = log_pattern.match(line.strip())
    if match:
        status_code = int(match.group(2))
        file_size = int(match.group(3))
        return status_code, file_size

    return None, None


def handle_interrupt(signum: int, frame) -> None:
    """
    Handle KeyboardInterrupt by printing statistics and exiting.

    Args:
        signum (int): The signal number (e.g., SIGINT).
        frame: The current execution frame.

    Returns: None
    """
    print_stats()
    sys.exit(0)


# Register the signal handler for KeyboardInterrupt (CTRL + C)
signal.signal(signal.SIGINT, handle_interrupt)


def main() -> None:
    """
    Main function to compute metrics.

    Args: None

    Returns: None
    """
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
        Handle KeyboardInterrupt by printing statistics and exiting.

        Args: None

        Returns: None
        """
        pass

    # Print final statistics if the loop ends without KeyboardInterrupt
    print_stats()


if __name__ == "__main__":
    main()
