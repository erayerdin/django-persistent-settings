# Basic Usage

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
