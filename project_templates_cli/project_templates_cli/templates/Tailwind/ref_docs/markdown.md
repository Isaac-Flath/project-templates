To render markdown you can use the `render_md` function that is available in the `render_markdown.py` file in your module by defaults.  Here is an example of it's use:

```python
from .utils import render_md

render_md("# My markdown header\n\n>A quote\n\n**All** markdown works")
```

Keep in mind `render_md` takes in a string so you can read from markdown files to pass that.  This works my rendering markdown to html to markdown using `mistletoe` and then using `apply_classes`.

`apply_classes` lets you give a dictionary of `class:class_string` (e.g. `{'h1':'text-4xl font-bold mt-12 mb-6 gradient-text-primary'}`) to apply those classes to the html provided.  For example:

```python
apply_classes("<h1>hello</h1><b>world<\b>", {'h1':'text-4xl font-bold mt-12 mb-6 gradient-text-primary'})

# Result: <h1 class="text-4xl font-bold mt-12 mb-6 gradient-text-primary">hello</h1><b>world<\b>
```