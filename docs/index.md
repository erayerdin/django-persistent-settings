# Welcome to Django Persistent Settings

Django Persistent Settings is a library to help you store and
retrieve platform-specific settings, in and from the database.

Django Persistent Settings is an alpha product and is subject to
have breaking changes.

## Python and Django Compatibility

Django Persistent Settings currently supports Python 3.6 to 3.7
*and* Django 2.0 to 2.2.

Django Persistent Settings does not target Django 3.x yet and
will provide considerable updates for only 2.x.

## Installation

To install Django Persistent Settings, use `pip`:

```bash
pip install django-persistent-settings
```

Then you need to register it in `INSTALLED_APPS` in your Django settings file:

```python
INSTALLED_APPS = [
    # ... other apps
    "persistent_settings",
]
```

Also, you can *optionally* register `PersistentSettingsMiddleware` in order to
access the settings from a `HttpRequest` instance (inside a view):

```python
MIDDLEWARE = [
    # ... other middlewares
    "persistent_settings.middlewares.PersistentSettingsMiddleware",
]
```

## License

Django Persistent Settings is licensed under the terms of
[Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)
.
