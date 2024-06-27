from bussines.service_ap import *
from domain.ap import *  # incarcam toate fct
from infrastructura.repository_apartamente import *
from validare.validator_ap import valideaza_ap


def ruleaza_teste_domeniu():
    id_ap = 3
    apa = 100
    canal = 150
    incalzire = 200
    gaz = 250
    altele = 300
    ziua = 16
    ap = creeaza_ap(id_ap, apa, canal, incalzire, gaz, altele, ziua)
    assert (get_id(ap) == id_ap)
    assert (get_apa(ap) == apa)
    assert (get_canal(ap) == canal)
    assert (get_incalzire(ap) == incalzire)
    assert (get_gaz(ap) == gaz)
    assert (get_altele(ap) == altele)
    assert (get_ziua(ap) == ziua)
    apa_nou = 300
    set_apa(ap, apa_nou)
    assert (get_apa(ap) == apa_nou)
    altele_nou = 150
    set_altele(ap, altele_nou)
    alt_ap_acelasi_id = creeaza_ap(id_ap, apa_nou, canal, incalzire, gaz, altele_nou, ziua)
    assert (egal_ap(ap, alt_ap_acelasi_id))


def ruleaza_teste_validare():
    id_ap = 3
    apa = 100
    canal = 150
    incalzire = 200
    gaz = 250
    altele = 300
    ziua = 16
    ap = creeaza_ap(id_ap, apa, canal, incalzire, gaz, altele, ziua)
    valideaza_ap(ap)
    id_ap_invalid = -3
    apa_invalid = -4
    canal_invalid = -8
    incalzire_invalid = -100
    gaz_invalid = -98
    altele_invalid = -31
    ziua_invalid = 67
    ap_invalid = creeaza_ap(id_ap_invalid, apa_invalid, canal_invalid, incalzire_invalid, gaz_invalid, altele_invalid, ziua_invalid)
    try:
        valideaza_ap(ap_invalid)
        assert False
    except ValueError as ve:
        assert (str(ve) == "id invalid!\nsuma apa invalida!\nsuma canal invalida!\nsuma incalzire invalida!\nsuma gaz invalida!\nsuma altele invalida!\nziua invalida!\n")


def ruleaza_teste_infrastructura():
    aps = {}  # dictionar de apartamente
    assert (nr_ap(aps) == 0)
    id_ap = 3
    apa = 100
    canal = 150
    incalzire = 200
    gaz = 250
    altele = 300
    ziua = 9
    ap = creeaza_ap(id_ap, apa, canal, incalzire, gaz, altele, ziua)
    adauga_ap(aps, ap)
    assert (nr_ap(aps) == 1)
    try:
        adauga_ap(aps, ap)
        assert False
    except ValueError as ve:
        assert (str(ve) == "apartament existent!")
    ap_gasit = cauta_ap_dupa_id(aps, id_ap)
    assert (egal_ap(ap_gasit, ap))
    alt_id = 1
    ap_alt_id = creeaza_ap(alt_id, apa, canal, incalzire, gaz, altele, ziua)
    try:
        sterge_ap_dupa_id(aps, alt_id)
        assert False
    except ValueError as ve:
        assert (str(ve) == "apartament inexistent!")
    try:
        modifica_ap(aps, ap_alt_id)
        assert False
    except ValueError as ve:
        assert (str(ve) == "apartament inexistent!")
    adauga_ap(aps, ap_alt_id)
    assert (nr_ap(aps) == 2)
    lista_aps = get_all_aps(aps)
    assert (len(lista_aps) == 2)
    assert (egal_ap(lista_aps[0], ap))
    assert (egal_ap(lista_aps[1], ap_alt_id))
    apa_nou = 500
    canal_nou = 700
    ap_modificat = creeaza_ap(id_ap, apa_nou, canal_nou, incalzire, gaz, altele, ziua) #eroare?
    modifica_ap(aps, ap_modificat)
    ap_gasit = cauta_ap_dupa_id(aps, id_ap)
    assert (get_apa(ap_gasit) == apa_nou)
    sterge_ap_dupa_id(aps, id_ap)
    assert (nr_ap(aps) == 1)


def ruleaza_teste_bussines():
    aps = {}
    assert (nr_ap_service(aps) == 0)
    id_ap = 3
    apa = 200
    canal = 300
    incalzire = 100
    gaz = 400
    altele = 50
    ziua = 28
    adauga_ap_service(aps, id_ap, apa, canal, incalzire, gaz, altele, ziua)
    assert (nr_ap_service(aps) == 1)
    ap_gasit = cauta_ap_dupa_id_service(aps, id_ap)
    assert(get_id(ap_gasit) == id_ap)
    try:
        adauga_ap_service(aps, id_ap, apa, canal, incalzire, gaz, altele, ziua)
        assert False
    except ValueError as ve:
        assert(str(ve) == "apartament existent!")
    alt_id_ap = 9
    try:
        cauta_ap_dupa_id_service(aps, alt_id_ap)
        assert False
    except ValueError as ve:
        assert(str(ve) == "apartament inexistent!")
    apa_nou = 700
    canal_nou = 90
    try:
        modifica_ap_service(aps, alt_id_ap, apa_nou, canal_nou, incalzire, gaz, altele, ziua)
        assert False
    except ValueError as ve:
        assert(str(ve) == "apartament inexistent!")
    try:
        sterge_ap_dupa_id_service(aps,alt_id_ap)
        assert False
    except ValueError as ve:
        assert(str(ve) == "apartament inexistent!")
    id_ap_invalid = -1
    apa_invalid = -2
    canal_invalid = -78
    incalzire_invalid = -46
    gaz_invalid = -21
    altele_invalid = -55
    ziua_invalid = 0
    try:
        adauga_ap_service(aps, id_ap_invalid, apa_invalid, canal_invalid, incalzire_invalid, gaz_invalid, altele_invalid, ziua_invalid)
        assert False
    except ValueError as ve:
        assert(str(ve) == "id invalid!\nsuma apa invalida!\nsuma canal invalida!\nsuma incalzire invalida!\nsuma gaz invalida!\nsuma altele invalida!\nziua invalida!\n")
    adauga_ap_service(aps, alt_id_ap, apa, canal, incalzire, gaz, altele, ziua)
    assert(nr_ap_service(aps) == 2)
    lista_aps=get_all_aps_service(aps)
    assert(len(lista_aps) == 2)
    modifica_ap_service(aps, id_ap, apa_nou, canal_nou, incalzire, gaz, altele, ziua)
    ap_gasit=cauta_ap_dupa_id_service(aps, id_ap)
    assert (get_apa(ap_gasit) == apa_nou)
    sterge_ap_dupa_id_service(aps, id_ap)
    assert(nr_ap_service(aps) == 1)

def ruleaza_toate_testele():
    ruleaza_teste_domeniu()
    ruleaza_teste_validare()
    ruleaza_teste_infrastructura()
    ruleaza_teste_bussines()
