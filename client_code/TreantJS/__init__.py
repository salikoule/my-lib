from ._anvil_designer import TreantJSTemplate
from anvil import *
import anvil.server
from anvil.js.window import Treant
import anvil.js
import json
import uuid

class TreantJS(TreantJSTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.treant = Treant
    self.tree_id = str(uuid.uuid4())

  def form_show(self, **event_args):
    self.flow_panel.clear()
    panel = anvil.js.get_dom_node(self.flow_panel)
    panel.innerHTML = f'<div id="{self.tree_id}" style="width:500px; height: 500px;"> </div>'
    simple_chart_config = {}
    simple_chart_config['chart']= {
        'container': f'#{self.tree_id}',
        'rootOrientation': 'NORTH',
        'nodeAlign':'CENTER',
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
            'type': "step",
            'style': {
                "stroke-width": 2,
                "stroke": "#ccc"
            }
            },
     }

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
    
    self.treant(simple_chart_config)
    
          
  def on_toggle_collapse_finished(self, args):
    print('ok')
    print(args)
