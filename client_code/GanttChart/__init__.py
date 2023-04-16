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
				'start': '2018-10-01',
				'end': '2018-10-08',
				'name': 'Redesign website',
				'id': "Task 0",
				'progress': 20
			},
			{
				'start': '2018-10-03',
				'end': '2018-10-06',
				'name': 'Write new content',
				'id': "Task 1",
				'progress': 5,
				'dependencies': 'Task 0'
			},
			{
				'start': '2018-10-04',
				'end': '2018-10-08',
				'name': 'Apply new styles',
				'id': "Task 2",
				'progress': 10,
				'dependencies': 'Task 1'
			},
			{
				'start': '2018-10-08',
				'end': '2018-10-09',
				'name': 'Review',
				'id': "Task 3",
				'progress': 5,
				'dependencies': 'Task 2'
			},
			{
				'start': '2018-10-08',
				'end': '2018-10-10',
				'name': 'Deploy',
				'id': "Task 4",
				'progress': 0,
				'dependencies': 'Task 2'
			},
			{
				'start': '2018-10-11',
				'end': '2018-10-11',
				'name': 'Go Live!',
				'id': "Task 5",
				'progress': 0,
				'dependencies': 'Task 4',
				'custom_class': 'bar-milestone'
			},
			# {
			# 	'start': '2014-01-05',
			# 	'end': '2019-10-12',
			# 	'name': 'Long term task',
			# 	'id': "Task 6",
			# 	'progress': 0
			# }
		]
    #print(dir(Gantt))
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
    {'on_click': self.on_click, 'on_date_change': self.on_date_change,'on_progress_change': self.on_progress_change,'on_view_change': self.on_view_change,}
                      )
    #self.gantt.on('on_click')
    #print(dict(self.gantt))

  def link_click(self, **event_args):
    self.gantt.change_view_mode(event_args['sender'].tag)

  def on_click(self, task):
    print(task)

  def on_date_change(self, task, start, end):
    print(task, start, end)

  def on_progress_change(self, task, progress):
    print(task, progress)

  def on_view_change(self, mode):
    print(mode)
    


