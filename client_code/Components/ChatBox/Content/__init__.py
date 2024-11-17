from ._anvil_designer import ContentTemplate
from anvil import *
import anvil.server
from datetime import datetime
import anvil.media
from ....Utils import convert

class Content(ContentTemplate):
  def __init__(self, **properties):
    self.user = None
    self.init_components(**properties)

  def form_show(self, **event_args):
    self.user = self.parent.parent.user
    self.format_datetime()
    self.refresh_data_bindings()

  def format_datetime(self):
    """Formats the label text to pretty date"""
    # time = self.item['created'].strftime('%d/%m/%Y, %H:%M:%S')
    self.label_datetime.text = convert.datetime_to_pretty(datetime.strptime(self.item['created'], '%d/%m/%Y, %H:%M:%S'))
