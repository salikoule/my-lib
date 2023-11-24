from ._anvil_designer import _TestChartJSTemplate
from anvil import *
import anvil.server
from .. import Utils
import random
import time
from anvil.js import window

class _TestChartJS(_TestChartJSTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    print(dir(window))

    self.chart_js.labels = [50,60,70,80,90,100,110,120,130,140,150]
    self.chart_js.datasets = [{
      'backgroundColor':"rgba(0,0,255,1.0)",
      'borderColor': "rgba(0,0,255,0.1)",
      'data': [7,8,8,9,9,9,10,11,14,14,15]
    }]

  def form_show(self, **event_args):
    pass

  def button_1_click(self, **event_args):
    for i in range(160, 500, 10):
      self.chart_js.chart.data.labels.append(i)
      # self.chart_js.chart.data.labels.pop(0)
      self.chart_js.chart.data.datasets[0].data.append(random.randint(5, 20))
      # self.chart_js.chart.data.datasets[0].data.pop(0)
      self.chart_js.chart.update()
      time.sleep(1)
    
