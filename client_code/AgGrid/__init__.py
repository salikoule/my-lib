from ._anvil_designer import AgGridTemplate
from anvil import *
import anvil.js
import datetime
import json
from anvil.js.window import agGrid
from anvil.js.window import window
import uuid

class AgGrid(AgGridTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self._grid_options = {'defaultColDef': {
                      'flex': 1,
                      'minWidth': 100,
                      'resizable': True,
                      'enableValue': True,
                      'enableRowGroup': True,
                      'filter': True,
                      'filterParams': {
                        'buttons': ['reset', 'apply'],
                        'debounceMs': 200
                          },
                      'sortable':True
                    }}
    self.init_components(**properties)
    self.grid_id = str(uuid.uuid4())
    print('hello')
    print('hello to you too')

  @property
  def height(self):
    return self._height
  
  @height.setter
  def height(self, h):
    self._height = h

  @property
  def theme(self):
    return self._theme
  
  @theme.setter
  def theme(self, t):
    self._theme = t

  @property
  def pagination(self):
    return self._pagination
  
  @pagination.setter
  def pagination(self, p):
    self._pagination = p
    self._grid_options.update({'pagination': p})

  @property
  def pagination_page_size(self):
    return self._pagination_page_size
  
  @pagination_page_size.setter
  def pagination_page_size(self, ppz):
    self._pagination_page_size = ppz
    self._grid_options.update({'paginationPageSize': ppz})

  @property
  def sidebar(self):
    return self._sidebar
  
  @sidebar.setter
  def sidebar(self, s):
    self._sidebar = s
    self._grid_options.update({'sidebar': s})

  @property
  def row_selection(self):
    return self._row_selection
  
  @row_selection.setter
  def row_selection(self, rs):
    self._row_selection = rs
    self._grid_options.update({'rowSelection': rs})
    
  @property
  def grid_options(self):
    return self._grid_options
  
  @grid_options.setter
  def grid_options(self, go={}):
    self._grid_options.update(go)
    
  def form_show(self, **event_args):
    self.flow_panel.clear()
    grid_panel = anvil.js.get_dom_node(self.flow_panel)
    grid_panel.innerHTML = f'<div id="{self.grid_id}" class="{self.theme}" style="height: {self.height}px"></div>'
    ag_grid_id = window.document.getElementById(f"{self.grid_id}")
    self.grid = agGrid.Grid(ag_grid_id, self.grid_options)

