from ._anvil_designer import Form2Template
from anvil import *
import anvil.server

_js_timepicker = anvil.js.import_from("//cdnjs.cloudflare.com/ajax/libs/timepicker/1.3.5/jquery.timepicker.min.js")

class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    print(dir(_js_timepicker))

    # Any code you write here will run before the form opens.

  def form_show(self, **event_args):
    self.column_panel.clear()
    panel = anvil.js.get_dom_node(self.column_panel)
    self.timepicker = _js_timepicker.timepicker(panel)
    

