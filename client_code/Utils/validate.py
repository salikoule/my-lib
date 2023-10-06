import anvil.server
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from .Utils import Module1
#
#    Module1.say_hello()
#

def email_format(email: str) -> bool:
  """  A valid email has the format: username@domain
  Username can contain letters, numbers, underscores and periods
  Domain can contain letters, numbers, hyphens and periods
  Domain must end with a valid top-level domain (e.g. .com, .org, .net)"""
  pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
  return re.match(pattern, email) is not None
