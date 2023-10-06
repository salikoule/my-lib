import anvil.server
import random


def generate_pastel_color() -> str:
  # Generate a random pastel color
  r = random.randint(150, 255)
  g = random.randint(150, 255)
  b = random.randint(150, 255)
  return f'rgba({r}, {g}, {b}, 0.8)'
