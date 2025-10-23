from ._anvil_designer import ClipboardButtonTemplate
from anvil import *
import m3.components as m3
import anvil.server
import anvil.js
from anvil_extras import popover
import time


class ClipboardButton(ClipboardButtonTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.copy_link.popover(content='Copied!', placement='right', trigger='manual')

  @property
  def text(self):
    return self._text
  
  @text.setter
  def text(self, t):
    self._text = t

  def copy_link_click(self, **event_args):
      anvil.js.call("copyclip", self.text)
      self.copy_link.pop("show")
      time.sleep(1)
      self.copy_link.pop("hide")
    
