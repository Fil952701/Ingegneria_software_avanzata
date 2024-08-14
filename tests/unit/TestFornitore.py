import unittest

from fornitore.controller.ControllerFornitore import ControllerFornitore

from fornitore.model.Fornitore import Fornitore


# Classe di test per la sezione fornitore


class TestFornitore(unittest.TestCase):

    def setUp(self):
        self.fornitore = Fornitore(cod_fornitore="TH000", nome="Yamaha", indirizzo="Siemensstr. 22-34, 25462 Rellingen, Germania",
                                   telefono="410133",
                                   partita_iva="8543215395", sito_web="https://it.yamaha.com",
                                   rappresentante="Marco Papini",
                                   data_affiliazione="16/01/2020", stato="P")

        self.Controller_Fornitore = ControllerFornitore(self.fornitore)

    # Test di ControllerFornitore
    def test_set_cod_fornitore(self):
        right_code = "TH000"
        wrong_code = "GHF005"
        try:
            self.Controller_Fornitore.set_cod_fornitore(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Fornitore.set_cod_fornitore(right_code)
        except (Exception,):
            self.fail()

    def test_set_nome(self):
        right_code = "Yamaha"
        wrong_code = "Yamaha34bg4ta"
        try:
            self.Controller_Fornitore.set_nome(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Fornitore.set_nome(right_code)
        except (Exception,):
            self.fail()

    def test_set_indirizzo(self):
        right_code = "Siemensstr. 22-34, 25462 Rellingen, Germania"
        wrong_code = "a"
        try:
            self.Controller_Fornitore.set_indirizzo(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Fornitore.set_indirizzo(right_code)
        except (Exception,):
            self.fail()

    def test_set_partita_iva(self):
        right_code = "8543215395"
        wrong_code = "IT025466G256"
        try:
            self.Controller_Fornitore.set_partita_iva(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Fornitore.set_partita_iva(right_code)
        except (Exception,):
            self.fail()

    def test_set_telefono(self):
        right_code = "410133"
        wrong_code = "5624866a"
        try:
            self.Controller_Fornitore.set_telefono(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Fornitore.set_telefono(right_code)
        except (Exception,):
            self.fail()

    def test_set_sito_web(self):
        right_code = "https://it.yamaha.com"
        wrong_code = "https://www.kawaipianos.it"
        try:
            self.Controller_Fornitore.set_sito_web(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Fornitore.set_sito_web(right_code)
        except (Exception,):
            self.fail()

    def test_set_data_affiliazione(self):
        right_code = "16/01/2020"
        wrong_code = "2067-12-01"
        try:
            self.Controller_Fornitore.set_data_affiliazione(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Fornitore.set_data_affiliazione(right_code)
        except (Exception,):
            self.fail()

    def test_set_stato(self):
        right_code = "P"
        wrong_code = "S"
        try:
            self.Controller_Fornitore.set_stato(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Fornitore.set_stato(right_code)
        except (Exception,):
            self.fail()

if __name__ == '__main__':
    unittest.main()
