from ._anvil_designer import DemoChartJSTemplate
from anvil import *
import anvil.server
from .. import Utils
import random
import time
from ..Components.ChartJS import ChartJS
from anvil_extras.Tabs import Tabs

class DemoChartJS(DemoChartJSTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.chart_js_bar.labels = [50,60,70,80,90,100,110,120,130,140,150]
    self.chart_js_bar.datasets = [
            {
              'fill': {
                'target': 'origin',
                'above': 'rgb(255, 0, 0)',
                'below': 'rgb(0, 0, 255)' 
              }
            }
        ]


  def form_show(self, **event_args):
    pass
