screen gallery(current_page=1):
    tag menu
    use game_menu(_("Gallery")):
        $ gallery_pages = (len(galleries)-1)//6+1
        $ last_num_scenes = len(galleries) % 6
        fixed:
            button:
                style_prefix "page_label"
                xalign 0.5
                text "Page [current_page]"

            grid 3 2:
                style_prefix "slot"
                xalign 0.5
                yalign 0.5
                spacing gui.slot_spacing

                $ first_scene = (current_page-1) * 6
                if current_page < gallery_pages or last_num_scenes == 0:
                    for i in range(first_scene,first_scene+6):
                        button:
                            if renpy.seen_label(galleries[i]):
                                action Replay(galleries[i])
                            add galleries[i]:
                                if not renpy.seen_label(galleries[i]):
                                    blur 20.0
                else:
                    for i in range(first_scene,first_scene+last_num_scenes):
                        button:
                            if renpy.seen_label(galleries[i]):
                                action Replay(galleries[i])
                            add galleries[i]:
                                if not renpy.seen_label(galleries[i]):
                                    blur 20.0
                    for i in range(6-last_num_scenes):
                        button:
                            null
            hbox:
                style_prefix "page"
                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                for show_page in range(1, gallery_pages+1):
                    textbutton "[show_page]" action ShowMenu("gallery", current_page=show_page, _transition=Dissolve(0.0))

define galleries = [
    "gal_prologueviosex",    "gal_c2viopublicsex",    "gal_c2ritadream1",
    "gal_c2ritadream2",      "gal_c2ritadream3",      "gal_c3viosex",
    "gal_c4viosex",          "gal_c5ritalocker",      "gal_c5ritapizza",
    "gal_c5viogroup1",       "gal_c5viogroup2",       "gal_c5viogroup3",
    "gal_c5viosex",          "gal_c6ritapool",        "gal_c6ritatheater",
    "gal_c6ritafj",          "gal_c7ritabjconnor",    "gal_c7ritalocker",
    "gal_c7ritabjpool",      "gal_c7viogroup1",       "gal_c7viogroup2",
    "gal_c8ritajosh",        "gal_c8ritapizza",       "gal_c9ritacj",
    "gal_c9ritaluna",        "gal_c9ritavio",         "gal_c9ritaharuka",
    "gal_c10ritapool",       "gal_c10ritaoutside"
    ]