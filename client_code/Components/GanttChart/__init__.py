from ._anvil_designer import GanttChartTemplate
from anvil import *
import anvil.server
from anvil.js.window import Gantt
import anvil.js
from ..._TestGanttChart.Form1 import Form1

class GanttChart(GanttChartTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.tasks = self.panel = None
    self.events = {
      'on_click': self.on_click, 
      'on_date_change': self.on_date_change,'on_progress_change': self.on_progress_change,'on_view_change': self.on_view_change, 
      'custom_popup_html':self.custom_popup_html
    }

    self.init_components(**properties)
        # self.tasks = []

  @property
  def view_mode(self):
    return self._view_mode
  
  @view_mode.setter
  def view_mode(self, vm):
    self._view_mode = vm

  @property
  def tasks(self):
    return self._tasks
  
  @tasks.setter
  def tasks(self, t):
    self._tasks = t
    self.build_gantt()
    # try:
    #   self.refresh()
    # except:
    #   print('error')

  def refresh(self):
    self.gantt.setup_tasks(self.tasks)
    self.gantt.change_view_mode()

  def form_show(self, **event_args):
    self.column_panel_1.clear()
    self.panel = anvil.js.get_dom_node(self.column_panel_1)
    self.build_gantt()

  def build_gantt(self):
    if not (self.tasks and self.panel):
      return
    self.gantt = Gantt(self.panel, self.tasks, self.events.update({'view_mode': self.view_mode,'header_height': 50,
    'column_width': 30,}))
    #  {
    # 'header_height': 50,
    # 'column_width': 30,
    # 'step': 24,
    # 'view_modes': ['Quarter Day', 'Half Day', 'Day', 'Week', 'Month'],
    # 'bar_height': 20,
    # 'bar_corner_radius': 3,
    # 'arrow_curve': 5,
    # 'padding': 18,
    # 'view_mode': 'Day',
    # 'date_format': 'YYYY-MM-DD',
    # #'language': 'en', // or 'es', 'it', 'ru', 'ptBr', 'fr', 'tr', 'zh', 'de', 'hu',
    # 'custom_popup_html': None
    # },

  def link_click(self, **event_args):
    self.gantt.change_view_mode(event_args['sender'].tag)

  def on_click(self, task):
    self.raise_event('on_click', task=task)
    

  def on_date_change(self, task, start, end):
    self.raise_event('on_date_change', task=task, start=start, end=end)

  def on_progress_change(self, task, progress):
    self.raise_event('on_progress_change', task=task, progress=progress)

  def on_view_change(self, mode):
    self.raise_event('on_view_change', mode=mode)

  def custom_popup_html(self, task):
    # grid_panel = anvil.js.get_dom_node(Form1())
    # return grid_panel.innerHTML
    return """<div class="details-container">
		  <h5>Custome Task</h5>
		  <p>Expected to finish by 2023</p>
		  <p>80% completed!</p>
		</div>"""

    


