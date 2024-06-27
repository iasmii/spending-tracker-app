def creeaza_ap(id_ap, apa, canal, incalzire, gaz, altele, ziua):
    """
    creeaza un apartament
    :param id_ap: numarul apartemntului
    :type id_ap: int
    :param apa: suma cheltuita pt apa
    :type apa: int
    :param canal: suma cheltuita pt canal
    :type canal: int
    :param incalzire: suma cheltuita pt incalzire
    :type incalzire: int
    :param gaz: suma cheltuita pt gaz
    :type gaz: int
    :param altele: suma cheltuita pt altele
    :type altele: int
    :param ziua: ziua pt care cheltuielile au valorile date
    :type ziua: int
    :return: cheltuielile pt apartamentul creat
    :rtype: dict (chei:nr, apa, canal, incalzire, gaz, altele)
    """
    return {
        'id':id_ap,
        'apa':apa,'canal':canal,
        'incalzire':incalzire,
        'gaz':gaz,
        'altele':altele,
        'ziua':ziua
    }

def get_id(ap):
    return ap['id']

def get_apa(ap):
    return ap['apa']

def get_canal(ap):
    return ap['canal']

def get_incalzire(ap):
    return ap['incalzire']

def get_gaz(ap):
    return ap['gaz']

def get_altele(ap):
    return ap['altele']

def get_ziua(ap):
    return ap['ziua']

#id ul nu se schimba deci nu facem set pt id

def set_apa(ap, apa_nou):
    ap['apa'] = apa_nou

def set_canal(ap, canal_nou):
    ap['canal'] = canal_nou

def set_incalzire(ap, incalzire_nou):
    ap['incalzire'] = incalzire_nou

def set_gaz(ap, gaz_nou):
    ap['gaz'] = gaz_nou

def set_altele(ap, altele_nou):
    ap['altele'] = altele_nou

def set_ziua(ap, ziua_nou):
    ap['ziua'] = ziua_nou

def egal_ap(ap1, ap2):
    return get_id(ap1) == get_id(ap2)