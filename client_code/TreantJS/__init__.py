from ._anvil_designer import TreantJSTemplate
from anvil import *
import anvil.server

from anvil.js.window import Treant
import anvil.js
import json
from ..TreantLib import TreantLib

class TreantJS(TreantJSTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def form_show(self, **event_args):
    #self.canvas.clear()
    # panel = anvil.js.get_dom_node(self.flow_panel)
    # panel.innerHTML = f'<div id="treeSimple" style="width:500px; height: 500px;"> </div>'
    self.flow_panel.add_component(TreantLib())
    simple_chart_config = {}
    simple_chart_config['chart']= {
        'container': '#treeSimple',
        'rootOrientation': 'SOUTH',
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
    data = anvil.server.call('get_tree')
    rows=json.loads(data)
    simple_chart_config['nodeStructure'] = rows
    # simple_chart_config['nodeStructure'] = {
    #     'text': { 'name': "Parent node" },
    #     'children': [
    #         {
    #             'text': { 'name': "First child" }
    #         },
    #         {
    #             'text': { 'name': "Second child" }
    #         }
    #     ]
    # }
    # simple_chart_config = {
    #     'chart': {
    #         'container': "#treeSimple",

    #         'animateOnInit': True,
            
    #         'node': {
    #             'collapsable': True
    #         },
    #         'animation': {
    #             'nodeAnimation': "easeOutBounce",
    #             'nodeSpeed': 700,
    #             'connectorsAnimation': "bounce",
    #             'connectorsSpeed': 700
    #         }
    #     },
    #     'nodeStructure': {
    #         'children': [
    #             {
    #                 'collapsed': True,
    #                 'children': [
    #                     {
    #                         'name': 'Child 1'
    #                     }
    #                 ]
    #             },
    #             {
    #                 #image: "img/sterling.png",
    #                 'childrenDropLevel': 1,
    #                 'children': [
    #                     {
    #                         'name': 'Child '
    #                         #image: "img/woodhouse.png"
    #                     }
    #                 ]
    #             },
    #             {
    #                 'pseudo': True,
    #                 'children': [
    #                     {
    #                         'name': 'Child 3'
    #                         #image: "img/cheryl.png"
    #                     },
    #                     {
    #                         'name': 'Child 4'
    #                         #image: "img/pam.png"
    #                     }
    #                 ]
    #             }
    #         ]
    #     }
    # }
    self.treant = Treant
    self.treant(simple_chart_config)
    
          

