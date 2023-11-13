import anvil.server
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
