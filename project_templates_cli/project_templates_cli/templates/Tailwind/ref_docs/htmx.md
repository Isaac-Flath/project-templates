To use HTMX with FastHTML you can pass the attributes to the HTML elements (e.g. `Button("Show", hx_get=my_route, hx_target='#my-target')`).  Key things to keep in mind:

In FastHTML routes stringify to the route path so you can be pythonic instead of passing strings.  For example if we have the following routes:

```python
@rt
def my_route(): return "Hello world"

@rt
def my_second_route(my_arg:str): return my_arg
```

In this example `Button("Show", hx_get=my_route)` would translate to `Button("Show", hx_get='/my_route')`.  

For routes that have query or path parameters we can use the `to` method if it's not passed via a form.  For example, `Button("Show", hx_get=my_second_route.to(my_arg="Goodbye"))` would translate to `Button("Show", hx_get='/my_second_route?my_arg=Goodbye')`.

`@rt` by default exposes routes as both a `GET` and a `POST`, which is almost always what I want.

## File Upload Example

## Cascading DropDown Example

## Infinite Scroll Example

## Simple Todo App Example