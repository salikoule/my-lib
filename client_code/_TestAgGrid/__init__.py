from ._anvil_designer import _TestAgGridTemplate
from anvil import *
import anvil.server

class _TestAgGrid(_TestAgGridTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass


    
