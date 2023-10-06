import anvil.server
import random


def pastel_color(opacity:float = 0.8) -> str:
  """Generate a random pastel color.
     Default opacity is 0.8."""
  r = random.randint(150, 255)
  g = random.randint(150, 255)
  b = random.randint(150, 255)
  return f'rgba({r}, {g}, {b}, {opacity})'
