from ._anvil_designer import ChatBoxTemplate
from anvil import *
import m3.components as m3
import anvil.server
from datetime import datetime

class ChatBox(ChatBoxTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.conversation = []
    self.sender = None
    self.recipient = None

  @property
  def db(self):
    return self._db
  
  @db.setter
  def db(self, d):
    self._db = d

  @property
  def sender(self):
    return self._sender
  
  @sender.setter
  def sender(self, s):
    self._sender = s

  @property
  def recipient(self):
    return self._recipient
  
  @recipient.setter
  def recipient(self, r):
    self._recipient = r

  @property
  def conversation(self):
    return self._conversation
  
  @conversation.setter
  def conversation(self, c):
    self._conversation = c if c else []

  def form_show(self, **event_args):
    self.chat_panel.items = self.conversation
    self.go_to_bottom()
  
  def go_to_bottom(self):
    """Moves the scroll to the last element of the repeating panel"""
    chat_area = anvil.js.get_dom_node(self.chat_panel)
    chat_area.scrollTop = chat_area.scrollHeight

  def text_message_change(self, **event_args):
    """This method is called when the text in this text area is edited"""
    pass

  def button_send_click(self, **event_args):
    """Adds the content of the quil to repeating_panel, database and sends email"""
    content = self.text_message.text
    if content and content.strip() != '':
      self.raise_event('send_button_click', content=content)

  def text_message_text_change(self, **event_args):
    self.item['content'] = event_args['sender'].content

  def get_content(self):
    content = ''.join([item['insert'] for item in self.item['content']])
    return content.strip()

  def try_again_event(self):
    self.raise_event('try_again')

  def content_edited_event(self, item):
    self.raise_event('edited', item = item)

  def approved_message_event(self):
    self.raise_event('approved_message')    

  def delete_message(self, item):
    self.raise_event('delete_message', item = item)    

  def ai_switch_change(self, **event_args):
    self.raise_event('ai_switch_change') 
