import anvil.server
from anytree import Node, AnyNode, RenderTree
from anytree.exporter import JsonExporter

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
@anvil.server.callable
def get_tree():
  parent = AnyNode(text = {'name':'Parent'})
  node = AnyNode(text = {'name':'Child 1'}, parent = parent)
  node = AnyNode(text = {'name':'Child 2'}, parent = parent)
  exporter = JsonExporter(sort_keys=True)
  print(RenderTree(parent))
  return exporter.export(parent)

