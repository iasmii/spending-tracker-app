from domain.ap import get_id

def adauga_ap(aps, ap):
    id_ap=get_id(ap)
    if id_ap in aps:
        raise ValueError("apartament existent!")
    aps[id_ap]=ap

def nr_ap(aps):
    return len(aps)

def cauta_ap_dupa_id(aps, id_ap):
    if id_ap not in aps:
        raise ValueError("apartament inexistent!")
    return aps[id_ap]

def sterge_ap_dupa_id(aps, id_ap):
    if id_ap not in aps:
        raise ValueError("apartament inexistent!")
    del aps[id_ap]

def modifica_ap(aps, ap):
    id_ap = get_id(ap)
    if id_ap not in aps:
        raise ValueError("apartament inexistent!")
    aps[id_ap] = ap

def get_all_aps(aps):
    lista_ap = []
    for id_ap in aps:
        lista_ap.append(aps[id_ap])
    return lista_ap
