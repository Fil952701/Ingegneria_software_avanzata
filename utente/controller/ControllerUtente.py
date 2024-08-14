from datetime import datetime


class ControllerUtente:
    def __init__(self, utente):
        self.model= utente

    ################# GETTER #################

    def get_cod_utente(self):
        return self.model.cod_utente

    def get_nome(self):
        return self.model.nome

    def get_cognome(self):
        return self.model.cognome

    def get_data_nascita(self):
        return self.model.data_nascita

    def get_luogo_nascita(self):
        return self.model.luogo_nascita

    def get_cf(self):
        return self.model.cf

    def get_data_inizio_contratto(self):
        if self.model.data_inizio_contratto is None:
            return "00/00/0000"
        else:
            return self.model.data_inizio_contratto

    def get_data_scadenza_contratto(self):
        if self.model.data_scadenza_contratto is None:
            return "31/12/9999"
        else:
            return self.model.data_scadenza_contratto

    def get_ruolo(self):
        if self.model.ruolo=="D":
            return "Dipendente"
        else:
            return "Amministratore"

    def get_indirizzo(self):
        return self.model.indirizzo

    def get_telefono(self):
        return self.model.telefono

    def get_stipendio(self):
        return  self.model.stipendio

    def get_username(self):
        if self.model.ruolo== "A":
            return self.model.username
        else:
            return None

    def get_password(self):
        if self.model.ruolo== "A":
            return self.model.password
        else:
            return None

    ################# SETTER #################

    def set_cod_utente(self, codice):
        if codice.isdigit():
            self.model.cod_utente= codice
        else:
            raise Exception()

    def set_nome(self, nome):
        if nome.isalpha():
            self.model.nome= nome
        else:
            raise Exception()

    def set_cognome(self, cognome):
        if cognome.isalpha():
            self.model.cognome= cognome
        else:
            raise Exception()

    def set_data_nascita(self, data_nascita):
        if datetime.strptime(data_nascita, "%d/%m/%Y"):
            self.model.data_nascita= data_nascita
        else:
            raise Exception()

    def set_luogo_nascita(self, luogo_nascita):
        if luogo_nascita.isalpha():
            self.model.luogo_nascita= luogo_nascita
        else:
            raise Exception()

    def set_cf(self, cf):
        if len(cf) == 16:
            self.model.cf= cf
        else:
            raise Exception()

    def set_data_inizio_contratto(self, data_inizio_contratto):
        if datetime.strptime(data_inizio_contratto, "%d/%m/%Y"):
            self.model.data_inizio_contratto= data_inizio_contratto
        else:
            raise Exception()

    def set_data_scadenza_contratto(self, data_scadenza_contratto):
        if datetime.strptime(data_scadenza_contratto, "%d/%m/%Y"):
            self.model.data_scadenza_contratto= data_scadenza_contratto
        else:
            raise Exception()

    def set_ruolo(self, ruolo):
        if ruolo=="D" or ruolo=="A":
            if ruolo=="Dipendente":
                self.model.ruolo= "D"
            else:
                self.model.ruolo= "A"
        else:
            raise Exception()

    def set_indirizzo(self, indirizzo):
        self.model.indirizzo= indirizzo

    def set_telefono(self, telefono):
        if telefono.isdigit():
            self.model.telefono= telefono
        else:
            raise Exception()

    def set_stipendio(self, stipendio):
        if stipendio.isdigit() or stipendio is None:
            self.model.stipendio= stipendio
        else:
            raise Exception()

    def set_username(self, username):
        self.model.username= username

    def set_password(self, password):
        self.model.password= password



