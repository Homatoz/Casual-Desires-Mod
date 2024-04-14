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
                            if galleries[first_scene][2]:
                                action Replay(galleries[first_scene][1])
                            add galleries[first_scene][0]:
                                if not galleries[first_scene][2]:
                                    blur 20.0
                            $ first_scene += 1
                else:
                    for i in range(first_scene,first_scene+last_num_scenes):
                        button:
                            if galleries[first_scene][2]:
                                action Replay(galleries[first_scene][1])
                            add galleries[first_scene][0]:
                                if not galleries[first_scene][2]:
                                    blur 20.0
                            $ first_scene += 1
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
    ["galch0sc1.jpg","prologue",True]
    ]