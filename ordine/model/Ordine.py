class Ordine:
    def __init__(self, cod_fattura, cod_fornitore, stato, data_ordine,
                 data_arrivo_prevista, data_arrivo_effettiva, importo_totale, strumenti_totali):
        super(Ordine, self).__init__()
        self.cod_fattura = cod_fattura  # str
        self.cod_fornitore = cod_fornitore  # int
        self.stato = stato  # str
        self.data_ordine = data_ordine  # str
        self.data_arrivo_prevista = data_arrivo_prevista  # float
        self.data_arrivo_effettiva= data_arrivo_effettiva
        self.importo_totale= importo_totale
        self.strumenti_totali= strumenti_totali



