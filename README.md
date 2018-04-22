# Widget Coding Challenge
## Overview
This repo is for a software demo to show how a RESTful API could be implemented in Python/Django. It was written using Python v3.6 on Windows x64 but it should be platform-agnostic.

## Local Deployment

 1. Install python v3.x for your system (latest is v3.6 as of this document).
 2. Clone this repo (`$ git clone <url> <some_other_optional_name>`)
 3. Create your virtual env (in Windows, run `pip source env/Scripts/activate`).
 4. Download needed packages (`pip install -r requirements.txt`).
 5. Start the application server (`cd widget_challenge; python manage.py runserver`)
 6. Access the API through the browser (`http://localhost:8000/`)
 7. Optional: run unit tests (`python manage.py test`)

The following endpoints are available: `finishes`, `sizes`, `categories`, `widgets`, `orders`, `orderitems`.
 - The `widgets` have names as well as properties defined by `finishes`, `sizes`, `categories` through foreign keys.
 - The `orders` do not have any properties.
 - The `orderitems` have properties defined by `widgets` and `orders` through foreign keys. Both `widgets` and `orders` can have multiple `orderitems`.
