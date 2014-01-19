# freezing-hipster

Time King website. Aggregates and displays data from all of their social networks. Runs on Google App Engine using Python.

## Requirements
    Google App Engine
    PIL (pillow - Python imaging library)

Install PIL with
    sudo pip install PIL
or
    sudo pip install pillow

Install the [Google App Engine SDK](https://developers.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python) for Python, and select `Preferences > Make Symlinks`.

## Installation
    git clone https://github.com/luster/freezing-hipster.git
    cd freezing-hipster

Rename `conf/apis_example.json` to conf/apis.json and remove the first line/fill in your developer keys.
Rename `conf/site-conf_example.json` to `conf/site-conf.json` and remove the first line/fill in your developer URL and URI.

## Running
While in the top project directory, run

    dev_appserver.py .

Open a web browser and go to http://localhost:8080 to view the main page, and go to http://localhost:8000 to view the GAE admin page.
