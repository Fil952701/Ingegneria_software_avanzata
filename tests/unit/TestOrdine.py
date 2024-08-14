import unittest

from ordine.controller.ControllerOrdine import ControllerOrdine

from ordine.model.Ordine import Ordine


# classe di test della sezione dell'ordine


class TestOrdine(unittest.TestCase):

    def setUp(self):
        self.ordine = Ordine(cod_fattura="100", cod_fornitore="TH000", stato="In negozio",
                                   data_ordine="2023-01-07", data_arrivo_prevista="2023-01-15",
                                   data_arrivo_effettiva="2023-01-15",
                                   importo_totale="539325", strumenti_totali="53")

        self.Controller_Ordine = ControllerOrdine(self.ordine)

    # Test di ControllerOrdine
    def test_set_cod_fattura(self):
        right_code = "100"
        wrong_code = "8"
        try:
            self.Controller_Ordine.set_cod_fattura(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Ordine.set_cod_fattura(right_code)
        except (Exception,):
            self.fail()

    def test_set_cod_fornitore(self):
        right_code = "TH000"
        wrong_code = "I0034"
        try:
            self.Controller_Ordine.set_cod_fornitore(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Ordine.set_cod_fornitore(right_code)
        except (Exception,):
            self.fail()

    def test_set_data_ordine(self):
        right_code = "2023-01-07"
        wrong_code = "20-10-2023"
        try:
            self.Controller_Ordine.set_data_ordine(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Ordine.set_data_ordine(right_code)
        except (Exception,):
            self.fail()

    def test_set_data_arrivo_prevista(self):
        right_code = "2023-01-15"
        wrong_code = "15-01-2023"
        try:
            self.Controller_Ordine.set_data_arrivo_prevista(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Ordine.set_data_arrivo_prevista(right_code)
        except (Exception,):
            self.fail()

    def test_set_data_arrivo_effettiva(self):
        right_code = "2023-01-15"
        wrong_code = "15-01-2023"
        try:
            self.Controller_Ordine.set_data_arrivo_effettiva(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Ordine.set_data_arrivo_effettiva(right_code)
        except (Exception,):
            self.fail()

    def test_set_stato(self):
        right_code = "In negozio"
        wrong_code = "in_negozio"
        try:
            self.Controller_Ordine.set_stato(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Ordine.set_stato(right_code)
        except (Exception,):
            self.fail()

if __name__ == '__main__':
    unittest.main()
