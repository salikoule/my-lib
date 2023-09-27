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

  @property
  def height(self):
    return self._height
  
  @height.setter
  def height(self, h):
    self._height = h

  @property
  def width(self):
    return self._width
  
  @width.setter
  def width(self, w):
    self._width = w

  @property
  def root_orientation(self):
    return self._root_orientation
  
  @root_orientation.setter
  def root_orientation(self, ro):
    self._root_orientation = ro

  @property
  def node_align(self):
    return self._node_align
  
  @node_align.setter
  def node_align(self, na):
    self._node_align = na

  @property
  def connectors(self):
    return self._connectors
  
  @connectors.setter
  def connectors(self, c):
    self._connectors = c

  def form_show(self, **event_args):
    self.flow_panel.clear()
    panel = anvil.js.get_dom_node(self.flow_panel)
    panel.innerHTML = f'<div id="{self.tree_id}" style="width:{self.width}px; height: {self.height}px;"> </div>'
    simple_chart_config = {}
    simple_chart_config['chart']= {
        'container': f'#{self.tree_id}',
        'rootOrientation': self.root_orientation,
        'nodeAlign': self.node_align,
        'levelSeparation':    100,
        'siblingSeparation':  20,
        'subTeeSeparation':   20,
        'scrollbar' : self.scrollbar,
        'padding':5,
        'animateOnInit':True,
        'animation':{
          'nodeSpeed':1000,
          'connectorsSpeed': 1200
        },
        'connectors': {
            'type': self.connectors,
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
