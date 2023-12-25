from ._anvil_designer import _TestTreantTemplate
from anvil import *
import anvil.server
from functools import partial
from anvil.js.window import window

class _TestTreant(_TestTreantTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.first_time = True
    lbl = Label(text='Click', foreground='grey', role='body')
    btn = Link(icon='fa:repeat', role='body')
    # btn_node = anvil.js.get_dom_node(btn)
    # btn_node.addEventListener('click', self.btn_click)
    # panel = FlowPanel(spacing='none', align='left', vertical_align='top')
    panel = ColumnPanel(wrap_on='never', col_spacing=None)
    # btn.set_event_handler('click', self.btn_click)
    panel.add_component(lbl)
    panel.add_component(btn)
    # print(anvil.js.get_dom_node(panel).innerHTML)
    self.node = {
        'text': { 'name': "Parent node"},
        'innerHTML': anvil.js.get_dom_node(panel).innerHTML,
        'HTMLid':1,
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
    comp = window.document.getElementById(1)
    # comp = window.document.getElementsByClassName('anvil-component-icon left fa fa-repeat left-icon')
    # print(comp)
    # print(dict(comp['data']['treenode']))
    # print(comp['data']['treenode'])
    comp.addEventListener('click', self.btn_click)

  def btn_click(self, event):
    alert('Hello')

  def button_1_click(self, **event_args):
    self.node['children'].append({'text': { 'name': "Third child" }})
    self.treant_js_1.node_structure = self.node
    #self.form_show()


