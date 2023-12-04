from ._anvil_designer import ContentTemplate
from anvil import *
import anvil.server
from datetime import datetime
import anvil.media
from ....Utils import convert


class Content(ContentTemplate):
  def __init__(self, **properties):
    self.init_db()
    self.init_defaults()
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
  def init_db(self):
    """Getting and instance of the database"""
    self.db = globals.DB
    
  def init_defaults(self):
    """Initializes the default values of some variables"""
    self.user = self.db.user
    self.gb = globals

  def form_show(self, **event_args):
    self.format_datetime()
    self.refresh_data_bindings()

  def format_datetime(self):
    """Formats the label text to pretty date"""
    time = self.item['created'].strftime('%d/%m/%Y, %H:%M:%S')
    self.label_datetime.text = convert.datetime_to_pretty(datetime.strptime(time, '%d/%m/%Y, %H:%M:%S'))

  def link_1_click(self, **event_args):
    """Downloads the message's attachment"""
    anvil.media.download(self.item['attachment'])
