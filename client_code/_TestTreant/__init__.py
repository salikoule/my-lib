from ._anvil_designer import _TestTreantTemplate
from anvil import *
import anvil.server

class _TestTreant(_TestTreantTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
