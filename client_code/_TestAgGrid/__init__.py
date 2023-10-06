from ._anvil_designer import _TestAgGridTemplate
from anvil import *
import anvil.server

class _TestAgGrid(_TestAgGridTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.col_defs = [
        { 'field': "make" },
        { 'field': "model" },
        { 'field': "price" }
                    ]
    row_data = [
      { 'make': "Toyota", 'model': "Celica", 'price': 35000 },
      { 'make': "Ford", 'model': "Mondeo", 'price': 32000 },
      { 'make': "Porsche", 'model': "Boxster", 'price': 72000 }
    ]
    grid_options = {'columnDefs': self.col_defs,
                                  'rowData': row_data,
                                  #'onCellClicked': self.on_cell_clicked,
                                  #'onRowSelected': self.on_row_selected,
                                 }
    self.ag_grid_1.grid_options = grid_options



    
