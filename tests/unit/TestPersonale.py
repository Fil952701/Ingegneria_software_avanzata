import unittest

from utente.controller.ControllerUtente import ControllerUtente

from utente.model.Utente import Utente


# classe di test della sezione del personale


class TestPersonale(unittest.TestCase):

    def setUp(self):
        self.utente = Utente(cod_utente=1, nome="Filippo", cognome="Matteini", data_nascita="27/01/1995",
                                   luogo_nascita="San Marino", cf="MTTFPP95A27Z130T",
                                   data_inizio_contratto="30/10/2020", data_scadenza_contratto= None, ruolo="A",
                                   indirizzo="Via Ca Riccio, 32", telefono="3318494191",
                                    stipendio=None, username="fil95", password="outfield85")

        self.Controller_Utente = ControllerUtente(self.utente)

    # Test di ControllerFornitore
    def test_set_cod_utente(self):
        right_code = "1"
        wrong_code = "C1"
        try:
            self.Controller_Utente.set_cod_utente(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Utente.set_cod_utente(right_code)
        except (Exception,):
            self.fail()

    def test_set_nome(self):
        right_code = "Filippo"
        wrong_code = "Filippo35j4jtr"
        try:
            self.Controller_Utente.set_nome(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Utente.set_nome(right_code)
        except (Exception,):
            self.fail()

    def test_set_cognome(self):
        right_code = "Matteini"
        wrong_code = "Matteini35j4jtr"
        try:
            self.Controller_Utente.set_cognome(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Utente.set_cognome(right_code)
        except (Exception,):
            self.fail()

    def test_set_data_nascita(self):
        right_code = "27/01/1995"
        wrong_code = "1995-01-27"
        try:
            self.Controller_Utente.set_data_nascita(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Utente.set_data_nascita(right_code)
        except (Exception,):
            self.fail()

    def test_set_luogo_nascita(self):
        right_code = "San Marino"
        wrong_code = "Avellino"
        try:
            self.Controller_Utente.set_luogo_nascita(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Utente.set_luogo_nascita(right_code)
        except (Exception,):
            self.fail()

    def test_set_cf(self):
        right_code = "MTTFPP95A27Z130T"
        wrong_code = "UTRP29294ZD10304"
        try:
            self.Controller_Utente.set_cf(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Utente.set_cf(right_code)
        except (Exception,):
            self.fail()

    def test_set_data_inizio_contratto(self):
        right_code = "30/10/2023"
        wrong_code = "2023-10-24"
        try:
            self.Controller_Utente.set_data_inizio_contratto(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Utente.set_data_inizio_contratto(right_code)
        except (Exception,):
            self.fail()

    def test_set_data_scadenza_contratto(self):
        right_code = "15/10/2023"
        wrong_code = "2023-10-15"
        try:
            self.Controller_Utente.set_data_scadenza_contratto(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Utente.set_data_scadenza_contratto(right_code)
        except (Exception,):
            self.fail()

    def test_set_ruolo(self):
        right_code = "A"
        wrong_code = "P"
        try:
            self.Controller_Utente.set_ruolo(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Utente.set_ruolo(right_code)
        except (Exception,):
            self.fail()

    def test_set_telefono(self):
        right_code = "3318494191"
        wrong_code = "331r8494Afs191"
        try:
            self.Controller_Utente.set_telefono(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Utente.set_telefono(right_code)
        except (Exception,):
            self.fail()

    def test_set_stipendio(self):
        right_code = "1500"
        wrong_code = "a500d"
        try:
            self.Controller_Utente.set_stipendio(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Utente.set_stipendio(right_code)
        except (Exception,):
            self.fail()

if __name__ == '__main__':
    unittest.main()
