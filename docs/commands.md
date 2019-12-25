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
 > python manage.py getvar FOO
lorem ipsum

# bash-style
 > python manage.py getvar FOO -b  # or --bash-style
export FOO="lorem ipsum"

# if it does not exist
 > python manage.py getvar BAR
Variable named BAR does not exist.
```

## Deleting Variables

`delvar` is a management command to delete `Variable` instances.

| Name | Short Name | Value | Description |
|------|------------|-------|-------------|
| name | | | The name of `Variable`. |
| --no-error | -n | `True` if exists. | The command does not raise any exceptions if Variable does not exist. |

To give some examples:

```bash
 > python manage.py delvar FOO
Successfully deleted Variable named FOO.

# if it does not exist
 > python manage.py delvar BAR
Variable named BAR does not exist.
# this raises `CommandError`, so exit-code is not zero.
# if this is not the behavior you'd like, then use `--no-error` or `-n`

 > python manage.py delvar BAR -n  # or --no-error
Variable named BAR does not exist.
# returns 0 exit-code
```
