from ._anvil_designer import _TestTreantTemplate
from anvil import *
import anvil.server

class _TestTreant(_TestTreantTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.first_time = True
    self.node = {
        'text': { 'name': "Parent node" },
        'children': [
            {
                'text': { 'name': "First child" }
            },
            {
                'text': { 'name': "Second child" }
            }
        ]
    }
    self.node = {
      'text': {'name': 'Start'}, 
      'children': [
        {'name': 'Pending', 'children': [{'name': 'Connected', 'children': [{'name': 'Waiting Follow Up Response'}]}, {'name': 'Declined'}]}]}
    self.treant_js_1.node_structure = self.node
    

  def form_show(self, **event_args):
    pass
    #self.treant_js_1.node_structure = self.node

  def button_1_click(self, **event_args):
    self.node['children'].append({'text': { 'name': "Third child" }})
    self.treant_js_1.node_structure = self.node
    #self.form_show()


