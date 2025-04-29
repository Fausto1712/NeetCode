from datetime import datetime

def date_to_unix(date_str, format="%Y-%m-%d %H:%M:%S"):
    """
    Converts a given date string to a Unix timestamp.

    :param date_str: Date string (e.g., "2025-03-24 12:30:00")
    :param format: Format of the input date string
    :return: Unix timestamp (int)
    """
    dt = datetime.strptime(date_str, format)
    return int(dt.timestamp())

# Example usage
date_input = input("Enter a date (YYYY-MM-DD HH:MM:SS): ")
unix_timestamp = date_to_unix(date_input)
print(f"Unix timestamp: {unix_timestamp}")
