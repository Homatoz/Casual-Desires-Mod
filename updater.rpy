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

    if save_updated:
        $ renpy.notify("Save updated")
        $ renpy.block_rollback()
    return