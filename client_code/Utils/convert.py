import anvil.server
import anvil.tz as tz
from datetime import datetime

def to_local_time(utc_time):
  """Converts the utc time to browser's timezone"""
  if utc_time is not None:
    if type(utc_time) is str:
      utc_time = datetime.strptime(utc_time, "%d/%m/%Y, %H:%M:%S")
    from_zone = tz.tzutc()
    to_zone = anvil.tz.tzlocal()
    utc_time = utc_time.replace(tzinfo=from_zone)
    central = utc_time.astimezone(to_zone)
    return central.strftime("%H:%M:%S %d/%m/%Y")
  else:
    return None

millnames = ['',' k',' m',' bn',' tn']
def millify(n):
    """Converts big number to a friendly readable format"""
    n = float(n)
    millidx = max(0,min(len(millnames)-1,
                        int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))

    return '{:.1f}{}'.format(n / 10**(3 * millidx), millnames[millidx])

def string_to_hex_color(input_str):
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
