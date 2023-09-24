from ._anvil_designer import CalendarTemplate
from anvil import *
from anvil.js.window import FullCalendar
import anvil.js

class Calendar(CalendarTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def form_show(self, **event_args):
    self.column_panel.clear()
    calendar = anvil.js.get_dom_node(self.column_panel)
    self.calendar = FullCalendar.Calendar(
      calendar, 
      {
        'initialView': 'multiMonthYear',
        #'initialView': 'dayGridMonth',
        #'initialView': 'resourceTimeGridDay',
        'selectable': True,
        'firstDay':1,
        'dateClick':self.date_click,
        'eventClick':self.event_click,
        'events': [
            { 
              'title': 'The Title', 
              'start': '2023-04-19', 
              'end': '2023-04-19'
            },
          { 
              'title': 'The Event', 
              'allDay': True, 
              'start': '2023-04-20', 
              'end': '2023-04-20'
            },
        ]
      },
    )

    self.calendar.render()
    

  def date_click(self, info):
    print(info)
    info.dayEl.style.backgroundColor = 'red'

  def event_click(self, info):
    print(info.event.title)
    info.el.style.backgroundColor = 'red'

  def button_1_click(self, **event_args):
    self.calendar.addEvent({ 
              'title': 'Ad Hoc', 
              'start': '2023-04-22', 
              'end': '2023-04-22'
            })
