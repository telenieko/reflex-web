```python exec
import reflex as rx
from pcweb import constants, styles
from pcweb.pages.docs import api_reference, library
```

# Pages

Pages in Reflex allow you to define components for different URLs. This section covers creating pages, handling URL
arguments, accessing query parameters, managing page metadata, and handling page load events.

## Adding a Page

You can create a page by defining a function that returns a component.
By default, the function name will be used as the route, but you can also specify a route.

```python
def index():
    return rx.text('Root Page')

def about():
    return rx.text('About Page')


def custom():
    return rx.text('Custom Route')

app = rx.App()

app.add_page(index)
app.add_page(about)
app.add_page(custom, route="/custom-route")
```

In this example we create three pages:

- `index` - The root route, available at `/`
- `about` - available at `/about`
- `custom` - available at `/custom-route`

```md alert
# Index is a special exception where it is available at both `/` and `/index`. All other pages are only available at their specified route.
```

## Page Decorator

You can also use the `@rx.page` decorator to add a page.

```python
@rx.page(route='/', title='My Beautiful App')
def index():
    return rx.text('A Beautiful App')
```

This is equivalent to calling `app.add_page` with the same arguments.

```md alert warning
# Remember to import the modules defining your decorated pages.

This is necessary for the pages to be registered with the app.

You can directly import the module or import another module that imports the decorated pages.
```

## Navigating Between Pages

### Links

Links are accessible elements used primarily for navigation. Use the `href` prop to specify the location for the link to navigate to.

```python demo
rx.link("Reflex Home Page.", href="https://reflex.dev")
```

You can also provide local links to other pages in your project without writing the full url.

```python demo
rx.link("Example", href="/docs/library",)
```
Check out the docs [here]({library.typography.link.path}) to learn more.

### Redirect

Redirect the user to a new path within the application using `rx.redirect()`.

- `path`: The destination path or URL to which the user should be redirected.
- `external`: If set to True, the redirection will open in a new tab. Defaults to `False`.

```python demo
rx.vstack(
    rx.button("open in tab", on_click=rx.redirect("/docs/api-reference/special_events")),
    rx.button("open in new tab", on_click=rx.redirect('https://github.com/reflex-dev/reflex/', external=True))
)
```

Redirect can also be run from an event handler in State, meaning logic can be added behind it. It is necessary to `return` the `rx.redirect()`.

```python demo exec
class Redirect2ExampleState(rx.State):
    redirect_to_org: bool = False

    def change_redirect(self):
        self.redirect_to_org = not self.redirect_to_org

    @rx.var
    def url(self) -> str:
        return 'https://github.com/reflex-dev/' if self.redirect_to_org else 'https://github.com/reflex-dev/reflex/'

    def change_page(self):
        return rx.redirect(self.url, external=True)

def redirect_example():
    return rx.vstack(
        rx.text(f"{Redirect2ExampleState.url}"),
        rx.button("Change redirect location", on_click=Redirect2ExampleState.change_redirect),
        rx.button("Redirect to new page in State", on_click=Redirect2ExampleState.change_page),

    )
```




## Nested Routes

Pages can also have nested routes.

```python
@rx.page(route='/nested/page')
def nested_page():
    return rx.text('Nested Page')

app = rx.App()
```

This component will be available at `/nested/page`.

## Getting the Current Page Link

The `router.page.path` attribute allows you to obtain the path of the current page from the router data,
for dynamic pages this will contain the slug rather than the actual value used to load the page.

To get the actual URL displayed in the browser, use `router.page.raw_path`. This
will contain all query parameters and dynamic path segments.

```python
class State(rx.State):
    def some_method(self):
        current_page_route = self.router.page.path
        current_page_url = self.router.page.raw_path
        # ... Your logic here ...
```

In the above example, `current_page_route` will contain the route pattern (e.g., `/posts/[id]`), while `current_page_url`
will contain the actual URL (e.g., `http://example.com/posts/123`).

To get the full URL, access the same attributes with `full_` prefix.

Example:

```python
class State(rx.State):
    @rx.var
    def current_url(self) -> str:
        return self.router.page.full_raw_path
```

In this example, running on `localhost` should display `http://localhost:3000/user/hey/posts/3/`

## Getting Client IP

You can use the `router.session.client_ip` attribute to obtain the IP address of the client associated
with the current state.

```python
class State(rx.State):
    def some_method(self):
        client_ip = self.router.session.client_ip
        # ... Your logic here ...
```
