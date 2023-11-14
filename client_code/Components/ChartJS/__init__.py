from ._anvil_designer import ChartJSTemplate
from anvil import *
import anvil.server
from anvil.js.window import Chart

class ChartJS(ChartJSTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @property
  def labels(self):
    return self._labels
  
  @labels.setter
  def labels(self, l):
    self._labels = l

  @property
  def data(self):
    return self._data
  
  @data.setter
  def data(self, d):
    self._data = d

  @property
  def type(self):
    return self._type
  
  @type.setter
  def type(self, t):
    self._type = t

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
    Chart(ctx, config)
