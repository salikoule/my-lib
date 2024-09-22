import anvil.server
import anvil.tz
# This is a package.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from . import Package1
#
#    Package1.say_hello()
#

def centered_alert(content, title = "", buttons=None, large=False):
  """Centered Aligned Alert with blurred background effect"""
  return anvil.alert(content, title=title, buttons=buttons, large=large, role='center-alert')

def remove_trailing_spaces(text: str) -> str:
    """
    Removes trailing spaces from the given text.

    Args:
        text (str): The text to remove trailing spaces from.

    Returns:
        str or None: The text with trailing spaces removed, or None if the input is None.
    """
    return text.rstrip() if text is not None else None
