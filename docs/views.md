# Usage in Views

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
