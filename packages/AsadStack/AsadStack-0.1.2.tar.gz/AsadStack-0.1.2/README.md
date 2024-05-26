# AsadStack: Python Web Framework

![purpose](https://img.shields.io/badge/purpose-learning-green.svg?style=flat-square)
![license](https://img.shields.io/badge/license-MIT-green.svg?style=flat-square)
![PyPI - Version](https://img.shields.io/pypi/v/AsadStack)


## Description

AsadStack is a Python Web Framework

It's a WSGI framework and can be used with any WSGI application server such as Gunicorn.

## Installation

```shell
pip install AsadStack
```

## How to use it

### Basic Usage

```python
from Asad_Stack.app import AsadStackApp
app = AsadStackApp()

@app.route("/home", allowed_methods=["get"])
def home(request, response):
    response.text = "That is home page"


@app.route("/about", allowed_methods=["put"])
def about(request, response):
    response.text = "That is about page"


@app.route("/hello/{name}")
def greeting(request, response, name):
    response.text = f"Hello {name}"


@app.route("/books")
class Books:
    def get(self, request, response):
        response.text = "That is books page"

    def post(self, request, response):
        response.text = "That is books post page"


def new_handler(request, response):
    response.text = "That is new handler"


@app.route("/template")
def template_handler(request, response):
    response.html = app.template(
        "home.html",
        context={"new_title": "Best Title", "new_body": "Best Body Asadbek"}
    )

@app.route("/json")
def json_handler(req, resp):
    response_data = {"name": "Asadbek", "type": "json"}
    resp.json = response_data
```

### Unit Tests

The recommended way of writing unit tests is with [pytest](https://docs.pytest.org/en/latest/).
There are two built in fixtures
that you may want to use when writing unit tests with AsadStack.
The first one is `app` which is an instance of `AsadStackApp`.

```python
def test_route_overlap_throws_exception(app):
    @app.route("/")
    def home(req, resp):
        resp.text = "That is home page"

    with pytest.raises(AssertionError):
        app.route("/")
        def home2(req, resp):
            resp.text = "That is home2 page"
```

The other one is `test_client` that you can use to sen HTTP requests to your
handlers.It is based on the famous [requests]("https://requests.readthedocs.io/") and 
it should feel very familiar:

```python
def test_parameterized_route(app, test_client):
    @app.route("/hello/{name}")
    def greeting(req, resp, name):
        resp.text = f"Hello {name}"
        
    assert test_client.get("http://testserver/hello/Asadtopchik").text == "Hello Asadtopchik"

```

## Templates

The default folder for templates is `templates`. You can change it when 
initializing the main `AsadStackApp()` class:

```python
app = AsadStackApp(template_dir="template_dir_name")
```

Then you can use HTML files in that folder like so in a handler:

```python

@app.route("/template")
def template_handler(request, response):
    response.html = app.template(
        "home.html",
        context={"new_title": "Best Title", "new_body": "Best Body Asadbek"}
    )
```

## Static Files

You can use `static` folder in your project to serve static files.

```python
app = AsadStackApp(static_dir="static")
```

Then you can use HTML files in that folder like so in a handler:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{new_title}}</title>
    <link rel="stylesheet" href="/static/home.css">
</head>
<body>
<h1>{{new_body}}</h1>
<p>This a paragraph</p>
</body>
</html>
```

### Middleware

You can create custom middleware by extending the `Middleware` class.

```python
from Asad_Stack.middleware import Middleware
from Asad_Stack.app import AsadStackApp

app = AsadStackApp()

class MyMiddleware(Middleware):
    def process_request(self, req):
        print("request is being called", req.url)
        
    def process_response(self, req, resp):
        print("response has been generated", resp.url)


app.add_middleware(MyMiddleware)
```