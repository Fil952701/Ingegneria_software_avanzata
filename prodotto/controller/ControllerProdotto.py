from datetime import datetime

# Metodi per andare a gestire le azioni da eseguire sui prodotti

# Metodi per effettuare get

class ControllerProdotto:
    def __init__(self, prodotto):
        self.model = prodotto

    def get_cod_fattura(self):
        return self.model.cod_fattura

    def get_cod_fornitore(self):
        return self.model.cod_fornitore

    def get_data_ordine(self):
        return self.model.data_ordine

    def get_cod_prodotto(self):
        return self.model.cod_prodotto

    def get_tipologia(self):
        if self.model.tipologia == "PA":
            return "Pianoforti acustici"
        elif self.model.tipologia == "PD":
            return "Pianoforti digitali"
        elif self.model.tipologia == "CE":
            return "Chitarre elettriche"
        elif self.model.tipologia == "CA":
            return "Chitarre acustiche"
        elif self.model.tipologia == "VI":
            return "Violini"
        elif self.model.tipologia == "VE":
            return "Viole"
        elif self.model.tipologia == "VC":
            return "Violoncelli"
        elif self.model.tipologia == "BS":
            return "Bassi"
        elif self.model.tipologia == "XL":
            return "Xilofoni"
        elif self.model.tipologia == "MC":
            return "Maracas"
        elif self.model.tipologia == "BT":
            return "Batterie"
        elif self.model.tipologia == "FT":
            return "Flauti"
        elif self.model.tipologia == "FA":
            return "Fiati ad ancia"
        elif self.model.tipologia == "OT":
            return "Ottoni"
        elif self.model.tipologia == "OG":
            return "Organi"
        elif self.model.tipologia == "AR":
            return "Armoniche"
        elif self.model.tipologia == "ST":
            return "Sintetizzatori"

    def get_nome(self):
        return self.model.nome

    def get_stato(self):
        return self.model.stato

    # Metodi per effettuare set

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

    def set_cod_prodotto(self, cod_prodotto):
        if cod_prodotto.startswith("S") and cod_prodotto.isalnum():
            self.model.cod_prodotto = cod_prodotto
        else: 
            raise Exception()

    def set_data_ordine(self, data_ordine):
        if datetime.strptime(data_ordine, "%d/%m/%Y"):
            self.model.data_ordine = data_ordine
        else:
            raise Exception()

    def set_nome(self, nome):
        self.model.nome = nome

    def set_stato(self, stato):
        if stato == "In negozio" or stato == "In arrivo":
            self.model.stato = stato
        else:
            raise Exception()

