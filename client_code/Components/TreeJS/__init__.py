from ._anvil_designer import TreeJSTemplate
from anvil import *
import anvil.server

class TreeJS(TreeJSTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def initialize_js_tree(self):
    data = [
                {
                    "text": "Root Node",
                    "children": [
                        {
                            "text": "Child Node 1"
                        },
                        {
                            "text": "Child Node 2"
                        }
                    ]
                }
            ]
    self.call_js('initialize_js_tree', data)

  def form_show(self, **event_args):
    self.initialize_js_tree()
        
    # Add a button to add a new node
    self.add_button = Button(text="Add Node", role="primary")
    self.add_button.set_event_handler("click", self.add_node_to_tree)
    self.add_component(self.add_button)
    

  def node_clicked_callback(self, event, data):
      print(data['node']['text'])
      #alert(f"Node '{data['node']['text']}' was clicked!")

  def add_node_to_tree(self, **event_args):
    print('ok')
    new_node_text = "New Node"
    self.call_js('add_node_to_js_tree', new_node_text)
