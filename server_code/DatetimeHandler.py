import anvil.server
from .Utils import remove_trailing_spaces
from datetime import datetime, date, timedelta
import pytz

DEFAULT_TIMEZONE = 'UTC'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

class DatetimeHandler():
    def __init__(self, timezone: str = None, date_format: str = None) -> None:
        self.timezone = timezone
        self.date_format = date_format

    @property
    def timezone(self):
        return self._timezone

    @timezone.setter
    def timezone(self, tzone):
        tzone = DEFAULT_TIMEZONE if not tzone or remove_trailing_spaces(tzone) == '' else tzone
        self._timezone = pytz.timezone(tzone)

    @property
    def date_format(self):
        return self._date_format

    @date_format.setter
    def date_format(self, dformat):
        self._date_format = DEFAULT_DATE_FORMAT if not dformat or remove_trailing_spaces(dformat) == '' else dformat

    # def get_utc_datetime_now(self) -> datetime:
    #     """
    #     Returns the current date and time in UTC.

    #     This method retrieves the current date and time in Coordinated Universal Time (UTC)
    #     using the `datetime` module and the `pytz` library.

    #     Returns:
    #         datetime: The current UTC date and time.
    #     """
    #     return datetime.now(pytz.utc)

    def get_datetime_now(self) -> datetime:
        """
        Get the current date and time in the specified timezone.

        Returns:
            datetime: The current date and time in the specified timezone.
        """
        return datetime.now(self.timezone)
    
    def get_date_now(self) -> date:
        """
        Get the current date in the specified timezone.

        Args:
            timezone (str): The timezone to use for getting the current date.

        Returns:
            date: The current date in the specified timezone.
        """
        current_date = datetime.now(self.timezone).date() # Get the current date in the specified timezone
        return current_date

    def convert_to_timezone(self, _datetime: datetime = None) -> datetime:
        """
        Convert the provided datetime to the specified timezone.

        Args:
            _datetime (datetime): The datetime to convert.

        Returns:
            datetime: The converted datetime in the specified timezone.
        """
        target_datetime = _datetime.astimezone(self.timezone)
        return target_datetime

    def is_business_hours_workday(self, _datetime: datetime, start_time: str = '09:00', end_time: str = '17:00') -> bool:
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
    
    def is_midnight_workday(self, _datetime: datetime) -> bool:
        """
        Checks if the provided datetime is midnight (00:00), and workday (Monday - Friday).
        
        Args:
            t_datetime (datetime): The datetime to check.
            
        Returns:
            bool: True if the time is midnight and it's a weekday, False otherwise.
        """
        return True if _datetime.strftime('%H') == '00' and _datetime.weekday() < 5 else False
    
    def get_last_n_days(self, _date: date, n: int = 30) -> list:
        """
        Generate a list of the last 'n' days from a given date.

        Args:
            _date (date): The reference date from which to calculate the last 'n' days.
            n (int, optional): The number of days to include in the list. Defaults to 30.

        Returns:
            List[str]: A sorted list of the last 'n' days in 'YYYY-MM-DD' format.
        """
        last_n_days = []
        for i in range(n):
            day = _date - timedelta(days=i)
            last_n_days.append(day.strftime(self.date_format))
        return sorted(last_n_days)
    
    def get_date_n_working_days_before(self, _date: date = None, n: int = 0) -> date:
        """
        Gets the date that is `n` working days before the given date.

        Args:
            date (date): The starting date. Defaults to None.
            n (int): The number of working days to go back. Defaults to 0.

        Returns:
            date: The date that is `n` working days before the given date.

        Note:
            This function assumes that working days are Monday to Friday.
        """
        weekdays = [0, 1, 2, 3, 4]  # Assuming Monday to Friday are working days
        count = 0
        while count < n:
            _date -= timedelta(days=1)
            if _date.weekday() in weekdays:
                count += 1
        return _date.date()

    def get_date_n_days_before(self, _date: date = None, n: int = 0) -> date:
        """
        Gets the date that is `n` days before the given date.

        Args:
            date (date): The starting date. Defaults to None.
            n (int): The number of days to go back. Defaults to 0.

        Returns:
            date: The date that is `n` days before the given date.
        """
        return _date - timedelta(days=n)

    def get_date_n_days_after(self, _date: date = None, n: int = 0) -> date:
        """
        Gets the date that is `n` days after the given date.

        Args:
            date (date): The starting date. Defaults to None.
            n (int): The number of days to go back. Defaults to 0.

        Returns:
            date: The date that is `n` days before the given date.
        """
        return _date + timedelta(days=n)

    def get_all_timezones(self) -> list:
        """
        Get a list of all available timezones.

        Returns:
            list: A list of all available timezones.
        """
        return pytz.all_timezones

    def interval_past(self, _datetime: datetime, interval: int, unit: str) -> datetime:
        """
        Get the datetime that is `interval` units before the given datetime.

        Args:
            _datetime (datetime): The starting datetime.
            interval (int): The number of units to go back.
            unit (str): The unit of time to go back by. Can be 'days', 'hours', 'minutes', or 'seconds'.

        Returns:
            datetime: The datetime that is `interval` units before the given datetime.
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
            return None

    def units_passed(self, _datetime: datetime, unit: str) -> datetime:
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
        now = self.get_datetime_now()
        time_difference = now - _datetime

        if unit == 'days':
            return time_difference.days
        elif unit == 'hours':
            return time_difference.total_seconds() // 3600
        elif unit == 'minutes':
            return time_difference.total_seconds() // 60
        elif unit == 'seconds':
            return time_difference.total_seconds()
        else:
            raise ValueError("Unit must be 'days', 'hours', 'minutes', or 'seconds'.")