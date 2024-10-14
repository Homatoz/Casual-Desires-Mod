#Processing saves from the original game for correct work with the mod

label after_load:
    $ save_updated = False

    if hasattr(renpy.store, 'vir'):
        if vir == "Yes":
            $ virgin = True
        else:
            $ virgin = False
        $ del vir
        $ save_updated = True

    if hasattr(renpy.store, 'anvi'):
        if anvi == "Yes":
            $ analvirgin = True
        else:
            $ analvirgin = False
        $ del anvi
        $ save_updated = True

    if hasattr(renpy.store, 'sexp'):
        if fp=="Boyfriend" or fp=="Classmate" or fp=="Stranger":
            call add_partner(fp)
        if c9evelyn_is_partner:
            call add_partner("Evelyn")
        if c9connorfirst or c9joshfirst or c12cjsex or c14cjsex or c17pokersexboys:
            call add_partner("Connor")
            call add_partner("Josh")
        if c9lunasex and c9hadsex or c13lunasex or c15girlsthreesome:
            call add_partner("Luna")
        if c9viosex and c9hadsex or c14viosexvag or c18stripclubsexvio or ritaviorelationship or ritavioopenrelationship:
            call add_partner(vioname)
        if c9harukasex and c9hadsex or c14harukasex or c15girlsthreesome:
            call add_partner(frname)
        if c10poolsex:
            call add_partner("Pool Pervert")
        if c11pizzasex:
            call add_partner("Pizza Boy")
        if c11les:
            call add_partner("Female stranger from the street")
        if c12miasex:
            call add_partner("Mia")
        if c12waterparkfemale:
            call add_partner("Female stranger from the water park")
        if c14beachfemalesex:
            call add_partner("Female stranger 1 from the beach")
            call add_partner("Female stranger 2 from the beach")
        if c16mixedvag or c16mixedanal:
            call add_partner("Hotsprings Man")
        if c17spafemale:
            call add_partner("Masseuse")
        if c17spamale:
            call add_partner("Masseur")
        if c17hotspringsthreesome:
            call add_partner("Hotsprings Girl")
        if c17pokersexboys:
            call add_partner("Cedrick")
        if c17pokersexvio:
            call add_partner("Nick")
        if c17pokersexhar:
            call add_partner("Josh")
        if c18stripclubsexfemale:
            call add_partner("Stripclub Girl")
        if c18stripclubsexmale:
            call add_partner("Male stranger 1 from the stripclub")
            call add_partner("Male stranger 2 from the stripclub")
        $ del sexp
        $ save_updated = True

    if hasattr(renpy.store, 'sexe'):
        $ sexexp = sexe
        $ del sexe
        $ save_updated = True

    if lesonly == "False":
        $ lesonly = False
        $ save_updated = True

    if type(c2poolex) == int:
        $ c2poolex = bool(c2poolex)
        $ c2see = bool(c2see)
        $ c2_end1 = bool(c2_end1)
        $ c2_end2 = bool(c2_end2)
        $ c2_end3 = bool(c2_end3)
        $ save_updated = True

    if hasattr(renpy.store, 'lunanoclub'):
        $ c13lunanoclub = lunanoclub
        $ del lunanoclub
        $ save_updated = True

    if hasattr(renpy.store, 'lunamaleclub'):
        $ c13lunamaleclub = lunamaleclub
        $ del lunamaleclub
        $ save_updated = True

    if hasattr(renpy.store, 'lunafemaleclub'):
        $ c13lunafemaleclub = lunafemaleclub
        $ del lunafemaleclub
        $ save_updated = True

    if hasattr(renpy.store, 'vioc'):
        $ c3vioopenminded = bool(vioc)
        $ del vioc
        $ del viop
        $ save_updated = True

    if c6parkgirl or c8mia or c10mia:
        $ rita_met_mia = True

    if c10jasontease or c12jasonflirt or c15jasontease:
        $ rita_teased_jason = True

    if c5handjob or c6poolhj or c6theaterhj or c6joshfj or c7connorbj or c7poolbj:
        $ rita_held_dick = True

    if save_updated:
        $ renpy.notify("Save updated")
        $ renpy.block_rollback()
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
