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
