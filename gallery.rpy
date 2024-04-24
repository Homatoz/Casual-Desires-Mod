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
                            if galleries[i][2]:
                                action Replay(galleries[i][1])
                            add galleries[i][0]:
                                if not galleries[i][2]:
                                    blur 20.0
                else:
                    for i in range(first_scene,first_scene+last_num_scenes):
                        button:
                            if galleries[i][2]:
                                action Replay(galleries[i][1])
                            add galleries[i][0]:
                                if not galleries[i][2]:
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

# image, label, unlocked
define galleries = [
    ["gal_prologueviosex.jpg","gal_prologueviosex",True],
    ["gal_c2viopublicsex.jpg","gal_c2viopublicsex",True],
    ["gal_c2ritadream1.jpg","gal_c2ritadream1",True],
    ["gal_c2ritadream2.jpg","gal_c2ritadream2",True],
    ["gal_c2ritadream3.jpg","gal_c2ritadream3",True],
    ["gal_c3viosex.jpg","gal_c3viosex",True],
    ["gal_c4viosex.jpg","gal_c4viosex",True],
    ["gal_c5ritalocker.jpg","gal_c5ritalocker",True],
    ["gal_c5ritapizza.jpg","gal_c5ritapizza",True],
    ["gal_c5viogroup1.jpg","gal_c5viogroup1",True],
    ["gal_c5viogroup2.jpg","gal_c5viogroup2",True],
    ["gal_c5viogroup3.jpg","gal_c5viogroup3",True],
    ["gal_c5viosex.jpg","gal_c5viosex",True],
    ["gal_c6ritapool.jpg","gal_c6ritapool",True],
    ["gal_c6ritatheater.jpg","gal_c6ritatheater",True],
    ["gal_c6ritafj.jpg","gal_c6ritafj",True],
    ["gal_c7ritabjconnor.jpg","gal_c7ritabjconnor",True],
    ["gal_c7ritalocker.jpg","gal_c7ritalocker",True],
    ["gal_c7ritabjpool.jpg","gal_c7ritabjpool",True],
    ["gal_c7viogroup1.jpg","gal_c7viogroup1",True],
    ["gal_c7viogroup2.jpg","gal_c7viogroup2",True]
    ]