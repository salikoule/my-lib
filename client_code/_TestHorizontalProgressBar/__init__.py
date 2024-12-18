from ._anvil_designer import _TestHorizontalProgressBarTemplate
from anvil import *
import anvil.server


class _TestHorizontalProgressBar(_TestHorizontalProgressBarTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # self.horizontal_progressbar_1.value = 0.2
    # Any code you write here will run before the form opens.

  def form_show(self, **event_args):
    self.horizontal_progressbar_1.value = 95
