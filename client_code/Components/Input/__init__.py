from ._anvil_designer import InputTemplate
from anvil import *
import anvil.server

# add value properties for convenience
DatePicker.value = property(lambda self: self.date, lambda self, val: setattr(self, "date", val))
TextBox.value = property(lambda self: self.text, lambda self, val: setattr(self, "text", val))
DropDown.value = property(lambda self: self.selected_value, lambda self, val: setattr(self, "drop_down", val))
TextArea.value = property(lambda self: self.text, lambda self, val: setattr(self, "text_area", val))

class Input(InputTemplate):
  def __init__(self, error=None, type="text", key="", **properties):
    # Set Form properties and Data Bindings.
    self.init_components(error=error, type=type, key=key, **properties)
    self.prop = properties['prop']
    self.prerequisites = properties['prerequisites']
    self.label.text = ' '.join(list(k.capitalize() for k in key.split("_")))
    self.setup_input()

  def setup_input(self):
    self.input_panel.clear()
    if self.type == "date":
      self.input = DatePicker(**self.prop)
    elif self.type == "drop_down":
      self.input = DropDown(**self.prop)
    elif self.type == "text_area":
      self.input = TextArea(**self.prop)
    else:
      self.input = TextBox(**self.prop)

    if self.prerequisites:
      self.visible = False

    self.input_panel.add_component(self.input, expand=True)
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

  def refresh(self, **event_args):
    if self.prerequisites:
      key = event_args.get('key', None)
      value = event_args.get('value', None)
      if key in self.prerequisites:
        self.visible = True if value in self.prerequisites[key] else False
        print('---> Refreshed! <---')
