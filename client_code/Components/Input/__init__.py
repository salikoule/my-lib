from ._anvil_designer import InputTemplate
from anvil import *
import anvil.server

# add value properties for convenience
DatePicker.value = property(lambda self: self.date, lambda self, val: setattr(self, "date", val))
TextBox.value = property(lambda self: self.text, lambda self, val: setattr(self, "text", val))

class Input(InputTemplate):
  def __init__(self, error=None, type="text", key="", **properties):
    # Set Form properties and Data Bindings.
    self.init_components(error=error, type=type, key=key, **properties)

    self.label.text = key.capitalize()
    self.setup_input()

  def setup_input(self):
    if self.type == "date":
      self.input = DatePicker(format="DD-MM-YYYY")
      self.input_panel.clear()
      self.input_panel.add_component(self.input, expand=True)
    else:
      self.input = self.input_placeholder
      self.input.type = self.type
    self.input.add_event_handler("change", self.change)

  @property
  def error(self):
    return self._error

  @error.setter
  def error(self, error):
    self._error = error
    if not error:
      self.error_label.text = " "
    else:
      print(error, error.errors(self.key))
      self.error_label.text = "\n".join(error.errors(self.key)) or " "

  @property
  def value(self):
    return self.input.value

  @value.setter
  def value(self, value):
    self.input.value = value

  def change(self, **event_args):
    self.raise_event("change", key=self.key, value=self.value)
