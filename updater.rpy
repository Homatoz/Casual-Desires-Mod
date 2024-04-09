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
        $ sexpartners = sexp
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

    if save_updated:
        $ renpy.notify("Save updated")
        $ renpy.block_rollback()
    return