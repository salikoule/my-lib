from ._anvil_designer import AgGridTemplate
from anvil import *
import anvil.server
import anvil.js
import datetime
import json
from anvil.js.window import agGrid
from anvil.js.window import window
import uuid

class AgGrid(AgGridTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
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
                    },
                          'rowModelType': 'serverSide',
                         'serverSideDatasource': {'getRows':self.build_postgresql_query},}
    self.init_components(**properties)
    self.grid_id = str(uuid.uuid4())

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

  def build_postgresql_query(self, params):
    # Initialize the SQL query
    # print(params)
    print('ok')
    query = "SELECT * FROM your_table_name"

    # Pagination
    page_size = params.get("pageSize")
    start_row = params.get("startRow")
    if page_size and start_row is not None:
        query += f" LIMIT {page_size} OFFSET {start_row}"

    # Sorting
    sort_model = params.get("sortModel")
    if sort_model:
        sort_columns = []
        for sort in sort_model:
            col_id = sort["colId"]
            sort_dir = sort["sort"]
            sort_columns.append(f"{col_id} {sort_dir}")
        if sort_columns:
            query += " ORDER BY " + ", ".join(sort_columns)

    # Filtering
    filter_model = params.get("filterModel")
    if filter_model:
        filters = []
        for col_id, filter_values in filter_model.items():
            # Adjust this part based on your filter structure in ag-Grid
            filter_conditions = []
            for filter_val in filter_values:
                filter_conditions.append(f"{col_id} = '{filter_val}'")
            if filter_conditions:
                filters.append("(" + " OR ".join(filter_conditions) + ")")
        if filters:
            query += " WHERE " + " AND ".join(filters)

    # You can also handle grouping if needed
    print(query)
    return query


