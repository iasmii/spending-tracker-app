from domain.ap import get_id, get_apa, get_canal, get_incalzire, get_gaz, get_altele, get_ziua

def valideaza_ap(ap):
    erori = ""
    if get_id(ap) < 1:
        erori += "id invalid!\n"
    if get_apa(ap) < 0:
        erori += "suma apa invalida!\n"
    if get_canal(ap) < 0:
        erori += "suma canal invalida!\n"
    if get_incalzire(ap) < 0:
        erori += "suma incalzire invalida!\n"
    if get_gaz(ap) < 0:
        erori += "suma gaz invalida!\n"
    if get_altele(ap) < 0:
        erori += "suma altele invalida!\n"
    if get_ziua(ap) < 1 or get_ziua(ap) > 31:
        erori += "ziua invalida!\n"
    if len(erori) > 0:
        raise ValueError(erori)
