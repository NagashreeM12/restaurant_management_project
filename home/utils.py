# home/utils.py

from datetime import datetime, time

def is_restaurant_open():
    """
    Returns True if the restaurant is open based on the current day and time,
    otherwise returns False.
    """

    now = datetime.now()  # Get current date and time
    current_day = now.strftime("%A")  # e.g., 'Monday', 'Tuesday'
    current_time = now.time()

    # Define restaurant working hours (you can customize)
    # Example: open 9 AM to 10 PM daily
    opening_time = time(9, 0)   # 09:00 AM
    closing_time = time(22, 0)  # 10:00 PM

    # Optional: Different hours for weekends
    # if current_day in ['Saturday', 'Sunday']:
    #     opening_time = time(10, 0)
    #     closing_time = time(23, 0)

    # Check if current time is within opening hours
    if opening_time <= current_time <= closing_time:
        return True
    else:
        return False
