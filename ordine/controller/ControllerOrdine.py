from datetime import datetime


class ControllerOrdine:
    def __init__(self, ordine):
        self.model = ordine

    # Metodi per estrarre dati

    def get_cod_fattura(self):
        return self.model.cod_fattura

    def get_cod_fornitore(self):
        return self.model.cod_fornitore

    def get_data_ordine(self):
        if self.model.data_ordine is None:
            return "0000-00-00"
        else:
            return self.model.data_ordine

    def get_data_arrivo_prevista(self):
        if self.model.data_arrivo_prevista is None:
            return "9999-12-31"
        else:
            return self.model.data_arrivo_prevista

    def get_data_arrivo_effettiva(self):
        if self.model.data_arrivo_effettiva is None:
            return "9999-12-31"
        else:
            return self.model.data_arrivo_effettiva

    def get_stato(self):
        return self.model.stato


    # Metodi per settare dati

    def set_cod_fattura(self, cod_fattura):
        if len(cod_fattura) > 2 and cod_fattura.isdecimal():
            self.model.cod_fattura = cod_fattura
        else:
            raise Exception()

    def set_cod_fornitore(self, cod_fornitore):
        if cod_fornitore.startswith("AD") and cod_fornitore.isalnum() and len(cod_fornitore) < 6:
            self.model.cod_fornitore = cod_fornitore
        else:
            raise Exception()

    def set_data_ordine(self, data_ordine):
        if datetime.strptime(data_ordine, "%Y-%m-%d"):
            self.model.data_ordine = data_ordine
        else:
            raise Exception()

    def set_data_arrivo_prevista(self, data_arrio_prevista):
        if datetime.strptime(data_arrio_prevista, "%Y-%m-%d"):
            self.model.data_arrivo_prevista = data_arrio_prevista
        else:
            raise Exception()

    def set_data_arrivo_effettiva(self, data_arrio_effettiva):
        if datetime.strptime(data_arrio_effettiva, "%Y-%m-%d"):
            self.model.data_arrivo_effettiva = data_arrio_effettiva
        else:
            raise Exception()

    def set_stato(self, stato):
        if stato == "In negozio" or stato == "In arrivo":
            self.model.stato = stato
        else:
            raise Exception()