from ._anvil_designer import TimePickerTemplate
from anvil import *

class TimePicker(TimePickerTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.set_color(self.default_color)
    self.time_input.text = self.time
    
  @property
  def hour(self):
    return self._hour
  
  @hour.setter
  def hour(self, h):
    self._hour = h

  @property
  def minutes(self):
    return self._minutes
  
  @minutes.setter
  def minutes(self, m):
    self._minutes = m
    
  @property
  def time(self):
    if self._hour < 10:
      result = "0"+str(self._hour)
    else:
      result = str(self._hour)
      
    result += ":"
    
    if self._minutes < 10:
      result += "0"+str(self._minutes)
    else:
      result += str(self._minutes)
      
    return result

  @time.setter
  def time(self, t):
    self.time_input.text = t
    self.time_input_change()
    
  def set_color(self, c):
    if self.use_background_for_error:
      self.time_input.background = c
    else:
      self.time_input.foreground = c
  
  def is_valid(self, text=None):
    valid = True
    
    if not text:
      text = self.time_input.text
    
    num_colons = text.count(':')
    length = len(text)
    
    if num_colons > 1:
      valid = False
      
    elif length > 5:
      valid = False
      
    elif not text.replace(':', '').isdigit():
      valid = False
      
    elif num_colons == 0 and length > 2:
      valid = False
      
    else:      
      tokens = text.split(':')
      
      if tokens[0]:
        hour = int(tokens[0])
        
        if hour < 0 or hour > 23:
          valid = False
        else:
          self._hour = hour
          
      if num_colons == 1 and tokens[1]:
        minutes = int(tokens[1])
        
        if minutes < 0 or minutes > 59:
          valid = False
        else:
          self._minutes = minutes
      
    if not valid:
      self.set_color(self.error_color)
    else:
      self.set_color(self.default_color)
        
    return valid
  
  def time_input_change(self, **event_args):
    self.is_valid()
    self.raise_event('change')

  def time_input_pressed_enter(self, **event_args):
    self.time_input.text = self.time
    self.is_valid()
    self.raise_event('pressed_enter')

  def time_input_lost_focus(self, **event_args):
    self.time_input.text = self.time
    self.is_valid()
    self.raise_event('lost_focus')

  def form_show(self, **event_args):
    self.time_input.text = self.time