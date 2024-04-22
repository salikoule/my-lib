from ._anvil_designer import _TestGanttChartTemplate
from anvil import *
import anvil.server
from ..Utils import nanoid
from .Form1 import Form1
import anvil.js

class _TestGanttChart(_TestGanttChartTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    

  def form_show(self, **event_args):
    self.gantt_chart_1.tasks = self.tasks = [
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
				'dependencies': ['Task 4', 'Task 3'],
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
    self.gantt_chart_1.tasks = self.tasks




  






