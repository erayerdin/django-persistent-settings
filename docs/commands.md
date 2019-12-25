# Management Commands

There are helper `python manage.py` commands for retrieving, creating, updating
or deleting `Variable` instances.

## Retrieving Variables

`getvar` is a management command to retrieve `Variable` instances.

| Name | Short Name | Value | Description |
|------|------------|-------|-------------|
| name | | | The name of `Variable`. |
| --bash-style | -b | `True` if exists. | Prints out with bash-style starting with 'export'. |

To give some examples:

```bash
python manage.py getvar FOO
# > lorem ipsum

# bash-style
python manage.py getvar FOO -b  # or --bash-style
# > export FOO="lorem ipsum"

# if it does not exist
python manage.py getvar BAR
# > Variable named BAR does not exist.
```

!!! warning
    The `value` of `Variable` instances are stored as bytes in database using
    built-in `pickle` package of Python, which means retrieving them via
    `getvar` will result in showing their `__str__` in terminal. What that means
    is management commands are to be used *only and only* with primitive data
    types. Otherwise, you might get unexpected results.

## Setting Variables

`setvar` is a management command to create or update `Variable` instances.

| Name | Short Name | Choices | Value | Description |
|------|------------|---------|-------|-------------|
| name | | | | The name of `Variable`. |
| value | | | `None` | The value of `Variable`. |
| --type | -t | `str`, `int`, `float`, `bool` | `str` | The type of value. |
| --no-update | -n | | `True` if exists. | The command raises exception if `Variable` exists. |

By default, `setvar` without `value` creates or updates a `Variable` instance
with `None` (`null` in database).

```bash
python manage.py setvar FOO
# this creates a FOO variable with value null in database.
```

You usually would like to define a value:

```bash
python manage.py setvar FOO "lorem ipsum"
# this creates a FOO variable with value "lorem ipsum" in database
```

### Defining Types

There are some cases as below:

```bash
python manage.py setvar BAR 5.5
```

What happens in case of `BAR` variable? Well, whatever you provide as a value,
the value is considered to be `str` type by default, so it will not be `float`.
However, if you desire it to be `float` type, you need to explicitly define it
with `--type` argument:

```bash
python manage.py setvar BAR 5.5 --type float
# this creates a BAR variable with *float* value 5.5 in database
```

It's the same for `int` and `bool` type as well.

### Boolean Type

`bool` type also allows you to use convenient aliases to set to `False`, the
values below results in `False` (case-insensitive):

 - `f`
 - `false`
 - `0`
 - `n`
 - `no`

Any value with `--type bool` other than those above are considered to be `True`.
To give some examples:

```bash
# these will create or update FOO variable with value False as boolean type
python manage.py setvar FOO False --type bool
python manage.py setvar FOO false --type bool
python manage.py setvar FOO f --type bool
python manage.py setvar FOO 0 --type bool
python manage.py setvar FOO No --type bool
python manage.py setvar FOO no --type bool
python manage.py setvar FOO n --type bool

# these will create or update BAR variable with value True as boolean type
python manage.py setvar BAR True --type bool
python manage.py setvar BAR true --type bool
python manage.py setvar BAR t --type bool
python manage.py setvar BAR 1 --type bool
python manage.py setvar BAR Yes --type bool
python manage.py setvar BAR yes --type bool
python manage.py setvar BAR y --type bool
# or any value
python manage.py setvar BAR whatever --type bool  # will result in True
```

### Forcing No Update

The default behavior of `setvar` is to create if `Variable` does not exist, otherwise
update the value. This might not be the desired case for you, so you can use
`--no-update` flag to force raising exception in case `Variable` instance already
exists.

```bash
# will raise CommandError if FOO does not exist
python manage.py setvar FOO "bar" -n  # or --no-update
# > Variable named FOO already exists.
```

## Deleting Variables

`delvar` is a management command to delete `Variable` instances.

| Name | Short Name | Value | Description |
|------|------------|-------|-------------|
| name | | | The name of `Variable`. |
| --no-error | -n | `True` if exists. | The command does not raise any exceptions if `Variable` does not exist. |

To give some examples:

```bash
python manage.py delvar FOO
# Successfully deleted Variable named FOO.

# if it does not exist
python manage.py delvar BAR
# > Variable named BAR does not exist.
# this raises `CommandError`, so exit-code is not zero.
# if this is not the behavior you'd like, then use `--no-error` or `-n`

python manage.py delvar BAR -n  # or --no-error
# > Variable named BAR does not exist.
# returns 0 exit-code
```
