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
  def legend_display(self):
    """Select with True or Flase if the legent will be displayed"""
    return self._legend
  
  @legend_display.setter
  def legend_display(self, l_d):
    self._legend_display = l_d
    self._config['options']['plugins']['legend']['display'] = l_d

  @property
  def legend_position(self):
    """Select the position of the legend will be displayed"""
    return self._legend_position
  
  @legend_position.setter
  def legend_position(self, l_p):
    self._legend_position = l_p
    self._config['options']['plugins']['legend']['position'] = l_p

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
