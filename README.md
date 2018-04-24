# Widget Coding Challenge
## Overview
This repo is for a software demo to show how a Single Page Application web portal accessing a RESTful API could be implemented in Python/Django and AngularJS. It was written using Python v3.6 on Windows x64 but it should be platform-agnostic.

## Web Portal

Once the software is installed and the Django application server is running, the portal can be accessed through `http://localhost:8000/static/index.html#!/home`.

## Local Deployment

 1. Install python v3.x for your system (latest is v3.6 as of this document).
 2. Clone this repo (`$ git clone <url> <some_other_optional_name>`)
 3. Create your virtual env (in Windows, run `$ pip source env/Scripts/activate`).
 4. Download needed packages (`$ pip install -r requirements.txt`).
 5. Create the test database instance (`$ python manage.py makemigrations; python manage.py migrate`)
 5. Start the application server (`$ cd widget_challenge; python manage.py runserver`)
 6. Access the API through the browser (`http://localhost:8000/`)
 7. Optional: run unit tests (`$ python manage.py test`)

The following endpoints are available: `finishes`, `sizes`, `categories`, `widgets`, `orders`, `orderitems`.
 - The `widgets` have names as well as properties defined by `finishes`, `sizes`, `categories` through foreign keys.
 - The `orders` do not have any properties.
 - The `orderitems` have properties defined by `widgets` and `orders` through foreign keys. Both `widgets` and `orders` can have multiple `orderitems`.
 
## Project layout
 - The python API resides in the `/widget_challenge/api` directory.
 - The AngularJS SPA resides in the `/widget_challenge/static` directory.

## Release Notes
 - For the purposes of this exercise, the `SECRET_KEY` and `DEBUG` values in `widget_challenge/settings.py` have been left as is. The key value would not be included in a open repository in actual production software, and `DEBUG` would be set to `False`.
 - The API is currently not able to return children of parent endpoints (e.g. `/finishes/1/widgets`). For this iteration, the visualization of these item collections will be handled by the front end.
 - Queryset implementation in the views could be refactored to be made more concise.
 - The REST API and SPA codebases can be deployed separately, but they were both included in the same project for simplicity of deployment. 
 - The hostname/IP address and port for the REST endpoints used by the SPA is currently set to `localhost:8000` and is stored in `widget_challenge/static/js/env.js`. This application, as currently configured, will function properly when installed and used from the same computer.
 - A flash message needs to be added to let users know an action has taken place/error has been triggered.
 - A confirmation message is needed when an item is about to be deleted. 
