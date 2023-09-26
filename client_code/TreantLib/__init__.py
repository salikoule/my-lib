from ._anvil_designer import TreantLibTemplate
from anvil import *
import anvil.server

class TreantLib(TreantLibTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
