from fasthtml.common import *
from monsterui.all import *

app,rt = fast_app(hdrs=Theme.blue.headers())

@rt
def index():
    return Container("Hello World")

serve()