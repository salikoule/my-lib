from ._anvil_designer import GanttChartTemplate
from anvil import *
from anvil.js.window import Gantt
import anvil.js

class GanttChart(GanttChartTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.options = {}

    # Any code you write here will run before the form opens.

  def form_show(self, **event_args):
    self.column_panel_1.clear()
    gantt = anvil.js.get_dom_node(self.column_panel_1)
    tasks = [
      {
    	'id': 'Task 1',
    	'name': 'Redesign website',
    	'start': '2016-12-28',
    	'end': '2016-12-31',
    	'progress': 20,
    	'dependencies': 'Task 2, Task 3'
      },
      {
    	'id': 'Task 2',
    	'name': 'New login Page',
    	'start': '2016-12-28',
    	'end': '2016-12-31',
    	'progress': 50,
    	'dependencies': None
      },
      {
    	'id': 'Task 3',
    	'name': 'New theme',
    	'start': '2016-12-28',
    	'end': '2016-12-31',
    	'progress': 80,
    	'dependencies': None
      }
    ]
    self.gantt = Gantt(gantt, tasks,
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
    {'on_click': self.on_click}
                      )
    #self.gantt.on('on_click')

  def link_click(self, **event_args):
    self.gantt.change_view_mode(event_args['sender'].tag)

  def on_click(self, task):
    print(task)
    


