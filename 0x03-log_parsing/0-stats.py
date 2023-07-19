#!/usr/bin/env python3
"""
Reads stdin line by line and computes metrics.
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
"""

import sys

def print_stats(total_size, status_counts):
    """
    Print the computed statistics.
    """
    print("File size:", total_size)
    for status_code, count in sorted(status_counts.items()):
        print(f"{status_code}: {count}")

def parse_line(line):
    """
    Parse the line and extract file size and status code.
    """
    parts = line.strip().split()
    if len(parts) < 8 or parts[-4] != "GET" or parts[-2].isdigit() == False:
        return None, None

    status_code = int(parts[-2])
    file_size = int(parts[-1])
    return status_code, file_size

def main():
    total_size = 0
    status_counts = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            status_code, file_size = parse_line(line)
            if status_code is not None and file_size is not None:
                total_size += file_size
                status_counts[status_code] = status_counts.get(status_code, 0) + 1

            if i % 10 == 0:
                print_stats(total_size, status_counts)
    except KeyboardInterrupt:
        print_stats(total_size, status_counts)

if __name__ == "__main__":
    main()

