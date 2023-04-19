# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from . import Module1
#
#    Module1.say_hello()
#

import anvil.js
#uuid_module = anvil.js.import_from('https://cdn.jsdelivr.net/npm/nanoid/nanoid.js')
uuid_module = anvil.js.import_from('https://cdnjs.cloudflare.com/ajax/libs/nanoid/4.0.2/nanoid.min.js')

print(dir(uuid_module))
for i in range(100):
  print(uuid_module.nanoid(11))
#print(uuid_module.customAlphabet('1234567890abcdef', 10))