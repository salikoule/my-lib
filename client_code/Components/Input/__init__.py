from ._anvil_designer import InputTemplate
from anvil import *
import anvil.server

# add value properties for convenience
DatePicker.value = property(lambda self: self.date, lambda self, val: setattr(self, "date", val))
TextBox.value = property(lambda self: self.text, lambda self, val: setattr(self, "text", val))
DropDown.value = property(lambda self: self.drop_down, lambda self, val: setattr(self, "drop_down", val))
TextArea.value = property(lambda self: self.text_area, lambda self, val: setattr(self, "text_area", val))

class Input(InputTemplate):
  def __init__(self, error=None, type="text", key="", format="DD-MM-YYYY", items=[], **properties):
    # Set Form properties and Data Bindings.
    self.init_components(error=error, type=type, key=key, format=format, items=items, **properties)

    self.label.text = key.capitalize()
    self.setup_input()

  def setup_input(self):
    if self.type == "date":
      print(self.format)
      self.input = DatePicker(format=self.format, role='outlined')
      self.input_panel.clear()
      self.input_panel.add_component(self.input, expand=True)
    elif self.type == "drop_down":
      print(self.items)
      self.input = DropDown(items=self.items, role='outlined')
      self.input_panel.clear()
      self.input_panel.add_component(self.input, expand=True)
    elif self.type == "text_area":
      self.input = TextArea(role='outlined')
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
