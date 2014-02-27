# freezing-hipster

Time King website. Runs on Python/Flask/Postgres.

## Requirements

Postgres & virtualenv-2.7

If you don't have pip:

    sudo easy_install pip

If you don't have virtualenv:

    sudo pip install virtualenv

Create a virtual env called flask in the top-dir of the project:

    virtualenv-2.7 flask

Start the virtual environment:

    source flask/bin/activate

Install requirements with

    pip install requirements.txt

If you're on a Mac, install Postgres (http://postgresapp.com/) and symlink to your virtual environment bin:

    ln -s /Applications/Postgres93.app/Contents/MacOS/bin/pg_config flask/bin/pg_config

## Running
Make sure Postgres is running in the background.

Create the database by opening psql from the Postgres app and running

    CREATE DATABASE tkdb;

Run ./db_create from the top-dir.

While in the top-dir of the project, run

    ./run

Open a web browser and go to http://localhost:5000.
