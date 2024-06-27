from bussines.service_ap import *
from domain.ap import *  # incarcam toate fct

def ruleaza_ui():
    print("1. Adaugare")
    print("2. Stergere")
    print("3. Cautari")
    print("4. Rapoarte")
    print("5. Filtru")
    print("6. Undo")
    print("7. Iesire")

def start_ui():
    finished=False
    aps = {}
    while not finished:
        ruleaza_ui()
        #option=int(input("Optiunea dumneavoastra este: "))
        option = input("Introduceti comanda, subcomanda, id, cheltiuelile si ziua: ")
        separa_optiunea(aps, option)
        afis_lista(aps)
        """
        if option==1: #adaugare
            print("Optiunile de adaugare sunt:")
            print("1. Adauga o cheltuiala")
            print("2. Modifica o cheltuiala")
            subopt=int(input("Optiunea dumneavoastra de adaugare este: "))
            if subopt==1:
                id_ap = int(input("Introduceti id-ul apartamentului: "))
                apa = int(input("Introduceti suma cheltuita pt apa: "))
                canal = int(input("Introduceti suma cheltuita pt canal: "))
                incalzire = int(input("Introduceti suma cheltuita pt incalzire: "))
                gaz = int(input("Introduceti suma cheltuita pt gaz: "))
                altele = int(input("Introduceti suma cheltuita pt altele: "))
                ziua = int(input("Introduceti ziua in care se inregisreaza cheltuielile: "))
                adauga_ap_service(aps, id_ap, apa, canal, incalzire, gaz, altele, ziua)
                
                cheltuieli = input("Introduceti suma cheltuita pt: apa, canal, incalzire, gaz, altele si ziua: ")
                extrage_cheltuieli(aps, id_ap, cheltuieli)
                
                print("Apartamentul a fost adaugat cu succes!")
                afis_lista(aps)
            elif subopt==2:
                id_ap = int(input("Introduceti id-ul apartamentului: "))
                print("Cheltuielile care pot fi modificate sunt: apa, canal, incalzire, gaz, altele.")
                cmd = input("Cheltuiala pe care doriti sa o modificati este: ")
                val = int(input("Valoarea noua pt aceasta cheltuiala este: "))
                schimba_cheltuiala(cmd, val, aps, id_ap)
                print("Cheltuiala a fost modificata cu succes!")
                afis_lista(aps)
        
        elif option==2: #stergere
            print("Optiunile de stergere sunt:")
            print("1. Sterge toate cheltuielile de la un apartament")
            print("2. Sterge cheltuielile de la apartamente consecutive")
            print("3. Sterge cheltuielile de un anumit tip de la toate apartamentele")
            subopt = int(input("Optiunea dumneavoastra de stergere este:"))
            if subopt == 1:
                id_ap = int(input("Introduceti id-ul apartamentului: "))
                sterge_toate_cheltuielile(aps, id_ap)
                print("Cheltuielile au fost sterse cu succes!")
                afis_lista(aps)
            elif subopt == 2:
                primul_ap_de_sters = int(input("Introduceti numarul primului apartament din stergere:"))
                ultimul_ap_de_sters = int(input("Introduceti numarul ultimului apartament din stergere:"))
                sterge_cheltuieli_ap_consecutive(aps, primul_ap_de_sters, ultimul_ap_de_sters)
                print("Cheltuielile au fost sterse cu succes!")
                afis_lista(aps)
            elif subopt == 3:
                print("Cheltuielile care pot fi sterse sunt: apa, canal, incalzire, gaz, altele.")
                cmd = input("Cheltuiala pe care doriti sa o stergeti este: ")
                sterge_un_tip_de_cheltuiala(aps, cmd)
                print("Cheltuiala a fost stersa de la toate apartamentele cu succes!")
                afis_lista(aps)

        elif option==3: #cautari
            print("Optiunile de cautari sunt:")
            print("1. Tiparire toate apartamentele care au cheltuieli mai mari decât o suma data")
            print("2. Tiparire cheltuieli de un anumit tip de la toate apartamentele")
            print("3. Tiparire toate cheltuielile efectuate inainte de o zi si mai mari decat o suma")
            subopt = int(input("Optiunea dumneavoastra de cautari este:"))
            if subopt == 1:
                val = int(input("Introduceti suma cu care doriti sa comparati cheltuielile: "))
                afis_cheltuieli_mai_mari_suma(aps, val)
            elif subopt == 2:
                print("Cheltuielile care pot fi afisate sunt: apa, canal, incalzire, gaz, altele.")
                cmd = input("Cheltuiala pe care doriti sa o afisati este: ")
                afis_un_tip_de_cheltuiala(aps, cmd)
            elif subopt == 3:
                val = int(input("Introduceti suma cu care doriti sa comparati cheltuielile: "))
                data = int(input("Introduceti data: "))
                afis_cheltuieli_mai_mari_suma_ziua(aps, val, data)

        elif option==4: #rapoarte
            print("Optiunile de rapoarte sunt:")
            print("1. Tiparire suma totala pt un tip de cheltuiala")
            print("2. Tiparire apartamente sortate dupa un tip de cheltuiala")
            print("3. Tipareste totalul de cheltuieli pt un apartament dat")
            subopt = int(input("Optiunea dumneavoastra de rapoarte este:"))
            if subopt == 1:
                print("Cheltuielile care pot fi selectate sunt: apa, canal, incalzire, gaz, altele.")
                cmd = input("Cheltuiala pt care doriti calculati suma este: ")
                suma = suma_totala_pt_un_tip_cheltuiala(aps, cmd)
                print("Suma totala pt ", str(cmd), " este: ", suma)
            elif subopt == 2:
                print("Cheltuielile care pot fi selectate sunt: apa, canal, incalzire, gaz, altele.")
                cmd = input("Cheltuiala dupa care doriti sa sortati apartamentele este: ")
                sortare_dupa_cheltuiala(aps, cmd)
            elif subopt == 3:
                id_ap = int(input("Id-ul apartamentului pt care se calculeaza suma cheltuielilor este: "))
                suma = suma_totala_pt_un_ap(aps, id_ap)
                print("Suma totala pt apartamentul ", str(id_ap), " este: ", suma)

        elif option==5: #filtru
            print("Optiunile de filtru sunt:")
            print("1. Eliminare cheltuieli de un anumit tip")
            print("2. Eliminare cheltuieli mai mici decat o suma data")
            subopt = int(input("Optiunea dumneavoastra de filtru este:"))
            if subopt == 1:
                print("Cheltuielile care pot fi afisate sunt: apa, canal, incalzire, gaz, altele.")
                cmd = input("Cheltuiala pe care doriti sa o afisati este: ")
                sterge_un_tip_de_cheltuiala(aps, cmd)
                print("Cheltuiala a fost stersa de la toate apartamentele cu succes!")
                afis_lista(aps)
            elif subopt == 2:
                val = int(input("Introduceti suma cu care doriti sa comparati cheltuielile: "))
                sterge_cheltuieli_mai_mici(aps, val)
                print("Cheltuielile mai mici au fost sterse cu succes!")
                afis_lista(aps)

        elif option==6: #undo
            undo(aps)
            afis_lista(aps)

        elif option==7: #iesire din aplicatie
            finished=True
        
        else:
            print("Optiunea introdusa nu este valida!")
        """