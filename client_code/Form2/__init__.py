from ._anvil_designer import Form2Template
from anvil import *
import anvil.server

class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.demo = anvil.server.call('get_interface')

  def form_show(self, **event_args):
    self.demo.launch()
    
