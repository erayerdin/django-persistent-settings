# Roadmap

Django Persistent Settings is still an alpha product, thus it will have many
changes. This section will discuss what will be added, changed or removed.

## To Be Added

### Overriding Some Methods in Manager

`Variable` model actually has a field called `value_binary` typed `BinaryField`.
All values are stored as bytes in the database. However, a *property* called
`value` is provided to deserialize `value_binary`. While you can access `value`
on a `Variable` instance, it would be also convenient to override some default
manager methods to use `value`.

`value` is already used in the methods below:

 - `create`

`value` will be used in the methods below:

 - `update`
 - `filter`

### New Kwargs to `get_var` Template Tag

While `get_var` template tag renders the value of a `Variable` successfully,
there are some native types which are to be rendered differently based on their
value. For example, a bool `True` renders `"True"` in template, which, most of
the time, is not a desired behavior. Thus, new kwargs to be added to `get_var`,
some of which are:

 - `rit` stands for *render if `True`*, defaults to `"True"`.
 - `rif` stands for *render if `False`*, defaults to `"False"`.
 - `rin` stands for *render if `None`*, defaults to an empty string.

In far future, maybe those below can be considered:

 - `rgt` stands for *render if greater than x*.
 - `rlt` stands for *render if less than x*.

### User-Specific Settings

While platform-wide settings are good enough, it would be even greater to make
these settings user-specific, letting each user to set the settings to their
own choice.
