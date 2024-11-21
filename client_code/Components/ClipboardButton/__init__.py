from ._anvil_designer import ClipboardButtonTemplate
from anvil import *
import anvil.server
import anvil.js
from anvil_extras import popover
import time


class ClipboardButton(ClipboardButtonTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.button.popover(content='Copied!', placement='right', trigger='manual')

  @property
  def text(self):
    return self._text
  
  @text.setter
  def text(self, t):
    self._text = t

  def button_click(self, **event_args):
    anvil.js.call("copyclip", self.text)
    self.button.pop("show")
    time.sleep(1)
    self.button.pop("hide")
    
