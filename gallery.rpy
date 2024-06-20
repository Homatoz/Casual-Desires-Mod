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
                            if renpy.seen_label(galleries[i][0]):
                                action Replay(galleries[i][0])
                            add galleries[i][0]:
                                if not renpy.seen_label(galleries[i][0]):
                                    blur 20.0
                else:
                    for i in range(first_scene,first_scene+last_num_scenes):
                        button:
                            if renpy.seen_label(galleries[i][0]):
                                action Replay(galleries[i][0])
                            add galleries[i][0]:
                                if not renpy.seen_label(galleries[i][0]):
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
    ["gal_prologueviosex","intro vio 1"],           ["gal_c2viopublicsex","c2 outside 3-13"],               ["gal_c2ritadream1","c2 dream 1"],
    ["gal_c2ritadream2","c2 dream 3"],              ["gal_c2ritadream3","c2 dream 4"],                      ["gal_c3viosex","c3 viosex 1"],
    ["gal_c4viosex","c4 vtoi 1"],                   ["gal_c5ritalocker","c5 locker 10"],                    ["gal_c5ritapizza","c5 hj 1"],
    ["gal_c5viogroup1","c5 viosex 1"],              ["gal_c5viogroup2","c5 viosex mff 1"],                  ["gal_c5viogroup3","c5 viosex mmf 1"],
    ["gal_c5viosex","c5 viosexalt 1"],              ["gal_c6ritapool","c6 pool 11"],                        ["gal_c6ritatheater","c6 theater 9"],
    ["gal_c6ritafj","c6 boys 7"],                   ["gal_c7ritabjconnor","c7 home 6"],                     ["gal_c7ritalocker","c7 locker 17"],
    ["gal_c7ritabjpool","c7 pool 4"],               ["gal_c7viogroup1","c7 vio mmf 1"],                     ["gal_c7viogroup2","c7 vio les 1"],
    ["gal_c8ritajosh","c8 josh 12"],                ["gal_c8ritapizza","c8 pizzaboy 1"],                    ["gal_c9ritacj","c9 threesome 19"],
    ["gal_c9ritaluna","c9 luna 10"],                ["gal_c9ritavio","c9 vio 18"],                          ["gal_c9ritaharuka","c9 haruka 11"],
    ["gal_c10ritapool","c10 pool 9"],               ["gal_c10ritaoutside","c10 outside 10"],                ["gal_c11ritapizza","c11 pizzaboy 8"],
    ["gal_c11ritawoman","c11 les 17"],              ["gal_c11viogirls","c11 vio les 1"],                    ["gal_c11vioguys","c11 vio mmf 1"],
    ["gal_c12ritamia","c12 mia 16"],                ["gal_c12ritaconnor","c12 cj 10"],                      ["gal_c12ritacj","c12 cj 33"],
    ["gal_c12ritagirl","c12 waterpark girl 6"],     ["gal_c12ritaguy","c12 waterpark male 6"],              ["gal_c13ritaconnor","c13 connor 12"],
    ["gal_c13ritalucas","c13 lucas 9"],             ["gal_c13ritaluna","c13 lunahome 16"],                  ["gal_c14ritaguys","c14 beachsex male 1"],
    ["gal_c14ritagirls","c14 beachsex female 1"],   ["gal_c14ritaharuka","c14 haruka home 11"],             ["gal_c14ritacj","c14 cj sex 1"],
    ["gal_c14ritavio","c14 vio 13"],                ["gal_c15ritacj","c15 cjextra 1"],                      ["gal_c15vioguys","c15 viosex male 1"],
    ["gal_c15viogirl","c15 viosex girl 1"],         ["gal_c15ritagirls","c15 girlsroom 6"],                 ["gal_c15ritaspaguy","c15 spa 19m"],
    ["gal_c15ritaspagirl","c15 spa 19f"],           ["gal_c16hotsprings","c16 hotsprings male oral 1"],     ["gal_c17ritaspagirl","c17 spa 9f"],
    ["gal_c17ritaspaguy","c17 spa 9m"],             ["gal_c17hotsprings","c17 hotsprings sex 1"],           ["gal_c17pokerguys","c17 pokersex boys 1"],
    ["gal_c17pokergirls","c17 pokersex girls 1"],   ["gal_c17pokervio","c17 pokersex violet 1"],            ["gal_c17pokerharuka","c17 pokersex haruka 1"],
    ["gal_c18lunaguy","c18 luna male 5"],           ["gal_c18lunagirl","c18 luna female 4"],                ["gal_c18stripgirls","c18 stripclubsex female 1"],
    ["gal_c18stripguys","c18 stripclubsex male 1"], ["gal_c18stripvio","c18 stripclubsex female violet 1"], ["gal_c19ritadreamguys","c19 dream male 1"],
    ["gal_c19ritadreamgirls","c19 dream female 1"], ["gal_c19ritagirl","c19 delivery 4f"],                  ["gal_c19ritaguy","c19 delivery 4m"],
    ["gal_c19ritajason","c19 jasonoffice 1"],       ["gal_c19ritavio","c19 viohome 16"]
    ]