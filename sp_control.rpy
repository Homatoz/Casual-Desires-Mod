label add_partner(partner):
    if partner not in sexpartners:
        $ sexpartners.append(partner)
    return

label check_partner(partner):
    return partner in sexpartners

label first_partner(partner):
    if fp == "None":
        $ fp = partner
    return
