import anvil.server

BASIC_GRID_OPTIONS = {'defaultColDef': {
                      'flex': 1,
                      'minWidth': 100,
                      'resizable': True,
                      'enableValue': True,
                      'enableRowGroup': True,
                      # 'editable': True,
                      'filter': True,
                      'filterParams': {
                        'buttons': ['reset', 'apply'],
                        'debounceMs': 200
                          },
                      'sortable':True,
                      
                    },
                         #  'rowModelType': 'serverSide',
                         # 'serverSideDatasource': {'getRows':self.build_postgresql_query},
                         #  'serverSideStoreType': '',
                          # 'getServerSideDatasource':self.build_postgresql_query
                         # 'onSortChanged': self.on_sort_change,
                         }

CHART_BASIC_CONFIG = {
  'type': None,
  'data': {
      'labels': None,
      'datasets': None
    },
  'options': {
    'indexAxis': 'x',
    'elements': {
      'bar': {
        'borderWidth': 0,
      }
    },
    'responsive': False,
    'plugins': {
      'legend': {
        'display': True,
        'position': 'right',
      },
      'title': {
        'display': True,
        'text': ''
      },
      'tooltip':{
         'callbacks': {
         }
      }
    },
    'scales': {
      'y':{
         'reverse':False,
         'position': 'left',
          'title':{
            'display': False,
            'text': None
          },
         'grid': {
            'display': False
          },
        'ticks':{
          'callbacks':{}
        }
      },
      'x':{
        'reverse':False,
        'position': 'left',
        'title':{
            'display': False,
            'text':None
          },
         'grid': {
            'display': False
          },
        'ticks':{
          'callbacks':{}
        }
      },
    }
  },
}
