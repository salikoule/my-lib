from ._anvil_designer import _TestAgGridTemplate
from anvil import *
import anvil.server

class _TestAgGrid(_TestAgGridTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    
