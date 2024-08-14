import unittest
from prodotto.controller.ControllerProdotto import ControllerProdotto

from prodotto.model.Prodotto import Prodotto


# Classe di test della sezione prodotto


class TestProdotto(unittest.TestCase):

    def setUp(self):
        self.prodotto = Prodotto(cod_fattura=100, cod_fornitore="TH000", data_ordine="07/01/2023", cod_prodotto="S01",
                            marca="Yamaha", nome="C3", categoria="Cordofoni", tipologia="Pianoforti acustici", materiale="Legno",
                            colore="Nero",
                            quantita=2, prezzo_acquisto=20500, prezzo_vendita=30500, stato="Venduto",
                            sconto_consigliato=430, sconto=500, data_vendita="15/02/2023")
        self.Controller_Prodotto = ControllerProdotto(self.prodotto)

    # Test di ControllerProdotto
    def test_set_cod_fattura(self):
        right_code = "100"
        wrong_code = "5"
        try:
            self.Controller_Prodotto.set_cod_fattura(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Prodotto.set_cod_fattura(right_code)
        except (Exception,):
            self.fail()

    def test_set_cod_fornitore(self):
        right_code = "TH000"
        wrong_code = "J23CF"
        try:
            self.Controller_Prodotto.set_cod_fornitore(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Prodotto.set_cod_fornitore(right_code)
        except (Exception,):
            self.fail()

    def test_set_cod_prodotto(self):
        right_code = "S01"
        wrong_code = "P2O4"
        try:
            self.Controller_Prodotto.set_cod_prodotto(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Prodotto.set_cod_prodotto(right_code)
        except (Exception,):
            self.fail()

    def test_set_data_ordine(self):
        right_code = "15/02/2023"
        wrong_code = "10-08-2023"
        try:
            self.Controller_Prodotto.set_data_ordine(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Prodotto.set_data_ordine(right_code)
        except (Exception,):
            self.fail()

    def test_set_stato(self):
        right_code = "In negozio"
        wrong_code = "in_negozio"
        try:
            self.Controller_Prodotto.set_stato(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Prodotto.set_stato(right_code)
        except (Exception,):
            self.fail()

if __name__ == '__main__':
    unittest.main()
            
