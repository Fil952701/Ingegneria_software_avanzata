import os
import unittest

from listadelpersonale.controller.ControllerListaDelPersonale import ControllerListaDelPersonale
from listadelpersonale.model.ListaDelPersonale import ListaDelPersonale
from utente.model.Utente import Utente
from utente.controller.ControllerUtente import ControllerUtente

from listafornitori.controller.ControllerListaFornitori import ControllerListaFornitori
from fornitore.model.Fornitore import Fornitore
from fornitore.controller.ControllerFornitore import ControllerFornitore

from listaordini.controller.ControllerListaOrdini import ControllerListaOrdini
from ordine.model.Ordine import Ordine
from ordine.controller.ControllerOrdine import ControllerOrdine

from listaprodotti.controller.ControllerListaProdotti import ControllerListaProdotti
from prodotto.model.Prodotto import Prodotto
from prodotto.controller.ControllerProdotto import ControllerProdotto

from faker import Faker
import random
import datetime
import radar


#  Classe di test per la sezione integration


class TestIntegration_ultimo(unittest.TestCase):

    def setUp(self):
        #setup listadelpersonale e utente
        self.controller_lista_del_personale= ControllerListaDelPersonale()
        self.utente_test = Utente(1, "Filippo", "Matteini", "27/01/1995", "San Marino", "MTTFPP95A27Z130T", "30/10/2020", None, "A", "Via Ca Riccio, 32", 3318494191, None, "fil95", "outfield85")
        

        self.controller_utente= ControllerUtente(self.utente_test)

        #setup listafornitori e fornitore
        self.controller_lista_fornitori= ControllerListaFornitori()
        self.fornitore_test = Fornitore("TH000", "Yamaha", "Siemensstr. 22-34, 25462 Rellingen, Germania", 410133, 8543215395, "https://it.yamaha.com", "Marco Papini", "16/01/2020", "P")
        self.controller_fornitore= ControllerFornitore(self.fornitore_test)

        #setup listaordini e ordine
        self.controller_lista_ordini= ControllerListaOrdini()
        self.ordine_test = Ordine(100, "TH000", "In negozio", "2023-01-07", "2023-01-15", "2023-01-15", 539325, 53)
        self.controller_ordine= ControllerOrdine(self.ordine_test)

        #setup listaprodotti e prodotto
        self.controller_lista_prodotti= ControllerListaProdotti()
        self.prodotto_test = Prodotto(100, "TH000", "07/01/2023", "S01", "Yamaha", "C3", "Cordofoni", "Pianoforti acustici", "Legno", "Nero", 2, 20500, 30500, "Venduto", 430, 500, "15/02/2023")
        self.controller_prodotto= ControllerProdotto(self.prodotto_test)

        self.fake_data= Faker()
        Faker.seed(0)
    
    def tearDown(self):

        # finiti i test è necessario riprisitinare il database eliminando i pickle e riprendendo i file da json
        
        if os.path.isfile('listadelpersonale/data/DatabaseDelPersonale.pickle'):
            os.remove('listadelpersonale/data/DatabaseDelPersonale.pickle')

        if os.path.isfile('listafornitori/data/DatabaseFornitori.pickle'):
            os.remove('listafornitori/data/DatabaseFornitori.pickle')

        if os.path.isfile('listaordini/data/DatabaseOrdini.pickle'):
            os.remove('listaordini/data/DatabaseOrdini.pickle')

        if os.path.isfile('listaprodotti/data/DatabaseProdotti.pickle'):
            os.remove('listaprodotti/data/DatabaseProdotti.pickle')

        self.controller_lista_del_personale= ControllerListaDelPersonale()
        self.controller_lista_fornitori= ControllerListaFornitori()
        self.controller_lista_ordini= ControllerListaOrdini()
        self.controller_lista_prodotti= ControllerListaProdotti()

        self.controller_lista_del_personale.refresh_data()
        self.controller_lista_del_personale.save_data()
        self.controller_lista_fornitori.refresh_data()
        self.controller_lista_fornitori.save_data()
        self.controller_lista_ordini.refresh_data()
        self.controller_lista_ordini.save_data()
        self.controller_lista_prodotti.refresh_data()
        self.controller_lista_prodotti.save_data()
        

    # Test modulo della lista del personale e utente


    def test_listadelpersonale(self):
        
        lista_del_personale = self.controller_lista_del_personale.get_lista_del_personale()

        #inserimento di un utente
        lista_t0= len(lista_del_personale)

        for i in range(50):
            print("Utente "+str(i+1)+"\n")
            id= random.randint(100, 9999)
            #print(id)
            name= self.fake_data.first_name()
            #print(name)
            surname= self.fake_data.last_name()
            #print(surname)
            data_nascita= datetime.date(random.randint(1965, 2000), random.randint(1,12), random.randint(1,28))
            data_nascita_split= str(data_nascita).split("-")
            data_nascita= data_nascita_split[2]+"/"+data_nascita_split[1]+"/"+data_nascita_split[0]
            #print(data_nascita)
            city= self.fake_data.city()
            #print(city)
            CF= self.fake_data.ssn()
            #print(CF)
            data_inizio_lavoro= datetime.date(year= random.randint(int(data_nascita_split[0])+18, 2021), month= random.randint(1, 12), day= random.randint(1, 28))
            data_inizio_lavoro_split= str(data_inizio_lavoro).split("-")
            data_inizio_lavoro= data_inizio_lavoro_split[2]+"/"+data_inizio_lavoro_split[1]+"/"+data_inizio_lavoro_split[0]
            #print(str(data_inizio_lavoro))
            data_scadenza_lavoro= datetime.date(year= random.randint(int(data_inizio_lavoro_split[0])+1, int(data_inizio_lavoro_split[0])+5), month= random.randint(1, 12), day= random.randint(1, 28))
            data_scadenza_lavoro_split= str(data_scadenza_lavoro).split("-")
            data_scadenza_lavoro= data_scadenza_lavoro_split[2]+"/"+data_scadenza_lavoro_split[1]+"/"+data_scadenza_lavoro_split[0]
            #print(data_scadenza_lavoro)
            address= self.fake_data.address()
            #print(address)
            tipo_list= ["A", "D"]
            tipo= random.choice(tipo_list)
            #print(tipo)
            phone_number= self.fake_data.phone_number()
            #print(phone_number)
            salary= random.randint(500, 2500)
            #print(salary)
            username= self.fake_data.name()
            #print(username)
            password= self.fake_data.password()
            #print(password)
            if tipo == "D":
                utente_test= Utente(id, name, surname, data_nascita, city, CF, data_inizio_lavoro, data_scadenza_lavoro, tipo,address, phone_number, salary, None, None )
            if tipo == "A":
                utente_test= Utente(id, name, surname, data_nascita, city, CF, data_inizio_lavoro, data_scadenza_lavoro_split, tipo,address, phone_number, salary, username, password)
            self.controller_lista_del_personale.inserisci_utente(self.utente_test)
            self.assertTrue(self.utente_test in lista_del_personale)

        lista_del_personale = self.controller_lista_del_personale.get_lista_del_personale()
        lista_t1= len(lista_del_personale)
        self.assertTrue(lista_t1==lista_t0+50)
 

        #modifica di un utente
        controller_utente= ControllerUtente(utente_test)
        for i in range(50):
            print(i)

            id= random.randint(100, 9999)
            controller_utente.set_cod_utente(str(id))
            self.assertTrue(controller_utente.get_cod_utente() == str(id))

            name= self.fake_data.first_name()
            controller_utente.set_nome(name)
            self.assertTrue(controller_utente.get_nome() == name)

            surname= self.fake_data.last_name()
            controller_utente.set_cognome(surname)
            self.assertTrue(controller_utente.get_cognome() == surname)

            flag = True
            while flag:
                city= self.fake_data.city()
                if city.isalpha():
                    flag=False
            controller_utente.set_luogo_nascita(city)
            self.assertTrue(controller_utente.get_luogo_nascita() == city)

            CF= self.fake_data.ssn()
            CF= CF+"11111"
            controller_utente.set_cf(CF)
            self.assertTrue(controller_utente.get_cf() == CF)

            phone_number= random.randint(300000000, 3999999999)
            print(phone_number)
            controller_utente.set_telefono(str(phone_number))
            self.assertTrue(controller_utente.get_telefono() == str(phone_number))

            salary= random.randint(500, 2500)
            controller_utente.set_stipendio(str(salary))
            self.assertTrue(controller_utente.get_stipendio() == str(salary))

            data_nascita= datetime.date(random.randint(1965, 2000), random.randint(1,12), random.randint(1,28))
            data_nascita_split= str(data_nascita).split("-")
            data_nascita= data_nascita_split[2]+"/"+data_nascita_split[1]+"/"+data_nascita_split[0]
            self.assertFalse(self.controller_utente.get_data_nascita() == data_nascita)
            self.controller_utente.set_data_nascita(data_nascita)
            self.assertTrue(self.controller_utente.get_data_nascita() == data_nascita)

            data_inizio_lavoro= datetime.date(year= random.randint(int(data_nascita_split[0])+18, 2021), month= random.randint(1, 12), day= random.randint(1, 28))
            data_inizio_lavoro_split= str(data_inizio_lavoro).split("-")
            data_inizio_lavoro= data_inizio_lavoro_split[2]+"/"+data_inizio_lavoro_split[1]+"/"+data_inizio_lavoro_split[0]
            self.assertFalse(self.controller_utente.get_data_inizio_contratto() == data_inizio_lavoro)
            self.controller_utente.set_data_inizio_contratto(data_inizio_lavoro)
            self.assertTrue(self.controller_utente.get_data_inizio_contratto() == data_inizio_lavoro)

            data_scadenza_lavoro= datetime.date(year= random.randint(int(data_inizio_lavoro_split[0])+1, int(data_inizio_lavoro_split[0])+5), month= random.randint(1, 12), day= random.randint(1, 28))
            data_scadenza_lavoro_split= str(data_scadenza_lavoro).split("-")
            data_scadenza_lavoro= data_scadenza_lavoro_split[2]+"/"+data_scadenza_lavoro_split[1]+"/"+data_scadenza_lavoro_split[0]
            self.assertFalse(self.controller_utente.get_data_scadenza_contratto() == data_scadenza_lavoro)
            self.controller_utente.set_data_scadenza_contratto(data_scadenza_lavoro)
            self.assertTrue(self.controller_utente.get_data_scadenza_contratto() == data_scadenza_lavoro)

            address= self.fake_data.address()
            self.assertFalse(self.controller_utente.get_indirizzo() == address)
            self.controller_utente.set_indirizzo(address)
            self.assertTrue(self.controller_utente.get_indirizzo() == address)

        #refresh e salvataggio della lista
        #testo che se non salvo, con il refresh perdo le ultime modifiche
        self.controller_lista_del_personale.refresh_data()
        lista_del_personale = self.controller_lista_del_personale.get_lista_del_personale()
        self.assertTrue(self.utente_test not in lista_del_personale)
        #reinserisco l'utente
        self.controller_lista_del_personale.inserisci_utente(self.utente_test)
        self.controller_lista_del_personale.save_data()
        self.controller_lista_del_personale.refresh_data()
        self.assertTrue(self.utente_test in lista_del_personale)

        #eliminazione di un utente
        ultimo_utente = lista_del_personale[-1]
        self.controller_lista_del_personale.elimina_utente(ultimo_utente)
        lista_del_personale= self.controller_lista_del_personale.get_lista_del_personale()
        self.assertTrue(ultimo_utente not in lista_del_personale) 

    
    # Test modulo listafornitori e fornitore


    def test_listafornitori(self):
        
        lista_fornitori = self.controller_lista_fornitori.get_lista_fornitori()

        #inserimento di un fornitore
        lista_t0= len(lista_fornitori)
        
        self.controller_lista_fornitori.inserisci_fornitore(self.fornitore_test)
        lista_fornitori = self.controller_lista_fornitori.get_lista_fornitori()
        lista_t1= len(lista_fornitori)
        self.assertTrue(lista_t1==lista_t0+1)
        self.assertTrue(self.fornitore_test in lista_fornitori)

        #modifica di un fornitore
        self.assertFalse(self.controller_fornitore.get_nome() == "Yamaha")
        self.controller_fornitore.set_nome("Yamaha")
        self.assertTrue(self.controller_fornitore.get_nome() == "Yamaha")

        #refresh e salvataggio della lista
        #testo che se non salvo, con il refresh perdo le ultime modifiche
        self.controller_lista_fornitori.refresh_data()
        lista_fornitori = self.controller_lista_fornitori.get_lista_fornitori()
        self.assertTrue(self.fornitore_test not in lista_fornitori)
        #reinserisco il fornitore
        self.controller_lista_fornitori.inserisci_fornitore(self.fornitore_test)
        self.controller_lista_fornitori.save_data()
        self.controller_lista_fornitori.refresh_data()
        self.assertTrue(self.fornitore_test in lista_fornitori)

        #eliminazione di un fornitore
        ultimo_fornitore = lista_fornitori[-1]
        self.controller_lista_fornitori.elimina_fornitore(ultimo_fornitore)
        lista_fornitori= self.controller_lista_fornitori.get_lista_fornitori()
        self.assertTrue(ultimo_fornitore not in lista_fornitori) 


    # Test modulo e lista ordini


    def test_listaordini(self):
        
        lista_ordini = self.controller_lista_ordini.get_lista_ordini()

        #inserimento di un ordine
        lista_t0= len(lista_ordini)
        
        self.controller_lista_ordini.inserisci_ordine(self.ordine_test)
        lista_ordini= self.controller_lista_ordini.get_lista_ordini()
        lista_t1= len(lista_ordini)
        self.assertTrue(lista_t1==lista_t0+1)
        self.assertTrue(self.ordine_test in lista_ordini)

        #modifica di un ordine
        self.assertFalse(self.controller_ordine.get_cod_fattura() == "100")
        self.controller_ordine.set_cod_fattura("100")
        self.assertTrue(self.controller_ordine.get_cod_fattura() == "100")

        #refresh e salvataggio della lista
        #testo che se non salvo, con il refresh perdo le ultime modifiche
        self.controller_lista_ordini.refresh_data()
        lista_ordini= self.controller_lista_ordini.get_lista_ordini()
        self.assertTrue(self.ordine_test not in lista_ordini)
        #reinserisco l'ordine
        self.controller_lista_ordini.inserisci_ordine(self.ordine_test)
        self.controller_lista_ordini.save_data()
        self.controller_lista_ordini.refresh_data()
        self.assertTrue(self.ordine_test in lista_ordini)

        #eliminazione di un fornitore
        ultimo_ordine = lista_ordini[-1]
        self.controller_lista_ordini.elimina_ordine(ultimo_ordine)
        lista_ordini= self.controller_lista_ordini.get_lista_ordini()
        self.assertTrue(ultimo_ordine not in lista_ordini) 


    # Test moduli listaprodotti e prodotto


    def test_listaprodotti(self):
        
        lista_prodotti = self.controller_lista_prodotti.get_lista_prodotti()

        #inserimento di un prodotto
        lista_t0= len(lista_prodotti)
        
        self.controller_lista_prodotti.inserisci_prodotto(self.prodotto_test)
        lista_prodotti= self.controller_lista_prodotti.get_lista_prodotti()
        lista_t1= len(lista_prodotti)
        self.assertTrue(lista_t1==lista_t0+1)
        self.assertTrue(self.prodotto_test in lista_prodotti)

        #modifica di un prodotto
        self.assertFalse(self.controller_prodotto.get_nome() == "C3")
        self.controller_prodotto.set_nome("C3")
        self.assertTrue(self.controller_prodotto.get_nome() == "C3")

        #refresh e salvataggio della lista
        #testo che se non salvo, con il refresh perdo le ultime modifiche
        self.controller_lista_ordini.refresh_data()
        lista_ordini= self.controller_lista_ordini.get_lista_ordini()
        self.assertTrue(self.ordine_test not in lista_ordini)
        #reinserisco il prodotto
        self.controller_lista_prodotti.inserisci_prodotto(self.prodotto_test)
        self.controller_lista_prodotti.save_data()
        self.controller_lista_prodotti.refresh_data()
        self.assertTrue(self.prodotto_test in lista_prodotti)

        #eliminazione di un prodotto
        ultimo_prodotto = lista_prodotti[-1]
        self.controller_lista_prodotti.elimina_prodotto(ultimo_prodotto)
        lista_prodotti= self.controller_lista_prodotti.get_lista_prodotti()
        self.assertTrue(ultimo_prodotto not in lista_prodotti) 



if __name__ == '__main__':
    unittest.main()