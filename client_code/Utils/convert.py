import anvil.server
import anvil.tz as tz
from datetime import datetime
import math
MILLINAMES = ['',' k',' m',' bn',' tn']

def utc_to_local_time(utc_time, format="%H:%M:%S %d/%m/%Y") -> datetime or None:
  """Converts the utc time to browser's timezone"""
  if utc_time is not None:
    if type(utc_time) is str:
      utc_time = datetime.strptime(utc_time, "%d/%m/%Y, %H:%M:%S")
    from_zone = tz.tzutc()
    to_zone = anvil.tz.tzlocal()
    utc_time = utc_time.replace(tzinfo=from_zone)
    central = utc_time.astimezone(to_zone)
    return central.strftime(format)
  else:
    return None

def millify(number:float or int !=None, precision:int = 0) -> str:
    """Converts big number to a friendly readable format"""
    n = float(number)
    millidx = max(0,min(len(MILLINAMES)-1,
                        int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))

    return f'{n / 10**(3 * millidx):.{precision}f}{MILLINAMES[millidx]}'

def string_to_hex_color(input_str:str != None) -> str:
    """
    Generates a unique hex color from any input string using a simple hash function.
    The color generated will not be too bright.

    Args:
        input_str (str): The input string to generate the color from.

    Returns:
        str: The generated hex color.
    """
    # Calculate the hash value of the input string
    hash_value = 0
    for char in input_str:
        hash_value = (hash_value * 31 + ord(char)) & 0xFFFFFFFF

    # Convert the hash value to a 24-bit RGB color
    red = (hash_value & 0xFF0000) >> 16
    green = (hash_value & 0x00FF00) >> 8
    blue = hash_value & 0x0000FF

    # Reduce the brightness of the RGB color
    red = int(red * 0.7)
    green = int(green * 0.7)
    blue = int(blue * 0.7)

    # Convert the RGB color to hex
    hex_color = "#%02x%02x%02x" % (red, green, blue)

    return hex_color

def hex_to_rgba(hex_color, alpha):
  hex_color = hex_color.lstrip('#')
  # Convert hex_color to RGB components
  r = int(hex_color[0:2], 16)
  g = int(hex_color[2:4], 16)
  b = int(hex_color[4:6], 16)
  return f'rgba({r}, {g}, {b}, {alpha})'


def datetime_to_pretty(time=False) -> str:
    """
    Get a datetime object or an int() Epoch timestamp and return a
    pretty string like 'an hour ago', 'Yesterday', '3 months ago',
    'just now', etc
    """
    now = datetime.utcnow()
    if type(time) is int:
        diff = now - datetime.fromtimestamp(time)
    elif isinstance(time, datetime):
        diff = now - time
    elif not time:
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
        days = day_diff // 7
        return str(days) + f" day{'s' if days > 1 else ''} ago"
    if day_diff < 31:
        weeks = day_diff // 7
        return str(weeks) + f" week{'s' if weeks > 1 else ''} ago"
    if day_diff < 365:
        months = day_diff // 30
        return str(months) + f" month{'s' if months > 1 else ''} ago"
    years = day_diff // 365
    return str(years) + f" year{'s' if years > 1 else ''} ago"
