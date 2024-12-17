import anvil.server
from .Utils import remove_trailing_spaces
from datetime import datetime, date, timedelta
import pytz

DEFAULT_TIMEZONE = 'UTC'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

def get_datetime_now(timezone: str = DEFAULT_TIMEZONE) -> datetime:
    """
    Get the current date and time in the specified timezone.

    Args:
        timezone (str): The timezone to use for getting the current date and time. Defaults to 'UTC' .

    Returns:
        datetime: The current date and time in the specified timezone.
    """
    return datetime.now(pytz.timezone(timezone))

def get_date_now(timezone: str = DEFAULT_TIMEZONE) -> date:
    """
    Get the current date in the specified timezone.

    Args:
        timezone (str): The timezone to use for getting the current date. Defaults to 'UTC' .

    Returns:
        date: The current date in the specified timezone.
    """
    current_date = datetime.now(pytz.timezone(timezone)).date() # Get the current date in the specified timezone
    return current_date

def get_todays_datetime(timezone: str = DEFAULT_TIMEZONE) -> date:
    """
    Get the today's datetime at midnight time in the specified timezone.

    Args:
        timezone (str): The timezone to use for getting the current date. Defaults to 'UTC' .

    Returns:
        date: The current date in the specified timezone.
    """
    current_date = datetime.now(pytz.timezone(timezone)).date() # Get the current date in the specified timezone
    return datetime.combine(current_date, datetime.min.time())

def convert_to_timezone(_datetime: datetime, timezone: str = DEFAULT_TIMEZONE) -> datetime:
    """
    Convert a datetime object to the specified timezone.

    Args:
        _datetime (datetime): The datetime object to convert.
        timezone (str): The timezone to convert the datetime object to. Defaults to 'UTC'.

    Returns:
        datetime: The datetime object converted to the specified timezone.
    """
    return _datetime.astimezone(pytz.timezone(timezone))

def is_business_hours_workday(_datetime: datetime, start_time: str = '09:00', end_time: str = '17:00') -> bool:
    """
    Checks if the provided datetime is within business hours (9 AM - 5 PM) on a workday (Monday - Friday).

    Args:
        _datetime (datetime): The datetime to check.
        start_time (str): The start of business hours. Defaults to '09:00'.
        end_time (str): The end of business hours. Defaults to '17:00'.

    Returns:
        bool: True if the time is within business hours on a workday, False otherwise.
    """
    is_workday = _datetime.weekday() < 5
    is_business_hours = start_time <= _datetime.strftime('%H:%M') <= end_time
    return is_workday and is_business_hours

def is_midnight_workday(_datetime: datetime) -> bool:
    """
    Checks if the provided datetime is midnight (00:00), and workday (Monday - Friday).

    Args:
        _datetime (datetime): The datetime to check.

    Returns:
        bool: True if the time is midnight and it's a weekday, False otherwise.
    """
    return True if _datetime.strftime('%H') == '00' and _datetime.weekday() < 5 else False

def get_last_n_days(_date: date, n: int = 30, date_format: str = DEFAULT_DATE_FORMAT) -> list:
    """
    Generate a list of the last 'n' days from a given date.

    Args:
        _date (date): The reference date from which to calculate the last 'n' days.
        n (int, optional): The number of days to include in the list. Defaults to 30.
        date_format (str, optional): The format in which to return the dates. Defaults to '%Y-%m-%d'.

    Returns:
        List[str]: A sorted list of the last 'n' days in 'YYYY-MM-DD' format.
    """
    last_n_days = []
    for i in range(n):
        day = _date - timedelta(days=i)
        last_n_days.append(day.strftime(date_format))
    return sorted(last_n_days)

def get_date_n_working_days_before(_date: date = None, n: int = 0) -> date:
    """
    Gets the date that is `n` working days before the given date.

    Args:
        date (date): The starting date. Defaults to None.
        n (int): The number of working days to go back. Defaults to 0.

    Returns:
        date: The date that is `n` working days before the given date.
    """
    if _date is None:
        _date = get_date_now()
    while n > 0:
        _date -= timedelta(days=1)
        if _date.weekday() < 5:
            n -= 1
    return _date.date()

def get_date_n_days_before(_date: date = None, n: int = 0) -> date:
    """
    Gets the date that is `n` days before the given date.

    Args:
        date (date): The starting date. Defaults to None.
        n (int): The number of days to go back. Defaults to 0.

    Returns:
        date: The date that is `n` days before the given date.
    """
    if _date is None:
        _date = get_date_now()
    return _date - timedelta(days=n)

def get_all_timezones() -> list:
    """
    Get a list of all available timezones.

    Returns:
        list: A list of all available timezones.
    """
    return pytz.all_timezones

def interval_past(_datetime: datetime, interval: int, unit: str) -> datetime:
    """
    Get the datetime that is `interval` units in the past from the given datetime.

    Args:
        _datetime (datetime): The reference datetime.
        interval (int): The number of units to go back.
        unit (str): The unit of time to go back by. Can be 'days', 'hours', 'minutes', or 'seconds'.

    Returns:
        datetime: The datetime that is `interval` units in the past from the given datetime.
    """
    if unit == 'days':
        return _datetime - timedelta(days=interval)
    elif unit == 'hours':
        return _datetime - timedelta(hours=interval)
    elif unit == 'minutes':
        return _datetime - timedelta(minutes=interval)
    elif unit == 'seconds':
        return _datetime - timedelta(seconds=interval)
    else:
        raise ValueError("Invalid unit. Please choose from 'days', 'hours', 'minutes', or 'seconds'.")
    
def units_passed(_datetime: datetime, unit: str) -> datetime:
    """
    Calculate the number of specified time units passed since a given datetime.
    Args:
        _datetime (datetime): The starting datetime to compare against the current datetime.
        unit (str): The unit of time to calculate the difference in. 
                    Must be one of 'days', 'hours', 'minutes', or 'seconds'.
    Returns:
        datetime: The number of specified time units passed since the given datetime.
    Raises:
        ValueError: If the unit is not one of 'days', 'hours', 'minutes', or 'seconds'.
    """
    now = get_datetime_now()
    time_difference = now - _datetime
    if unit == 'days':
        return time_difference.days
    elif unit == 'hours':
        return time_difference.seconds // 3600
    elif unit == 'minutes':
        return time_difference.seconds // 60
    elif unit == 'seconds':
        return time_difference.seconds
    else:
        raise ValueError("Invalid unit. Please choose from 'days', 'hours', 'minutes', or 'seconds.")