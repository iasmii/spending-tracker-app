from domain.ap import *
from infrastructura.repository_apartamente import adauga_ap, cauta_ap_dupa_id, modifica_ap, sterge_ap_dupa_id, nr_ap, \
    get_all_aps
from validare.validator_ap import valideaza_ap

undo_stack = []

def pregatire_undo(ap, instr):
    """
    pregateste operatia de undo deoarece retine valorile de dinaintea modificarii listei
    :param ap: apartamentul care va fi modificat
    :param instr: retinem operatia pe care o facem ca sa o inversam in undo
    :return:
    """
    id_ap = get_id(ap)
    apa_vechi = get_apa(ap)
    canal_vechi = get_canal(ap)
    incalzire_vechi = get_incalzire(ap)
    gaz_vechi = get_gaz(ap)
    altele_vechi = get_altele(ap)
    ziua_vechi = get_ziua(ap)
    comanda = (instr, id_ap, apa_vechi, canal_vechi, incalzire_vechi, gaz_vechi, altele_vechi, ziua_vechi)
    adauga_undo(comanda)

def adauga_undo(comanda):
    """
    retinem intr-o lista care actioneaza ca si o stiva valorile inainte de a fi modificate
    :param comanda: tuplu care retine valorile vechi
    :return:
    """
    undo_stack.append(comanda)

def undo(aps):
    """
    anuleaza efectele ultimei operatii efectuate
    :param aps: dictionarul de apartamente1
    :return:
    """
    comanda = undo_stack.pop()
    (instr, id_ap, apa_vechi, canal_vechi, incalzire_vechi, gaz_vechi, altele_vechi, ziua_vechi) = comanda
    if instr == 1: #undo pt adaugare
        sterge_ap_dupa_id_service(aps, id_ap)
    elif instr == 2: #undo pt stergere/modificare
        ap = cauta_ap_dupa_id_service(aps, id_ap)
        set_apa(ap, apa_vechi)
        set_canal(ap, canal_vechi)
        set_incalzire(ap, incalzire_vechi)
        set_gaz(ap, gaz_vechi)
        set_altele(ap, altele_vechi)
        set_ziua(ap, ziua_vechi)

def adauga_ap_service(aps, id_ap, apa, canal, incalzire, gaz, altele, ziua):
    """
    adauga apartamentele in dictionar
    :param aps: dictionarul de apartamente
    :type aps: dictionar
    :param id_ap: id-ul unui apartament
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
    :param ziua: ziua in care cheltuielile au valorile date
    :type ziua: int
    :return:
    """
    ap = creeaza_ap(id_ap, apa, canal, incalzire, gaz, altele, ziua)
    valideaza_ap(ap)
    instr = 1
    pregatire_undo(ap, instr)
    adauga_ap(aps, ap)

def cauta_ap_dupa_id_service(aps, id_ap):
    """
    cauta apartamentul in fct de id
    :param aps: dictionar de apartamente
    :type aps: dictionar
    :param id_ap: id-ul ap cautat
    :type id_ap: int
    :return: functia de cautare dupa id din repository
    """
    return cauta_ap_dupa_id(aps, id_ap)

def modifica_ap_service(aps, id_ap, apa, canal, incalzire, gaz, altele, ziua):
    """
    modifica datele unui apartament, creand noul ap, validand datele noi si apeland fct in repository
    :param aps: dictionarul de apartamente
    :type aps: dictionar
    :param id_ap: id-ul unui apartament
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
    :param ziua: ziua in care cheltuielile au valorile date
    :type ziua: int
    :return:
    """
    ap = creeaza_ap(id_ap, apa, canal, incalzire, gaz, altele, ziua)
    valideaza_ap(ap)
    instr = 2
    pregatire_undo(ap, instr)
    modifica_ap(aps, ap)

def sterge_ap_dupa_id_service(aps, id_ap):
    """
    sterge apartamentul in fct de id
    :param aps: dictionarul de apartamente
    :type aps: dict
    :param id_ap: id-ul unui apartament
    :type id_ap: int
    :return:
    """
    sterge_ap_dupa_id(aps, id_ap)

def nr_ap_service(aps):
    """
    numara cate apartamente sunt in dictionar
    :param aps: dictionarul de apartamente
    :type aps: dictionar
    :return: nr de apartamente din dictionar
    """
    return nr_ap(aps)

def get_all_aps_service(aps):
    """
    returneaza o lista cu toate ap adaugate in dictionar
    :param aps: dictionarul de apartamente
    :type aps: dictionar
    :return: functia get_all_aps din repository
    """
    return get_all_aps(aps)

def schimba_cheltuiala(cmd, val, aps, id_ap):
    """
    modifica cheltuiala aleasa, inlocuind valoarea veche cu cea noua
    :param cmd: comanda care indica cheltuiala care trebuie modificata
    :type cmd: str
    :param val: valoarea noua a cheltuielii
    :type  val: int
    :param aps: dictionar de apartamente
    :type  aps: dictionar
    :param id_ap: id-ul apartamentului
    :type id_ap: int
    :return:
    """
    ap = cauta_ap_dupa_id_service(aps, id_ap)
    instr = 2
    pregatire_undo(ap, instr)
    cmd.lower().strip()
    apa = get_apa(ap)
    canal = get_canal(ap)
    incalzire = get_incalzire(ap)
    gaz = get_gaz(ap)
    altele = get_altele(ap)
    ziua = get_ziua(ap)
    if cmd == "apa":
        modifica_ap_service(aps, id_ap, val, canal, incalzire, gaz, altele, ziua)
    elif cmd == "canal":
        modifica_ap_service(aps, id_ap, apa, val, incalzire, gaz, altele, ziua)
    elif cmd == "incalzire":
        modifica_ap_service(aps, id_ap, apa, canal, val, gaz, altele, ziua)
    elif cmd == "gaz":
        modifica_ap_service(aps, id_ap, apa, canal, incalzire, val, altele, ziua)
    elif cmd == "altele":
        modifica_ap_service(aps, id_ap, apa, canal, incalzire, gaz, val, ziua)

def sterge_toate_cheltuielile(aps, id_ap):
    """
    sterge toate cheltuielile unui apartament
     :param aps: dictionar de apartamente
    :type  aps: dictionar
    :param id_ap: id-ul apartamentului
    :type id_ap: int
    :return:
    """
    ap = cauta_ap_dupa_id_service(aps, id_ap)
    instr = 2
    pregatire_undo(ap, instr)
    val = 0
    set_apa(ap, val)
    set_canal(ap, val)
    set_incalzire(ap, val)
    set_gaz(ap, val)
    set_altele(ap, val)

def sterge_cheltuieli_ap_consecutive(aps, primul_ap_de_sters, ultimul_ap_de_sters):
    """
    sterge cheltuielile apartamentelor consecutive
    :param aps: dictionar de apartamente
    :type  aps: dictionar
    :param primul_ap_de_sters: numarul primului apartament care va fi sters
    :type primul_ap_de_sters: int
    :param ultimul_ap_de_sters: numarul ultimului apartament care va fi sters
    :type ultimul_ap_de_sters: int
    :return:
    """
    lista_ap = get_all_aps_service(aps)
    nr = int(nr_ap_service(aps))
    for i in range(nr):
        ap = cauta_ap_dupa_id_service(aps, get_id(lista_ap[i]))
        if i >= primul_ap_de_sters or i <= ultimul_ap_de_sters:
            id_ap = get_id(ap)
            sterge_toate_cheltuielile(aps, id_ap)

def sterge_un_tip_de_cheltuiala(aps, cmd):
    """
    sterge un tip de cheltuiala de la toate apartamentele
    :param aps: dictionar de apartamente
    :type  aps: dictionar
    :param cmd: comanda care indica cheltuiala care trebuie stearsa
    :type cmd: str
    :return:
    """
    cmd.lower().strip()
    val = 0
    lista_ap = get_all_aps_service(aps)
    if cmd == "apa":
        nr = int(nr_ap_service(aps))
        for i in range(nr):
            ap = cauta_ap_dupa_id_service(aps, get_id(lista_ap[i]))
            instr = 2
            pregatire_undo(ap, instr)
            set_apa(ap, val)
    elif cmd == "canal":
        nr = int(nr_ap_service(aps))
        for i in range(nr):
            ap = cauta_ap_dupa_id_service(aps, get_id(lista_ap[i]))
            instr = 2
            pregatire_undo(ap, instr)
            set_canal(ap, val)
    elif cmd == "incalzire":
        nr = int(nr_ap_service(aps))
        for i in range(nr):
            ap = cauta_ap_dupa_id_service(aps, get_id(lista_ap[i]))
            instr = 2
            pregatire_undo(ap, instr)
            set_incalzire(ap, val)
    elif cmd == "gaz":
        nr = int(nr_ap_service(aps))
        for i in range(nr):
            ap = cauta_ap_dupa_id_service(aps, get_id(lista_ap[i]))
            instr = 2
            pregatire_undo(ap, instr)
            set_gaz(ap, val)
    elif cmd == "altele":
        nr = int(nr_ap_service(aps))
        for i in range(nr):
            ap = cauta_ap_dupa_id_service(aps, get_id(lista_ap[i]))
            instr = 2
            pregatire_undo(ap, instr)
            set_altele(ap, val)

def afis_cheltuieli_mai_mari_suma(aps, val):
    """
    afiseaza apartamentele cu totalul cheltuielilor mai mare ca si o suma data
    :param aps: dictionarul de apartamente
    :type aps: dictionar
    :param val: suma cu care se compara totalul cheltuielilor
    :type val: int
    :return:
    """
    lista_ap = get_all_aps_service(aps)
    nr = int(nr_ap_service(aps))
    ok = 0
    for i in range(nr):
        ap = cauta_ap_dupa_id_service(aps, get_id(lista_ap[i]))
        total_cheltuieli = get_apa(ap) + get_canal(ap) + get_incalzire(ap) + get_gaz(ap) + get_altele(ap)
        if total_cheltuieli > val:
            print("Id: ", get_id(ap), ", apa: ", get_apa(ap), ", canal: ", get_canal(ap), ", incalzire: ", get_incalzire(ap), ", gaz: ", get_gaz(ap), ", altele: ", get_altele(ap), ", ziua: ", get_ziua(ap))
            ok = 1
    if ok == 0:
        print("Niciun apartament nu indeplineste conditia!")

def afis_un_tip_de_cheltuiala(aps, cmd):
    """
    afiseaza un tip de cheltuiala de la toate apartamentele
    :param aps: dictionarul de apartamente
    :type aps: dictionar
    :param cmd: comanda care indica cheltuiala de afisat
    :type cmd: str
    :return:
    """
    cmd.lower().strip()
    lista_ap = get_all_aps_service(aps)
    if cmd == "apa":
        nr = int(nr_ap_service(aps))
        for i in range(nr):
            ap = cauta_ap_dupa_id_service(aps, get_id(lista_ap[i]))
            print("Id: ", get_id(ap), ", apa: ", get_apa(ap), ";")
    elif cmd == "canal":
        nr = int(nr_ap_service(aps))
        for i in range(nr):
            ap = cauta_ap_dupa_id_service(aps, get_id(lista_ap[i]))
            print("Id: ", get_id(ap), ", canal: ", get_canal(ap), ";")
    elif cmd == "incalzire":
        nr = int(nr_ap_service(aps))
        for i in range(nr):
            ap = cauta_ap_dupa_id_service(aps, get_id(lista_ap[i]))
            print("Id: ", get_id(ap), ", incalzire: ", get_incalzire(ap), ";")
    elif cmd == "gaz":
        nr = int(nr_ap_service(aps))
        for i in range(nr):
            ap = cauta_ap_dupa_id_service(aps, get_id(lista_ap[i]))
            print("Id: ", get_id(ap), ", gaz: ", get_gaz(ap), ";")
    elif cmd == "altele":
        nr = int(nr_ap_service(aps))
        for i in range(nr):
            ap = cauta_ap_dupa_id_service(aps, get_id(lista_ap[i]))
            print("Id: ", get_id(ap), ", altele: ", get_altele(ap), ";")

def suma_totala_pt_un_tip_cheltuiala(aps, cmd):
    """
    calculeaza suma totala pt un tip de cheltuiala de la toate apartamentele
    :param aps: dictionarul de apartamente
    :type aps: dictionar
    :param cmd: comanda care indica cheltuiala pt care se calculeaza suma
    :type cmd: str
    :return: suma totala pt un tip de cheltuiala de la toate apartamentele
    """
    cmd.lower().strip()
    lista_ap = get_all_aps_service(aps)
    suma = 0
    if cmd == "apa":
        nr = int(nr_ap_service(aps))
        for i in range(nr):
            ap = cauta_ap_dupa_id_service(aps, get_id(lista_ap[i]))
            suma += get_apa(ap)
    elif cmd == "canal":
        nr = int(nr_ap_service(aps))
        for i in range(nr):
            ap = cauta_ap_dupa_id_service(aps, get_id(lista_ap[i]))
            suma += get_canal(ap)
    elif cmd == "incalzire":
        nr = int(nr_ap_service(aps))
        for i in range(nr):
            ap = cauta_ap_dupa_id_service(aps, get_id(lista_ap[i]))
            suma += get_incalzire(ap)
    elif cmd == "gaz":
        nr = int(nr_ap_service(aps))
        for i in range(nr):
            ap = cauta_ap_dupa_id_service(aps, get_id(lista_ap[i]))
            suma += get_gaz(ap)
    elif cmd == "altele":
        nr = int(nr_ap_service(aps))
        for i in range(nr):
            ap = cauta_ap_dupa_id_service(aps, get_id(lista_ap[i]))
            suma += get_altele(ap)
    return suma

def suma_totala_pt_un_ap(aps, id_ap):
    """
    calculeaza suma tutror cheltuielilor de la un apartament
    :param aps: dictionarul de apartamente
    :type aps: dictionar
    :param id_ap: id-ul unui apartament
    :type id_ap: int
    :return: suma tutror cheltuielilor de la un apartament
    """
    ap = cauta_ap_dupa_id_service(aps, id_ap)
    suma = get_apa(ap) + get_canal(ap) + get_incalzire(ap) + get_gaz(ap) + get_altele(ap)
    return suma

def sterge_cheltuieli_mai_mici(aps, val):
    """
    sterge toate cheltuielile mai mici decat o suma data
    :param aps: dictionarul de apartamente
    :type aps: dictionar
    :param val: suma cu care se compara cheltuielile
    :type val: int
    :return:
    """
    lista_ap = get_all_aps_service(aps)
    zero = 0
    nr = int(nr_ap_service(aps))
    for i in range(nr):
        ap = cauta_ap_dupa_id_service(aps, get_id(lista_ap[i]))
        instr = 2
        pregatire_undo(ap, instr)
        if get_apa(ap) < val:
            set_apa(ap, zero)
        if get_canal(ap) < val:
            set_canal(ap, zero)
        if get_incalzire(ap) < val:
            set_incalzire(ap, zero)
        if get_gaz(ap) < val:
            set_gaz(ap, zero)
        if get_altele(ap) < val:
            set_altele(ap, zero)

def sortare_dupa_cheltuiala(aps, cmd):
    """
    afiseaza si sorteaza crescator apartamentele in functie de valoarea unui tip de cheltuiala
    :param aps: dictionarul de apartamente
    :type aps: dictionar
    :param cmd: comanda care indica cheltuiala in functie de care se sorteaza apartamentele
    :type cmd: str
    :return:
    """
    cmd.lower().strip()
    lista_ap = get_all_aps_service(aps)
    if cmd == "apa":
        nr = int(nr_ap_service(aps))
        for i in range(nr-1):
            for j in range(i+1, nr):
                api = cauta_ap_dupa_id_service(aps, get_id(lista_ap[i]))
                apj = cauta_ap_dupa_id_service(aps, get_id(lista_ap[j]))
                if get_apa(api)>get_apa(apj):
                    aux=lista_ap[i]
                    lista_ap[i]=lista_ap[j]
                    lista_ap[j]=aux
    elif cmd == "canal":
        nr = int(nr_ap_service(aps))
        for i in range(nr - 1):
            for j in range(i + 1, nr):
                api = cauta_ap_dupa_id_service(aps, get_id(lista_ap[i]))
                apj = cauta_ap_dupa_id_service(aps, get_id(lista_ap[j]))
                if get_canal(api) > get_canal(apj):
                    aux = lista_ap[i]
                    lista_ap[i] = lista_ap[j]
                    lista_ap[j] = aux
    elif cmd == "incalzire":
        nr = int(nr_ap_service(aps))
        for i in range(nr - 1):
            for j in range(i + 1, nr):
                api = cauta_ap_dupa_id_service(aps, get_id(lista_ap[i]))
                apj = cauta_ap_dupa_id_service(aps, get_id(lista_ap[j]))
                if get_incalzire(api) > get_incalzire(apj):
                    aux = lista_ap[i]
                    lista_ap[i] = lista_ap[j]
                    lista_ap[j] = aux
    elif cmd == "gaz":
        nr = int(nr_ap_service(aps))
        for i in range(nr - 1):
            for j in range(i + 1, nr):
                api = cauta_ap_dupa_id_service(aps, get_id(lista_ap[i]))
                apj = cauta_ap_dupa_id_service(aps, get_id(lista_ap[j]))
                if get_gaz(api) > get_gaz(apj):
                    aux = lista_ap[i]
                    lista_ap[i] = lista_ap[j]
                    lista_ap[j] = aux
    elif cmd == "altele":
        nr = int(nr_ap_service(aps))
        for i in range(nr - 1):
            for j in range(i + 1, nr):
                api = cauta_ap_dupa_id_service(aps, get_id(lista_ap[i]))
                apj = cauta_ap_dupa_id_service(aps, get_id(lista_ap[j]))
                if get_altele(api) > get_altele(apj):
                    aux = lista_ap[i]
                    lista_ap[i] = lista_ap[j]
                    lista_ap[j] = aux
    nr = int(nr_ap_service(aps))
    for i in range(nr):
        ap = cauta_ap_dupa_id_service(aps, get_id(lista_ap[i]))
        print("Id: ", get_id(ap), ", apa: ", get_apa(ap), ", canal: ", get_canal(ap), ", incalzire: ", get_incalzire(ap), ", gaz: ", get_gaz(ap), ", altele: ", get_altele(ap), ", ziua: ", get_ziua(ap))

def afis_cheltuieli_mai_mari_suma_ziua(aps, val, data):
    """
    afiseaza apartamentele al caror total de cheltuieli e mai mare decat o suma data si au fost inregistrate inainte de ziua data
    :param aps: dictionarul de apartamente
    :type aps: dictionar
    :param val: suma cu care se compara totalul cheltuielilor
    :type val: int
    :param data: ziua cu care se compara data cheltuielilor
    :type data: int
    :return:
    """
    lista_ap = get_all_aps_service(aps)
    nr = int(nr_ap_service(aps))
    ok = 0
    for i in range(nr):
        ap = cauta_ap_dupa_id_service(aps, get_id(lista_ap[i]))
        ziua = get_ziua(ap)
        suma = suma_totala_pt_un_ap(aps, get_id(ap))
        if suma > val and ziua < data:
            print("Id: ", get_id(ap), ", apa: ", get_apa(ap), ", canal: ", get_canal(ap), ", incalzire: ", get_incalzire(ap), ", gaz: ", get_gaz(ap), ", altele: ", get_altele(ap), ", ziua: ", get_ziua(ap))
            ok = 1
    if ok == 0:
        print("Niciun apartament nu indeplineste conditia!")

def afis_lista(aps):
    lista_ap = get_all_aps_service(aps)
    nr = int(nr_ap_service(aps))
    for i in range (nr):
        ap = cauta_ap_dupa_id_service(aps, get_id(lista_ap[i]))
        print("Id: ", get_id(ap), ", apa: ", get_apa(ap), ", canal: ", get_canal(ap), ", incalzire: ", get_incalzire(ap), ", gaz: ", get_gaz(ap), ", altele: ", get_altele(ap), ", ziua: ", get_ziua(ap))

def separa_optiunea(aps, option):
    lista = option.split()
    print(lista)
    if lista[0] == "adaugare":
        if lista[1] == "adauga":
            for i in range (len(lista)-1):
                if lista[i] == "id":
                    id_ap = int(lista[i+1])
                elif lista[i] == "apa":
                    apa = int(lista[i+1])
                elif lista[i] == "canal":
                    canal = int(lista[i+1])
                elif lista[i] == "incalzire":
                    incalzire = int(lista[i+1])
                elif lista[i] == "gaz":
                    gaz = int(lista[i+1])
                elif lista[i] == "altele":
                    altele = int(lista[i+1])
                elif lista[i] == "ziua":
                    ziua = int(lista[i+1])
            adauga_ap_service(aps, id_ap, apa, canal, incalzire, gaz, altele, ziua)
        elif lista[1] == "modifica":
            for i in range(len(lista) - 1):
                if lista[i] == "id":
                    id_ap = int(lista[i+1])
                elif lista[i] == "apa":
                    cmd = "apa"
                    val = int(lista[i + 1])
                elif lista[i] == "canal":
                    cmd = "canal"
                    val = int(lista[i + 1])
                elif lista[i] == "incalzire":
                    cmd = "incalzire"
                    val = int(lista[i + 1])
                elif lista[i] == "gaz":
                    cmd = "gaz"
                    val = int(lista[i + 1])
                elif lista[i] == "altele":
                    cmd = "altele"
                    val = int(lista[i + 1])
            schimba_cheltuiala(cmd, val, aps, id_ap)
    elif lista[0] == "stergere":
        if lista[1] == "tot":
            for i in range (len(lista)-1):
                if lista[i] == "id":
                    id_ap = int(lista[i+1])
            sterge_toate_cheltuielile(aps, id_ap)
        if lista[1] == "consecutive":
            for i in range(len(lista) - 1):
                if lista[i] == "nr_primul_ap":
                    nr_primul_ap = int(lista[i + 1])
                if lista[i] == "nr_ultimul_ap":
                    nr_ultimul_ap = int(lista[i + 1])
            sterge_cheltuieli_ap_consecutive(aps, nr_primul_ap, nr_ultimul_ap)
        if lista[1] == "cheltuiala":
            for i in range(len(lista) - 1):
                if lista[i] == "apa":
                    cmd = "apa"
                elif lista[i] == "canal":
                    cmd = "canal"
                elif lista[i] == "incalzire":
                    cmd = "incalzire"
                elif lista[i] == "gaz":
                    cmd = "gaz"
                elif lista[i] == "altele":
                    cmd = "altele"
            sterge_un_tip_de_cheltuiala(aps, cmd)
"""
def extrage_cheltuieli(aps, id_ap, cheltuieli):
    res=[int(i) for i in cheltuieli.split(", ") if i.isdigit()]
    nr = len(res)
    for i in range(nr):
        if i == 0:
            apa = res[i]
        elif i == 1:
            canal = res[i]
        elif i == 2:
            incalzire = res[i]
        elif i == 3:
            gaz = res[i]
        elif i == 4:
            altele = res[i]
        elif i == 5:
            ziua = res[i]
    adauga_ap_service(aps, id_ap, apa, canal, incalzire, gaz, altele, ziua)
"""