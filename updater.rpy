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