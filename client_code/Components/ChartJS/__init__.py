from ._anvil_designer import ChartJSTemplate
from anvil import *
import anvil.server
from anvil.js.window import Chart
from ... import Components
import copy

class ChartJS(ChartJSTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self._config = copy.deepcopy(Components.CHART_BASIC_CONFIG)
    self.init_components(**properties)

  @property
  def labels(self):
    return self._labels
  
  @labels.setter
  def labels(self, l):
    self._labels = l
    self._config['data']['labels'] = l

  @property
  def datasets(self):
    return self._datasets
  
  @datasets.setter
  def datasets(self, d):
    self._datasets = d
    self._config['data']['datasets'] = d

  @property
  def type(self):
    return self._type
  
  @type.setter
  def type(self, t):
    self._type = t
    self._config['type'] = t

  @property
  def height(self):
    return self._height
  
  @height.setter
  def height(self, h):
    self._height = h

  def form_show(self, **event_args):
    self.clear()
    canvas = Canvas(height=self.height)
    self.add_component(canvas, full_width_row=True)
    ctx = js.get_dom_node(canvas)
    self.chart = Chart(ctx, self._config)
    canvas.add_event_handler('reset', self.chart_reset)
    # print(dir(self.chart))

  def chart_reset(self, **event_args):
    """Render the chart everytime the window sizing is changed."""
    print("rendering....")
    self.chart.render()
