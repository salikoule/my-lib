from ._anvil_designer import ChatBoxTemplate
from anvil import *
import anvil.server
from datetime import datetime

class ChatBox(ChatBoxTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.conversation = []
    self.user = None

  @property
  def db(self):
    return self._db
  
  @db.setter
  def db(self, d):
    self._db = d

  @property
  def user(self):
    return self._user
  
  @user.setter
  def user(self, u):
    self._user = u

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
    if 'content' in self.item:
      created = datetime.utcnow().strftime("%d/%m/%Y, %H:%M:%S")
      self.new_message = {'user': self.user, 'content': self.get_content(), 'created': created}
      if self.chat_panel.items is None:
        #In case is the first comment
        self.chat_panel.items = [self.new_message]
      else:
        #Appends last comment to the repeating panel
        self.chat_panel.items = list(self.chat_panel.items) + [self.new_message]
      self.text_message.content = None
      self.go_to_bottom()
      self.raise_event('x-send_event')
      # self.new_message = globals.get_comments_schema().copy()
      self.refresh_data_bindings()

  def text_message_text_change(self, **event_args):
    self.item['content'] = event_args['sender'].content

  def get_content(self):
    content = ''.join([item['insert'] for item in self.item['content']])
    return content.strip()
