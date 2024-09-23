import anvil.server
from .Utils import remove_trailing_spaces
from datetime import datetime, date, timedelta
import anvil.tz as tz

DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DISPLAYED_DATETIME_FORMAT = '%d/%m/%Y, %H:%M:%S'

class DatetimeHandler():
    def __init__(self, date_format: str = None, datetime_format: str = None) -> None:
        self.date_format = date_format
        self.datetime_format = datetime_format

    @property
    def date_format(self):
        return self._date_format

    @date_format.setter
    def date_format(self, dformat):
        self._date_format = DEFAULT_DATE_FORMAT if not dformat or remove_trailing_spaces(dformat) == '' else dformat

    @property
    def datetime_format(self):
        return self._datetime_format

    @datetime_format.setter
    def datetime_format(self, dtformat):
        self._datetime_format = DISPLAYED_DATETIME_FORMAT if not dtformat or remove_trailing_spaces(dtformat) == '' else dtformat

    def get_local_datetime_now(self) -> datetime:
        """
        Get the current local date and time.

        Returns:
            datetime: The current date and time.
        """
        return datetime.now()

    def get_utc_datetime_now(self) -> datetime:
        """
        Get the current UTC date and time.

        Returns:
            datetime: The current date and time.
        """
        return datetime.utcnow()
    
    def get_date_now(self) -> date:
        """
        Get the current date.

        Args:
            timezone (str): The timezone to use for getting the current date.

        Returns:
            date: The current date.
        """
        current_date = datetime.now().date() # Get the current date
        return current_date

    def convert_utc_to_local(self, _datetime: datetime) -> datetime or None:
      """Converts the utc time to browser's timezone"""
      if _datetime is not None:
        if isinstance(_datetime, str):
          _datetime = datetime.strptime(_datetime, self.datetime_format)
        from_zone = tz.tzutc()
        to_zone = anvil.tz.tzlocal()
        _datetime = _datetime.replace(tzinfo=from_zone)
        central = _datetime.astimezone(to_zone)
        return central.strftime(self.datetime_format)
      else:
        return None

    def datetime_to_pretty(self, _datetime=False) -> str:
      """
      Get a datetime object or an int() Epoch timestamp and return a
      pretty string like 'an hour ago', 'Yesterday', '3 months ago',
      'just now', etc
      """
      now = datetime.utcnow()
      if isinstance(_datetime, int):
          diff = now - datetime.fromtimestamp(_datetime)
      elif isinstance(_datetime, datetime):
          diff = now - _datetime
      elif not _datetime:
          diff = 0
      second_diff = diff.seconds
      day_diff = diff.days
  
      if day_diff < 0:
          return ''
  
      if day_diff == 0:
          if second_diff < 10:
              return "just now"
          if second_diff < 60:
              return str(second_diff) + " seconds ago"
          if second_diff < 120:
              return "a minute ago"
          if second_diff < 3600:
              return str(second_diff // 60) + " minutes ago"
          if second_diff < 7200:
              return "an hour ago"
          if second_diff < 86400:
              return str(second_diff // 3600) + " hours ago"
      if day_diff == 1:
          return "Yesterday"
      if day_diff < 7:
          return str(day_diff) + " days ago"
      if day_diff < 31:
          return str(day_diff // 7) + " weeks ago"
      if day_diff < 365:
          return str(day_diff // 30) + " months ago"
      return str(day_diff // 365) + " years ago"