from fasthtml.common import *
from monsterui.all import *

app, rt = fast_app(hdrs=Theme.blue.headers())

@rt
def index():
    return Container(
        H1("Hello, World!"),)

serve()