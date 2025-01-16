from ._anvil_designer import HorizontalProgressbarTemplate
from anvil import *
import anvil.server


class HorizontalProgressbar(HorizontalProgressbarTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.obj = anvil.js.get_dom_node(self)

  @property
  def value(self):
      return self._value

  @value.setter
  def value(self,value_prop):
      self._value = value_prop
      try:
          anvil.js.call("HorizontalProgressbarSetter", self.obj, self._value)
      except:
          # print("component not ready")
          pass
