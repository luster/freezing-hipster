from flask import render_template
from flask import send_from_directory
from app import app
from app.controllers import *

import os

PROJECT_DIR = os.path.dirname(__file__)

@app.route('/')
@app.route('/index')
def index():
    # set top nav bar
    top_nav = [
            "music",
            "tour",
            "shop",
            "contact"
            ]

    # get merch images, sort them, set alt text
    # TODO: put this in a separate controller
    # TODO: merch modeling for store
    merch_img_path = PROJECT_DIR+'/static/img/Assets/Merch'
    paths = './static/img/Assets/Merch/'
    merch = [{
                'href':paths+f,
                'alt': f.replace('_',' ').replace('.jpg','')}
                for f in os.listdir(merch_img_path)]
    merch = sorted(merch, key=lambda k: k['alt'])


    # show dates
    show_controller = ShowDateController()
    show_dates = show_controller.query_shows(4)

    # set context variables
    context = {}
    context['merch'] = merch
    context['top_nav'] = top_nav
    context['show_dates'] = show_dates

    return render_template("index.html", context=context)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
            'favicon.ico', mimetype='image/vnd.microsoft.icon')
