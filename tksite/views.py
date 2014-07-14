from django.shortcuts import render

def home(request):
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
    show_controller = BandsInTownController()
    show_dates = show_controller.query_shows()

    # social sprites
    social_sprites_controller = SocialSpritesController()
    social_sprites = social_sprites_controller.get_social_sprites()

    # set context variables
    context = {}
    context['merch'] = merch
    context['top_nav'] = top_nav
    context['show_dates'] = show_dates
    context['social_sprites'] = social_sprites

    return render(request, "2.html", context=context)
