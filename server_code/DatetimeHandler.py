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
        return _date

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

    def get_all_timezones(self) -> list:
        """
        Get a list of all available timezones.

        Returns:
            list: A list of all available timezones.
        """
        return pytz.all_timezones