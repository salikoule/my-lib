import anvil.server
import anvil.js

_js_nanoid = anvil.js.import_from("https://cdnjs.cloudflare.com/ajax/libs/nanoid/4.0.2/nanoid.min.js")
_nanoid = _js_nanoid.nanoid


class NANOID(str):
    def __init__(self, val):
        pass

    def __repr__(self):
        return "NANOID('" + self + "')"

def nanoid(num=11):
    """Returns a nanoid of default 11 characters. Argument num is to specify the number of characters to return"""
    return NANOID(_nanoid(num))

if __name__ == "__main__":
    x = nanoid()