# Usage in Templates

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

## Assignment in Template

You can assing the return value of `var` tag so that you can use it later on
in the template. For instance:

```html
{% var "FOO" as foo_var %}
{% if foo_var > 5 %}
    {# what happens if foo_var is greater than 5 #}
{% endif %}
```

## Conditional Rendering

We've already covered the rendering in some conditions in `var` tag as kwargs.
Those are:

 - `rit`: Renders given value if the `value` of `Variable` is `True`.
 - `rif`: Renders given value if the `value` of `Variable` is `False`.
 - `rin`: Renders given value if the `value` of `Variable` is `None`.
 - `rine`: Renders given value if the `Variable` with given name does not exist.

The usage is:

```
{% var "FOO1" rit="FOO1 is true" %}
{% var "FOO2" rif="FOO2 is false" %}
{% var "FOO3" rin="FOO3 is none" %}

{# you can even combine them #}
{% var "BAR" rit="BAR is true" rif="BAR is false" rin="BAR is none" %}
```

`var` template tag always fails if the `Variable` with given name does not
exist with `Variable.DoesNotExist` exception. You can also define what to render
in case the `Variable` does not exist by defining `rine` parameter.

```
{# assuming FOO does not exist #}
{% var FOO %}
{# fails #}

{% var FOO rine="FOO does not exist." %}
```
