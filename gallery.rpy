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
    "gal_c10ritapool",       "gal_c10ritaoutside",    "gal_c11ritapizza",
    "gal_c11ritawoman",      "gal_c11viogirls",       "gal_c11vioguys",
    "gal_c12ritamia",        "gal_c12ritaconnor",     "gal_c12ritacj",
    "gal_c12ritagirl",       "gal_c12ritaguy",        "gal_c13ritaconnor",
    "gal_c13ritalucas",      "gal_c13ritaluna",       "gal_c14ritaguys",
    "gal_c14ritagirls",      "gal_c14ritaharuka",     "gal_c14ritacj",
    "gal_c14ritavio",        "gal_c15ritacj",         "gal_c15vioguys",
    "gal_c15viogirl",        "gal_c15ritagirls",      "gal_c15ritaspaguy",
    "gal_c15ritaspagirl",    "gal_c16hotsprings"#,     "gal_c17ritaspaguy",
    #"gal_c17ritaspagirl",    "gal_c17hotsprings",     "gal_c17pokerguys",
    #"gal_c17pokergirls",     "gal_c17pokervio",       "gal_c17pokerharuka",
    #"gal_c18lunaguy",        "gal_c18lunagirl",       "gal_c18stripgirls",
    #"gal_c18stripguys",      "gal_c18stripvio",       "gal_c19ritadreamguys",
    #"gal_c19ritadreamgirls", "gal_c19ritaguy",        "gal_c19ritagirl",
    #"gal_c19ritajason",      "gal_c19ritavio"
    ]