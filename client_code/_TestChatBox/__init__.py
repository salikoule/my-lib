from ._anvil_designer import _TestChatBoxTemplate
from anvil import *
import anvil.server
from datetime import datetime


class _TestChatBox(_TestChatBoxTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    dt = datetime.utcnow().strftime("%Y-%m-%d, %H:%M:%S")
    conversation = [{'user': 'Christopher Harast', 'content': 'Hi Dave I’m hoping to connect with other IT professionals on LinkedIn. I grew my own IT company to $10m before selling it & now help owners double revenue over a 12-24 month period. I have some great guides & a money back guarantee, so if it sounds of interest, it’d be great to connect.', 'created': dt},
                    {'user': 'Christopher Harast', 'content': """Hi Dave, thanks for connecting and to provide some more context to my first message, my name is Chris and I’ve been helping businesses like yours grow for over 35 years. Besides my own IT company, and many others across 85 industries, I recently helped another IT Managed Services company grow from $1.8m to $4m in 2 years.

 If you feel I could provide any value or insights then let’s jump on a call. No pressure and no obligations whatsoever. Would you be open to a short meet and greet some time in the next week""", 'created': dt},
                    {'user': 'Dave', 'content': 'Christopher, I’m open to a conversation with you in early January.', 'created': dt},
                    {'user': 'AI', 'content': 'How about 10th January at 11am?', 'created': dt},
                   ]
    # print(conversation)
    self.chat_box_1.conversation = conversation
    self.chat_box_1.sender = {'name':'Christopher Harast', 'image': """https://www.shutterstock.com/image-photo/happy-puppy-welsh-corgi-14-600nw-2270841247.jpg"""}
    self.chat_box_1.recipient = {'name':'Dave', 'image': """https://t4.ftcdn.net/jpg/00/97/58/97/360_F_97589769_t45CqXyzjz0KXwoBZT9PRaWGHRk5hQqQ.jpg"""}
