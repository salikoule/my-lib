from ._anvil_designer import _TestGantChartTemplate
from anvil import *
import anvil.server

class _TestGantChart(_TestGantChartTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
