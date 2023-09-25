from ._anvil_designer import TreantTemplate
from anvil import *

from anvil.js.window import Treant
import anvil.js

class Treant(TreantTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def form_show(self, **event_args):
    #self.canvas.clear()
    panel = anvil.js.get_dom_node(self.canvas)
    panel.innerHTML = f'<div id="treeSimple" style="width:1300px;"> </div>'
    simple_chart_config = {}
    simple_chart_config['chart']= {
        'container': '#treeSimple',
        'rootOrientation': 'WEST',
        'nodeAlign':'BOTTOM',
        'levelSeparation':    100,
        'siblingSeparation':  20,
        'subTeeSeparation':   20,
        'scrollbar' : 'None',
        'padding':5,
        'animateOnInit':True,
        'animation':{
          'nodeSpeed':1000,
          'connectorsSpeed': 1200
        },
        'connectors': {
            'type': "curve",
            'style': {
                "stroke-width": 2,
                "stroke": "#ccc"
            }
            }}
    simple_chart_config['nodeStructure'] = {
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
    self.treant = Treant
    self.treant(simple_chart_config)

