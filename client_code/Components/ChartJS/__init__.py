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

  @property
  def options(self):
    return self._options
  
  @options.setter
  def options(self, o: dict):
    self._options = o
    self._config['options'].update(**o)

  @property
  def axis_title(self):
    """Give as input a dictionary with key the axis reference and with value the title text.
        Eg. {'x': 'Axis title'} """
    return self._axis_title
  
  @axis_title.setter
  def axis_title(self, a_t: dict):
    self._axis_title = a_t
    axis, title = list(a_t.items())[0]
    self._config['options']['scales'][axis]['title'] = {'text':title, 'display': True}

  @property
  def axis_stacked(self):
    """Give as input a dictionary with key the axis reference and with value a bool.
        Eg. {'x': True} """
    return self._axis_stacked
  
  @axis_stacked.setter
  def axis_stacked(self, a_s: dict):
    self._axis_stacked = a_s
    axis, stacked = list(a_s.items())[0]
    print(axis, stacked)
    self._config['options']['scales'][axis]['stacked'] = stacked

  @property
  def axis_min(self):
    """Give as input a dictionary with key the axis reference and with value the min value.
        Eg. {'x': 100} """
    return self._axis_min
  
  @axis_min.setter
  def axis_min(self, a_m: dict):
    self._axis_min = a_m
    axis, min_ = list(a_m.items())[0]
    self._config['options']['scales'][axis]['min'] = min_

  @property
  def axis_max(self):
    """Give as input a dictionary with key the axis reference and with value the max value.
        Eg. {'x': 100} """
    return self._axis_max
  
  @axis_max.setter
  def axis_max(self, a_m: dict):
    self._axis_max = a_m
    axis, max_ = list(a_m.items())[0]
    self._config['options']['scales'][axis]['max'] = max_

  @property
  def axis_tick_callback(self):
    """Give as input a dictionary with key the axis reference and with value the callback function.
        Eg. {'x': my_function}"""
    return self._axis_tick_callback
  
  @axis_tick_callback.setter
  def axis_tick_callback(self, atc: dict):
    if atc:
      self._axis_tick_callback = atc
      axis, func = list(atc.items())[0]
      self._config['options']['scales'][axis]['ticks']['callback'] = func

  @property
  def legend(self):
    """Give as input a dictionary that configures the legend
      Eg. {'display': True, 'position': 'right', ...}
    """
    return self._legend
  
  @legend.setter
  def legend(self, l):
    self._legend = l
    self._config['options']['plugins']['legend'] = l

  @property
  def title(self):
    """Give as input a dictionary that configures the title
      Eg. {'display': True, 'text': 'My Tile', 'color': 'red', ...}"""
    return self._title
  
  @title.setter
  def title(self, t):
    self._title = t
    self._config['options']['plugins']['title'] = t

  @property
  def tooltip(self):
    """Give as input a dictionary that configures the tooltip
      Eg. {'intersect': True, 'callbacks': {'label': label_event_func}, ...}
    """
    return self._tooltip
  
  @tooltip.setter
  def tooltip(self, t):
    self._tooltip = t
    self._config['options']['plugins']['tooltip'] = t
    
  def form_show(self, **event_args):
    self.plot_chart()

  def plot_chart(self):
    self.clear()
    canvas = Canvas(height=self.height)
    self.add_component(canvas, full_width_row=True)
    ctx = js.get_dom_node(canvas)
    self.chart = Chart(ctx, self._config)
    canvas.add_event_handler('reset', self.chart_reset)

  def chart_reset(self, **event_args):
    """Render the chart everytime the window sizing is changed."""
    print("rendering....")
    self.chart.render()
