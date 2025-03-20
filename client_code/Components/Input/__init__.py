from ._anvil_designer import InputTemplate
from anvil import *
import anvil.server
from anvil_extras.MultiSelectDropDown import MultiSelectDropDown

# add value properties for convenience
DatePicker.value = property(lambda self: self.date, lambda self, val: setattr(self, "date", val))
TextBox.value = property(lambda self: self.text, lambda self, val: setattr(self, "text", val))
DropDown.value = property(lambda self: self.selected_value, lambda self, val: setattr(self, "selected_value", val))
TextArea.value = property(lambda self: self.text, lambda self, val: setattr(self, "text", val))
MultiSelectDropDown.value = property(lambda self: self.selected, lambda self, val: setattr(self, "selected", val))

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
    elif self.type == "multi_drop_down":
      self.input = MultiSelectDropDown(**self.prop)
    elif self.type == "text_area":
      self.input = TextArea(**self.prop)
    else:
      self.input = TextBox(**self.prop)
      self.setup_hide_link()

    if self.prerequisites:
      self.visible = False

    self.input_panel.add_component(self.input, expand=True)
    self.input.add_event_handler("change", self.change)

  def setup_hide_link(self):
    self.link_hide_text.visible = self.prop.get('hide_text', False)
    self.link_hide_text.tag = self.prop.get('hide_text', False)
    self.link_hide_text.tooltip = 'unhide' if self.prop.get('hide_text', False) else None

  @property
  def error(self):
    return self._error

  @error.setter
  def error(self, error):
    self._error = error
    if not error:
      self.error_label.text = None
    else:
      self.error_label.text = "\n".join(error.errors(self.key)) or None
    self.error_label.visible = False if not self.error_label.text or self.error_label.text.strip() == '' else True

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

  def link_hide_text_click(self, **event_args):
    sender = event_args['sender']
    hide_text = not sender.tag
    sender.tag = hide_text
    self.input.hide_text = hide_text
    sender.icon = 'fa:eye' if hide_text else 'fa:eye-slash'
    sender.tooltip = 'unhide' if hide_text else 'hide'
    
