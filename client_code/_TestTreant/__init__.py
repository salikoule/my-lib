from ._anvil_designer import _TestTreantTemplate
from anvil import *
import anvil.server

class _TestTreant(_TestTreantTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.first_time = True
    btn = Button(text='Click me!', role='filled-button')
    panel = ColumnPanel()
    btn.set_event_handler('click', self.btn_click)
    panel.add_component(btn)
    self.node = {
        'text': { 'name': "Parent node" },
        'innerHTML': anvil.js.get_dom_node(panel).innerHTML,
        'children': [
            {
                'text': { 'name': "First child" }
            },
            {
                'text': { 'name': "Second child" }
            }
        ]
    }
    self.treant_js_1.node_structure = self.node
    

  def form_show(self, **event_args):
    pass
    #self.treant_js_1.node_structure = self.node

  def btn_click(self, **event_args):
    print('ok')
    alert('Hello')

  def button_1_click(self, **event_args):
    self.node['children'].append({'text': { 'name': "Third child" }})
    self.treant_js_1.node_structure = self.node
    #self.form_show()


