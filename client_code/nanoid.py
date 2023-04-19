import anvil.js
#nanoid_module = anvil.js.import_from('https://cdn.jsdelivr.net/npm/nanoid/nanoid.js')
nanoid_module = anvil.js.import_from('https://cdnjs.cloudflare.com/ajax/libs/nanoid/4.0.2/nanoid.min.js')

def nanoid(num=11):
  """Returns a nanoid of default 11 characters. Argument num is to specify the number of characters to return"""
  return nanoid_module.nanoid(num)