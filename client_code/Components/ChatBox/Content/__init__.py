from ._anvil_designer import ContentTemplate
from anvil import *
import anvil.server
from datetime import datetime
import anvil.media
from ....Utils import convert

class Content(ContentTemplate):
  def __init__(self, **properties):
    self.sender = None
    self.init_components(**properties)

  def form_show(self, **event_args):
    self.parent_form = self.parent.parent
    self.sender = self.parent_form.sender
    self.recipient = self.parent_form.recipient
    self.update_photo()
    self.format_datetime()
    self.refresh_data_bindings()

  def update_photo(self):
    avatar = '_/theme/avatar.png'
    if self.item.get('user') == 'AI':
      photo = '_/theme/ai-bot.png'
    elif self.sender and self.item.get('user') == self.sender['name']:
      photo = self.sender.get('image', avatar)
    elif self.recipient and self.item.get('user') == self.recipient['name']:
      photo = self.recipient.get('image', avatar)
    else:
      photo = avatar
    self.image_left.source = photo

  def format_datetime(self):
    """Formats the label text to pretty date"""
    # time = self.item['created'].strftime('%d/%m/%Y, %H:%M:%S')
    if self.item.get('created'):
      self.label_datetime.text = convert.datetime_to_pretty(datetime.strptime(self.item['created'], '%Y-%m-%d, %H:%M:%S'))
      self.label_datetime.tooltip = datetime.strptime(self.item['created'], '%Y-%m-%d, %H:%M:%S').strftime('%b %d, %Y %H:%M')

  def link_send_click(self, **event_args):
    yes_clicked = confirm('Are you sure you want to send this message?')
    if yes_clicked:
      self.item['user'] = self.sender['name']
      self.item['created'] = datetime.utcnow().strftime('%Y-%m-%d, %H:%M:%S')
      self.update_photo()
      self.format_datetime()
      self.refresh_data_bindings()

  def link_try_again_click(self, **event_args):
    self.parent_form.try_again_event()

  def link_edit_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass
