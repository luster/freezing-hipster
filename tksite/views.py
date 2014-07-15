from django.shortcuts import render

from controllers import *

import os

PROJECT_DIR = os.path.join(os.path.dirname(__file__), '..')

def home(request):
    # set top nav bar
    top_nav = [
            "music",
            "tour",
            "shop",
            "contact"
            ]

    # get merch images, sort them, set alt text
    mc = MerchController(PROJECT_DIR)
    merch = mc.get_merch()

    # show dates
    sc = BandsInTownController()
    show_dates = sc.query_shows()

    # social sprites
    ssc = SocialSpritesController()
    social_sprites = ssc.get_social_sprites()

    # set context variables
    context = {}
    context['merch'] = merch
    context['top_nav'] = top_nav
    context['show_dates'] = show_dates
    context['social_sprites'] = social_sprites

    return render(request, "index.html", context)
