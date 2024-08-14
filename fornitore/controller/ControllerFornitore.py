from datetime import datetime


class ControllerFornitore:
    def __init__(self, fornitore):
        self.model = fornitore

    # metodi di recupero dati per il controller fornitore

    def get_cod_fornitore(self):
        return self.model.cod_fornitore

    def get_nome(self):
        return self.model.nome

    def get_indirizzo(self):
        return self.model.indirizzo

    def get_telefono(self):
        return self.model.telefono

    def get_partita_iva(self):
        return self.model.partita_iva

    def get_sito_web(self):
        return self.model.sito_web

    def get_rappresentante(self):
        return self.model.rappresentante

    def get_data_affiliazione(self): 
        if self.model.data_affiliazione is None:
            return "00/00/0000"
        else:
            return self.model.data_affiliazione

    def get_stato(self):
        if self.model.stato == "S":
            return "Standard"
        else:
            return "Premium"

    # metodi di settaggio dati per il controller fornitore

    def set_cod_fornitore(self, codice_fornitore):
        if codice_fornitore.startswith("AD") and codice_fornitore.isalnum() and len(codice_fornitore) < 6:
            self.model.cod_fornitore = codice_fornitore
        else:
            raise Exception()

    def set_nome(self, nome):
        if nome.isalpha():
            self.model.nome = nome
        else:
            raise Exception()

    def set_indirizzo(self, indirizzo):
        if len(indirizzo) > 4:
            self.model.indirizzo = indirizzo
        else:
            raise Exception()

    def set_partita_iva(self, partita_iva):
        if len(partita_iva) == 11 and partita_iva.isdigit():
            self.model.partita_iva = partita_iva
        else:
            raise Exception()

    def set_telefono(self, telefono):
        if len(telefono) == 6 and telefono.isdigit():
            self.model.telefono = telefono
        else:
            raise Exception()

    def set_sito_web(self, sito_web):
        if sito_web.startswith("https://www."):
            self.model.sito_web = sito_web
        else:
            raise Exception()

    def set_rappresentante(self, rappresentante):
            self.model.rappresentante = rappresentante

    def set_data_affiliazione(self, data_affiliazione):
        if datetime.strptime(data_affiliazione, "%d/%m/%Y"):
            self.model.data_affiliazione = data_affiliazione
        else:
            raise Exception()

    def set_stato(self, stato):
        if stato == "Standard" or stato == "Premium":
            if stato == "Standard":
                self.model.stato = "S"
            else:
                self.model.stato = "P"
        else:
            raise Exception()