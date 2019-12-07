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

### Retrieving in Template

In order to get a variable in a template, you need to first load
`persistent_settings`:

```html
{% load persistent_settings %}
```

You can use `get_var` tag to get a `Variable`'s value:

```html
{% get_var "FOO" %}
```

[^1]: See [installation](/#installation) section.