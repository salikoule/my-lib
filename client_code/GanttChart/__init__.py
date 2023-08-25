from ._anvil_designer import GanttChartTemplate
from anvil import *
from anvil.js.window import Gantt
import anvil.js

class GanttChart(GanttChartTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.events = {'on_click': self.on_click, 'on_date_change': self.on_date_change,'on_progress_change': self.on_progress_change,'on_view_change': self.on_view_change}
    self.tasks = []
    print(dir(anvil.js.window))

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
    try:
      self.refresh()
    except:
      print('error')

  def refresh(self):
    self.gantt.setup_tasks(self.tasks)
    self.gantt.change_view_mode()

  def form_show(self, **event_args):
    self.column_panel_1.clear()
    panel = anvil.js.get_dom_node(self.column_panel_1)
    self.gantt = Gantt(panel, self.tasks, {'view_mode': self.view_mode}, self.events)
    
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

  def button_1_click(self, **event_args):
    self.tasks.append({
				'start': '2018-10-13',
				'end': '2018-10-15',
				'name': 'NOooooo Go Live!',
				'id': "Task 6",
				'progress': 20,
				'dependencies': 'Task 5',
				'custom_class': 'bar-milestone'
			})
    self.gantt.setup_tasks(self.tasks)
    self.gantt.change_view_mode()

    


