# How to Use

A *single* setting is called *variable* and is defined by `Variable` model in
`persistent_settings.models`.

It extends `django.models.Model`, so you can do standard stuffs with it.
However, Django Persistent Settings also helps you get `Variable`s in different
context.

## Creating A Variable

You can create a `Variable` instance with standard `create` method as below:

```python
from persistent_settings.models import Variable

Variable.objects.create(name="V_INT", value=5)
```

You can provide *any type* of `value`.

```python
v_int = Variable.objects.create(name="V_INT", value=5)
v_float = Variable.objects.create(name="V_FLOAT", value=5.5)
v_bool = Variable.objects.create(name="V_BOOL", value=False)
v_str = Variable.objects.create(name="V_STR", value="lorem")
```

!!! warning
    While it is possible to create a `Variable` with any type, Django
    Persistent Settings uses `pickle` under the hood and it has some
    *limitations* and *considerations*. Please consider checking
    [pickle documentation][pickle_docs] for further information.

!!! note
    A good convention regarding to the warning above is:

     - to use *only* primitive *or* built-in data types and
     - to not serialize a value given by the client before validating it.

[pickle_docs]: https://docs.python.org/3/library/pickle.html

## Retrieving A Variable

You can, again, retrieve a `Variable` instance in a standard fashion.

```python
variable = Variable.objects.get(name="FOO")
# or
variables = Variable.objects.filter(name__startswith="BAR")
```

### Retrieving from HttpRequest

You can retrieve a `Variable` instance from `HttpRequest` instance if you add
`PersistentSettingsMiddleware`[^1] to middlewares. `HttpRequest` instances are
injected in views by Django. If you use a function-based view:

```python
def foo_view(request, *args, **kwargs):
    # `request` is `HttpRequest` instance
    bar = request.persistent_settings["bar"]
    # ...
```

If you use a class-based view:

```python
class FooView(TemplateView):
    template_name = "foo.html"

    # for example, let's assume we need a Variable inside foo.html
    def get_context_data(self, **kwargs):
        # you can get HttpRequest instance with self.request
        kwargs["bar"] = self.request.persistent_settings["bar"]
        return super().get_context_data(**kwargs)
```

!!! tip
    This was only an example. You can already use custom template tags to get
    `Variable`s in templates, discussed in the next section.

[^1]: See [installation](/#installation) section.

### Retrieving in Template

In order to get a variable in a template, you need to first load
`persistent_settings`:

```html
{% load persistent_settings %}
```

You can use `var` tag to get a `Variable`'s value:

```html
{% var "FOO" %}
```

The table below shows which type of value renders how:

| Value | Type | Renders |
|---|---|---|
| 5 | int | "5" |
| 5.5 | float | "5.5" |
| "foo" | str | "foo" |
| True | bool | "True" |
| False | bool | "False |
| None | NoneType | "None" |

#### Assignment in Template

You can assing the return value of `var` tag so that you can use it later on
in the template. For instance:

```html
{% var "FOO" as foo_var %}
{% if foo_var > 5 %}
    {# what happens if foo_var is greater than 5 #}
{% endif %}
```

## Updating A Variable

You can update a single variable:

```python
variable.value = 5
variable.save()
# or
variable.save(update_fields=("value",))
```

Or you can mass update on a `QuerySet`:

```python
variables = Variable.objects.filter(name__startswith="FOO")
variables.update(value=5)
```
