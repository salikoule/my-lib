from ._anvil_designer import ContentTemplate
from anvil import *
import anvil.server
from datetime import datetime
import anvil.media
from ....Utils import convert
from anvil_extras import augment

class Content(ContentTemplate):
  def __init__(self, **properties):
    self.sender = None
    self.edit = False
    self.hover = False
    augment.set_event_handler(self, 'hover', self.is_hover)
    self.init_components(**properties)

  def form_show(self, **event_args):
    self.parent_form = self.parent.parent
    self.sender = self.parent_form.sender
    self.recipient = self.parent_form.recipient
    self.update_photo()
    self.format_datetime()
    self.refresh_data_bindings()

  def is_hover(self, **event_args):
    if not self.edit:
      event = event_args['event_type']
      self.hover = True if 'mouseenter' in event else False
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
    self.edit = True
    self.refresh_data_bindings()

  def link_cancel_click(self, **event_args):
    self.edit = False
    self.refresh_data_bindings()

  def link_save_click(self, **event_args):
    self.item['edited'] = True
    self.item['content'] = self.text_area_1.text
    self.link_cancel_click()
    self.parent_form.content_edited_event(self.item)
