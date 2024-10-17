#Check the save file for version compliance and make adjustments
label after_load:
    if mod_version_control < 4:
        call screen modal_info("Sorry, the save file\nis not compatible with\nthe current version of the game.")
        $ MainMenu(confirm=False)()
    $ mod_version_control = mod_current_version
    return

#Check the "persistent" file for the images seen and open the gallery
label check_persistent_to_open_gallery:
    python:
        for i in galleries:
            if renpy.seen_image(i[1]):
                renpy.mark_label_seen(i[0])

    if renpy.seen_image("c9 threesome 41-c"):
        $ persistent.c9connorfirst=True
    if renpy.seen_image("c9 threesome 41-j"):
        $ persistent.c9joshfirst=True
    if renpy.seen_image("c10 pool 20"):
        $ persistent.c10poolsex=True
    if renpy.seen_image("c11 pizzaboy 31"):
        $ persistent.c11pizzasex=True
    if renpy.seen_image("c13 lunahome 25"):
        $ persistent.c13lunasex=True
    if renpy.seen_image("c14 cj sex dp 1"):
        $ persistent.c14dp=True
    if renpy.seen_image("c14 cj sex 20"):
        $ persistent.c14nodp=True
    if renpy.seen_image("c14 vio vag 1"):
        $ persistent.c14vagtoy=True
    if renpy.seen_image("c14 vio anal 1"):
        $ persistent.c14analtoy=True
    if renpy.seen_image("c16 hotsprings male sex 2v"):
        $ persistent.c16mixedvag = True
    if renpy.seen_image("c16 hotsprings male sex 2a"):
        $ persistent.c16mixedanal = True
    if renpy.seen_image("c17 pokersex boys 20"):
        $ persistent.c17dp=True
    if renpy.seen_image("c17 pokersex boys vagend 1"):
        $ persistent.c17nodp=True
    if renpy.seen_image("c18 luna male 30"):
        $ persistent.c18lunasexmale=True
    if renpy.seen_image("c18 luna female 29"):
        $ persistent.c18lunasexfemale=True
    return

#Check the "persistent" file for the images seen and open the chapters
label check_persistent_to_update_chapter_labels:
    if renpy.seen_image("c3 title"):
        $ renpy.mark_label_seen("chapter3")
    if renpy.seen_image("c4 title"):
        $ renpy.mark_label_seen("chapter4")
    if renpy.seen_image("c5 title"):
        $ renpy.mark_label_seen("chapter5")
    if renpy.seen_image("c6 title"):
        $ renpy.mark_label_seen("chapter6")
    if renpy.seen_image("c7 title"):
        $ renpy.mark_label_seen("chapter7")
    if renpy.seen_image("c8 title"):
        $ renpy.mark_label_seen("chapter8")
    if renpy.seen_image("c9 parents 1"):
        $ renpy.mark_label_seen("chapter9")
    if renpy.seen_image("c10 intro 1"):
        $ renpy.mark_label_seen("chapter10")
    if renpy.seen_image("c11 intro 1"):
        $ renpy.mark_label_seen("chapter11")
    if renpy.seen_image("c12 luna 1"):
        $ renpy.mark_label_seen("chapter12")
    if renpy.seen_image("c13 intro 1"):
        $ renpy.mark_label_seen("chapter13")
    if renpy.seen_image("c14 intro 1"):
        $ renpy.mark_label_seen("chapter14")
    if renpy.seen_image("c15 hotsprings 1"):
        $ renpy.mark_label_seen("chapter15")
    if renpy.seen_image("c16 intro 1"):
        $ renpy.mark_label_seen("chapter16")
    if renpy.seen_image("c17 title"):
        $ renpy.mark_label_seen("chapter17")
    if renpy.seen_image("c18 lucy garden 1"):
        $ renpy.mark_label_seen("chapter18")
    if renpy.seen_image("c19 dream male 1") or renpy.seen_image("c19 dream female 1"):
        $ renpy.mark_label_seen("chapter19")
    return
