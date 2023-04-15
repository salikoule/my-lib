from ._anvil_designer import Form1Template
from anvil import *

import anvil.js

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    uuid_module = require(anvil.js.import_from('https://cdnjs.cloudflare.com/ajax/libs/shortid/2.2.16/generate.min.js'))
    #self.gantt_chart_1.add_tasks()
    # self.gantt_chart_1.add_event_handler('x-on_click', self.on_click)
    

  # def on_click(self, **event_args):
  #   print('->', event_args)

  # def form_show(self, **event_args):
  #   self.gantt_chart_1.add_event_handler('x-on_click', self.on_click)

  def gantt_chart_1_on_click(self, **event_args):
    print(event_args['sender'])

