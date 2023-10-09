from ._anvil_designer import Form2Template
from anvil import *
import anvil.server
from anvil.js.window import timepicker

class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    print(dir(w))

    # Any code you write here will run before the form opens.
