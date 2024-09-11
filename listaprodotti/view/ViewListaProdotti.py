from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QMessageBox, QApplication

from listaordini.controller.ControllerListaOrdini import ControllerListaOrdini
from listaprodotti.controller.ControllerListaProdotti import ControllerListaProdotti
from listaprodotti.view.ViewInserisciProdotto import ViewInserisciProdotto
from listaprodotti.view.ViewDisplayProdotto import ViewDisplayProdotto


# Visualizzazione del catalogo dei prodotti con la possibilità di effettuare filtraggio


class ViewListaProdotti(QWidget):
    def __init__(self, parent=None):
        super(ViewListaProdotti, self).__init__(parent)
        self.controller_lista_ordini = ControllerListaOrdini()
        self.controller_lista_prodotti = ControllerListaProdotti()
        self.lista_prodotti = self.controller_lista_prodotti.get_lista_prodotti()
        self.lista_prodotti_filtrata = self.lista_prodotti[:]
        self.lista_prodotti_cercati = []
        self.cerca_flag = False
        self.setWindowTitle("Catologo Prodotti")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listaprodotti/data/images/logo_mini.jpg'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        #self.setStyleSheet("background-image: url('immagini_home/data/musica.jpg');")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        # gestione Font
        font = QtGui.QFont()
        font.setBold(True)
        font.setPixelSize(20)
        font.setWeight(75)


    # Parte Statica
    
    
        # Top Widget
        self.topWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topWidget.sizePolicy().hasHeightForWidth())
        self.topWidget.setSizePolicy(sizePolicy)
        self.topWidget.setMinimumSize(QtCore.QSize(0, 80))
        self.topWidget.setObjectName("topWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.topWidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        # gestione del logo
        self.logo = QLabel(self.topWidget)
        pixmap = QPixmap('listaprodotti/data/images/logo_mini2.jpg')
        self.logo.setPixmap(pixmap)
        self.logo.resize(100, 100)
        self.gridLayout_3.addWidget(self.logo, 0, 6, 1, 1, QtCore.Qt.AlignHCenter)
        # ricerca elemento
        self.cerca = QtWidgets.QLineEdit(self.topWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cerca.sizePolicy().hasHeightForWidth())
        self.cerca.setSizePolicy(sizePolicy)
        self.cerca.setMinimumSize(QtCore.QSize(250, 0))
        self.cerca.setObjectName("cerca")
        self.cerca.setPlaceholderText("Cerca per codice prodotto")
        self.cerca.setClearButtonEnabled(False)
        self.gridLayout_3.addWidget(self.cerca, 0, 10, 1, 1)
        self.cerca.setStyleSheet("QLineEdit {\n"
                                  "   border-width: 2px;\n"
                                  "   border-radius: 10px;\n"
                                  "   border: 2px solid gray;\n"
                                  "   font: 12px;\n"
                                  "   padding: 6px;\n"
                                  "}")
        self.cerca.returnPressed.connect(self.cerca_prodotto)
        # inserimento prodotto
        self.inserisci_button = QtWidgets.QPushButton(self.topWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inserisci_button.sizePolicy().hasHeightForWidth())
        self.inserisci_button.setSizePolicy(sizePolicy)
        self.inserisci_button.setObjectName("inserisci_button")
        self.inserisci_button.setStyleSheet("QPushButton {\n"
                                        "   background-color:rgb(26, 218, 108);\n"
                                        "   border-width: 2px;\n"
                                        "   border-radius: 10px;\n"
                                        "   font: bold 12px;\n"
                                        "   padding: 6px;\n"
                                        "   color: black;\n"
                                        "}")
        self.gridLayout_3.addWidget(self.inserisci_button, 0, 9, 1, 1)
        self.inserisci_button.clicked.connect(self.show_inserisci_prodotto)

        # filtraggio Combobox per
        # tipologia 
        self.tipologia = QtWidgets.QComboBox(self.topWidget)
        self.tipologia.setObjectName("tipologia")
        self.tipologia.addItem("Pianoforti acustici")
        self.tipologia.addItem("Pianoforti digitali")
        self.tipologia.addItem("Chitarre elettriche")
        self.tipologia.addItem("Chitarre acustiche")
        self.tipologia.addItem("Violini")
        self.tipologia.addItem("Viole")
        self.tipologia.addItem("Violoncelli")
        self.tipologia.addItem("Bassi")
        self.tipologia.addItem("Xilofoni")
        self.tipologia.addItem("Maracas")
        self.tipologia.addItem("Percussioni")
        self.tipologia.addItem("Flauti")
        self.tipologia.addItem("Fiati ad ancia")
        self.tipologia.addItem("Ottoni")
        self.tipologia.addItem("Organi")
        self.tipologia.addItem("Armoniche")
        self.tipologia.addItem("Sintetizzatori")
        self.gridLayout_3.addWidget(self.tipologia, 3, 6, 1, 1)
        self.tipologia.setStyleSheet("QComboBox {\n"
                                  "   background-color:rgb(255, 255, 255);\n"
                                  "   border-width: 2px;\n"
                                  "   font: 12px;\n"
                                  "   padding: 3px;\n"
                                  "   color: black;\n"
                                  "}")
        self.tipologia.currentIndexChanged.connect(self.filtro_combobox)
        # nome
        self.nome = QtWidgets.QComboBox(self.topWidget)
        self.nome.setObjectName("nome")
        self.nome.addItem("Nome")
        self.nome.addItem("C3")
        self.nome.addItem("B2")
        self.nome.addItem("YAS-875EX")
        self.nome.addItem("A5R-ARE")
        self.nome.addItem("V20G")
        self.nome.addItem("VA7SG")
        self.nome.addItem("VC7SG")
        self.nome.addItem("YTR8445S")
        self.nome.addItem("BBP34")
        self.nome.addItem("TP8300R")
        self.nome.addItem("YV2030MS")
        self.nome.addItem("YV2700G")
        self.nome.addItem("YX35G")
        self.nome.addItem("U1-TA3")
        self.nome.addItem("CFX")
        self.nome.addItem("LL26-ARE")
        self.nome.addItem("LL-TA")
        self.nome.addItem("TRB1005J")
        self.nome.addItem("ATTITUDE LIMITED 3")
        self.nome.addItem("YOB-831")
        self.nome.addItem("YBB-641")
        self.nome.addItem("YCB-861")
        self.nome.addItem("YSS475II")
        self.nome.addItem("YFL997CH")
        self.nome.addItem("YFL817")
        self.nome.addItem("Live Custom Hybrid Oak")
        self.nome.addItem("YM1430")
        self.nome.addItem("CTX700")
        self.nome.addItem("WK7600")
        self.nome.addItem("Celviano AP750")
        self.nome.addItem("Tastiera Mini SA76")
        self.nome.addItem("Privia PX870BN")
        self.nome.addItem("Spirio D274")
        self.nome.addItem("K132")
        self.nome.addItem("Spirio R")
        self.nome.addItem("Black Masterpiece")
        self.nome.addItem("Model A Salon Grand Piano")
        self.nome.addItem("Model O Living Room Grand Piano")
        self.nome.addItem("Model M Medium Grand Piano")
        self.nome.addItem("Model S Baby Grand Piano")
        self.nome.addItem("VAD706")
        self.nome.addItem("TD07KX")
        self.nome.addItem("Aerophone Pro")
        self.nome.addItem("Jupiter X")
        self.nome.addItem("Sampling Pad SX Pro")
        self.nome.addItem("F107")
        self.nome.addItem("FP90X")
        self.nome.addItem("Fantom 6 EX")
        self.gridLayout_3.addWidget(self.nome, 3, 8, 1, 1)
        self.nome.setStyleSheet("QComboBox {\n"
                                  "   background-color:rgb(255, 255, 255);\n"
                                  "   border-width: 2px;\n"
                                  "   font: 12px;\n"
                                  "   padding: 3px;\n"
                                  "   color: black;\n"
                                  "}")
        self.nome.currentIndexChanged.connect(self.filtro_combobox)
        # categoria
        self.categoria = QtWidgets.QComboBox(self.topWidget)
        self.categoria.setObjectName("categoria")
        self.categoria.addItems(["Aerofoni", "Cordofoni", "Membranofoni", "Idiofoni", "Elettrofoni"])
        self.gridLayout_3.addWidget(self.categoria, 3, 5, 1, 1)
        self.categoria.setStyleSheet("QComboBox {\n"
                                  "   background-color:rgb(255, 255, 255);\n"
                                  "   border-width: 2px;\n"
                                  "   font: 12px;\n"
                                  "   padding: 3px;\n"
                                  "   color: black;\n"
                                  "}")
        self.categoria.currentIndexChanged.connect(self.filtro_combobox)
        # marca
        self.marca = QtWidgets.QComboBox(self.topWidget)
        self.marca.setObjectName("marca")
        self.marca.addItem("Marca")
        for item in self.controller_lista_prodotti.get_lista_marche():
            self.marca.addItem(str(item))
        self.gridLayout_3.addWidget(self.marca, 3, 4, 1, 1)
        self.marca.setStyleSheet("QComboBox {\n"
                                  "   background-color:rgb(255, 255, 255);\n"
                                  "   border-width: 2px;\n"
                                  "   font: 12px;\n"
                                  "   padding: 3px;\n"
                                  "   color: black;\n"
                                  "}")
        self.marca.currentIndexChanged.connect(self.filtro_combobox)
        # spacer
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 1, 8, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 1, 6, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 7, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 1, 5, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 1, 9, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 1, 10, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem7, 2, 0, 1, 11)
        # in_arrivo button
        self.in_arrivo = QtWidgets.QPushButton(self.topWidget)
        self.in_arrivo.setObjectName("in_arrivo")
        self.in_arrivo.setStyleSheet("QPushButton {\n"
                                            "   background-color:rgb(26, 108, 218);\n"
                                            "   border-width: 2px;\n"
                                            "   border-radius: 10px;\n"
                                            "   font: bold 12px;\n"
                                            "   padding: 6px;\n"
                                            "   color: white;\n"
                                            "}")
        self.gridLayout_3.addWidget(self.in_arrivo, 1, 0, 1, 1)
        self.in_arrivo.clicked.connect(self.show_in_arrivo)
        # in_negozio button
        self.in_negozio = QtWidgets.QPushButton(self.topWidget)
        self.in_negozio.setObjectName("in_negozio")
        self.in_negozio.setStyleSheet("QPushButton {\n"
                                            "   background-color:rgb(26, 108, 218);\n"
                                            "   border-width: 2px;\n"
                                            "   border-radius: 10px;\n"
                                            "   font: bold 12px;\n"
                                            "   padding: 6px;\n"
                                            "   color: white;\n"
                                            "}")
        self.gridLayout_3.addWidget(self.in_negozio, 1, 1, 1, 1)
        self.in_negozio.clicked.connect(self.show_in_negozio)
        # venduto button
        self.venduto = QtWidgets.QPushButton(self.topWidget)
        self.venduto.setObjectName("venduto")
        self.venduto.setStyleSheet("QPushButton {\n"
                                            "   background-color:rgb(218, 108, 26);\n"
                                            "   border-width: 2px;\n"
                                            "   border-radius: 10px;\n"
                                            "   font: bold 12px;\n"
                                            "   padding: 6px;\n"
                                            "   color: black;\n"
                                            "}")
        self.gridLayout_3.addWidget(self.venduto, 1, 2, 1, 1)
        self.venduto.clicked.connect(self.show_venduto)
        # reso button
        self.reso = QtWidgets.QPushButton(self.topWidget)
        self.reso.setObjectName("reso")
        self.reso.setStyleSheet("QPushButton {\n"
                                            "   background-color:rgb(218, 108, 26);\n"
                                            "   border-width: 2px;\n"
                                            "   border-radius: 10px;\n"
                                            "   font: bold 12px;\n"
                                            "   padding: 6px;\n"
                                            "   color: black;\n"
                                            "}")
        self.gridLayout_3.addWidget(self.reso, 1, 3, 1, 1)
        self.reso.clicked.connect(self.show_reso)

        # indietro
        self.indietro = QtWidgets.QPushButton(self.topWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.indietro.sizePolicy().hasHeightForWidth())
        self.indietro.setSizePolicy(sizePolicy)
        self.indietro.setObjectName("indietro")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listaprodotti/data/images/logo_home.jpg'))
        self.indietro.setIcon(icon)
        self.indietro.setIconSize(QSize(50, 50))
        self.indietro.setStyleSheet("QPushButton {\n"
                                "   background-color:white;\n"
                                "   border-width: 2px;\n"
                                "   border-radius: 10px;\n"
                                "   padding: 6px;\n"
                                "}")
        self.gridLayout_3.addWidget(self.indietro, 0, 0, 1, 1)
        self.indietro.clicked.connect(self.close)

        self.verticalLayout.addWidget(self.topWidget)

        # Widget centrale
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1172, 851))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")

        # CREAZIONE DEI WIDGET
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        height = self.screenRect.height()
        width = self.screenRect.width()
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, width, height))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)


   # Parte Dinamica


    def retranslateUi(self):
        for i in reversed(range(self.gridLayout_2.count())):
            self.gridLayout_2.itemAt(i).widget().setParent(None)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Area prodotti"))
        self.tipologia.setItemText(0, _translate("MainWindow", "Tipologia"))
        self.in_arrivo.setText(_translate("MainWindow", "IN ARRIVO"))
        self.categoria.setItemText(0, _translate("MainWindow", "Categoria"))
        self.in_negozio.setText(_translate("MainWindow", "IN NEGOZIO"))
        self.venduto.setText(_translate("MainWindow", "VENDUTO"))
        self.reso.setText(_translate("MainWindow", "RESO"))
        self.inserisci_button.setText(_translate("MainWindow", "Inserisci prodotto"))

        if self.cerca_flag:
            self.display_build(self.lista_prodotti_cercati)
        else:
            self.display_build(self.lista_prodotti_filtrata)


    # Event di click sui vari bottoni


    def show_inserisci_prodotto(self):
        self.view_inserisci_prodotto = ViewInserisciProdotto(self.controller_lista_prodotti, self.retranslateUi,
                                                               False, None, self.lista_prodotti_filtrata, None)
        self.view_inserisci_prodotto.show()
        for i in reversed(range(self.gridLayout_2.count())):
            self.gridLayout_2.itemAt(i).widget().setParent(None)
        self.retranslateUi()

    def cerca_prodotto(self):
        self.lista_prodotti_cercati = self.lista_prodotti_filtrata[:]

        self.cerca_flag = True
        codice_cerca = self.cerca.text()
        codice_cerca = codice_cerca.upper()
        elementi_da_rimuovere = []
        if codice_cerca.isalnum() and codice_cerca.startswith('S'):
            for prodotto in self.lista_prodotti_cercati:
                cod_prodotto= str(prodotto.cod_prodotto)
                cod_prodotto= cod_prodotto.upper()
                if not (codice_cerca in cod_prodotto):
                    elementi_da_rimuovere.append(prodotto)
            for prodotto in elementi_da_rimuovere:
                if prodotto in self.lista_prodotti_cercati:
                    self.lista_prodotti_cercati.remove(prodotto)
            for i in reversed(range(self.gridLayout_2.count())):
                self.gridLayout_2.itemAt(i).widget().setParent(None)
        else:
            self.popup_errore()
        self.retranslateUi()
        self.cerca_flag = False

    # crea l'elenco dei codici dei prodotti da visualizzare basati sui filtri utilizzati
    def filtro_lista(self, IA, IN, V, R):
        filtro_marca = str(self.marca.currentText())
        filtro_categoria = str(self.categoria.currentText())
        filtro_nome = str(self.nome.currentText())
        filtro_tipologia = str(self.tipologia.currentText())
        '''if str(self.tipologia.currentText()) == "Pianoforti acustici":
            filtro_tipologia = "PA"
        elif str(self.tipologia.currentText()) == "Pianoforti digitali":
            filtro_tipologia = "PD"
        elif str(self.tipologia.currentText()) == "Chitarre elettriche":
            filtro_tipologia = "CE"
        elif str(self.tipologia.currentText()) == "Chitarre acustiche":
            filtro_tipologia = "CA"
        elif str(self.tipologia.currentText()) == "Violini":
            filtro_tipologia = "VI"
        elif str(self.tipologia.currentText()) == "Viole":
            filtro_tipologia = "VE"
        elif str(self.tipologia.currentText()) == "Violoncelli":
            filtro_tipologia = "VC"
        elif str(self.tipologia.currentText()) == "Bassi":
            filtro_tipologia = "BS"
        elif str(self.tipologia.currentText()) == "Xilofoni":
            filtro_tipologia = "XL"
        elif str(self.tipologia.currentText()) == "Maracas":
            filtro_tipologia = "MC"
        elif str(self.tipologia.currentText()) == "Percussioni":
            filtro_tipologia = "BT"
        elif str(self.tipologia.currentText()) == "Flauti":
            filtro_tipologia = "FT"
        elif str(self.tipologia.currentText()) == "Fiati ad ancia":
            filtro_tipologia = "FA"
        elif str(self.tipologia.currentText()) == "Ottoni":
            filtro_tipologia = "TB"
        elif str(self.tipologia.currentText()) == "Organi":
            filtro_tipologia = "OG"
        elif str(self.tipologia.currentText()) == "Armoniche":
            filtro_tipologia = "AR"
        elif str(self.tipologia.currentText()) == "Sintetizzatori":
            filtro_tipologia = "ST"
        else:
            filtro_tipologia = "Tipologia"'''

        elementi_da_rimuovere = []
        lista = self.controller_lista_prodotti.get_lista_prodotti()
        self.lista_prodotti_filtrata = lista[:]

        if IA:
            for prodotto in self.lista_prodotti_filtrata:
                if prodotto.stato != "In arrivo":
                    elementi_da_rimuovere.append(prodotto)
            for prodotto in elementi_da_rimuovere:
                self.lista_prodotti_filtrata.remove(prodotto)
            elementi_da_rimuovere.clear()
        if IN:
            for prodotto in self.lista_prodotti_filtrata:
                if prodotto.stato != "In negozio":
                    elementi_da_rimuovere.append(prodotto)
            for prodotto in elementi_da_rimuovere:
                self.lista_prodotti_filtrata.remove(prodotto)
            elementi_da_rimuovere.clear()
        if V:
            for prodotto in self.lista_prodotti_filtrata:
                if prodotto.stato != "Venduto":
                    elementi_da_rimuovere.append(prodotto)
            for prodotto in elementi_da_rimuovere:
                self.lista_prodotti_filtrata.remove(prodotto)
            elementi_da_rimuovere.clear()
        if R:
            for prodotto in self.lista_prodotti_filtrata:
                if prodotto.stato != "Reso":
                    elementi_da_rimuovere.append(prodotto)
            for prodotto in elementi_da_rimuovere:
                self.lista_prodotti_filtrata.remove(prodotto)
            elementi_da_rimuovere.clear()
        if filtro_marca != "Marca":
            for prodotto in self.lista_prodotti_filtrata:
                if str(prodotto.marca) != str(filtro_marca):
                    elementi_da_rimuovere.append(prodotto)
            for prodotto in elementi_da_rimuovere:
                self.lista_prodotti_filtrata.remove(prodotto)
            elementi_da_rimuovere.clear()
        if filtro_categoria != "Categoria":
            for prodotto in self.lista_prodotti_filtrata:
                if str(prodotto.categoria) != str(filtro_categoria):
                    elementi_da_rimuovere.append(prodotto)
            for prodotto in elementi_da_rimuovere:
                self.lista_prodotti_filtrata.remove(prodotto)
            elementi_da_rimuovere.clear()
        if filtro_tipologia != "Tipologia":
            for prodotto in self.lista_prodotti_filtrata:
                if str(prodotto.tipologia) != str(filtro_tipologia):
                    elementi_da_rimuovere.append(prodotto)
            for prodotto in elementi_da_rimuovere:
                self.lista_prodotti_filtrata.remove(prodotto)
            elementi_da_rimuovere.clear()
        if filtro_nome != "Nome":
            for prodotto in self.lista_prodotti_filtrata:
                if str(prodotto.nome) != str(filtro_nome):
                    elementi_da_rimuovere.append(prodotto)
            for prodotto in elementi_da_rimuovere:
                self.lista_prodotti_filtrata.remove(prodotto)
            elementi_da_rimuovere.clear()

        self.retranslateUi()

    def display_build(self, lista_da_caricare):
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        width = self.screenRect.width()

        row = 0
        column = 0
        for prodotto in lista_da_caricare:
            self.widget_generico = QtWidgets.QWidget(self.scrollAreaWidgetContents)
            self.displayprodotto1 = ViewDisplayProdotto(prodotto, self.retranslateUi, self.controller_lista_prodotti, self.lista_prodotti_filtrata)
            self.widget_generico = self.displayprodotto1
            self.widget_generico.setMinimumSize(QtCore.QSize((int(width / 3.2)), 450))

            self.gridLayout_2.addWidget(self.widget_generico, row, column, 1, 1)

            if column == 2:
                row = row + 1
                column = 0
            else:
                column = column + 1

    def show_in_arrivo(self):
        self.filtro_lista(True, False, False, False)

    def show_in_negozio(self):
        self.filtro_lista(False, True, False, False)

    def show_venduto(self):
        self.filtro_lista(False, False, True, False)

    def show_reso(self):
        self.filtro_lista(False, False, False, True)

    def filtro_combobox(self):
        self.filtro_lista(False, False, False, False)

    def popup_errore(self):
        msg = QMessageBox()
        msg.setWindowTitle("WARNING")
        msg.setText("Hai inserito un codice prodotto non valido.\n\nProva con un formato del tipo: S**")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Yes)
        msg.setDefaultButton(QMessageBox.Yes)
        msg.exec_()

    def popup_no_prodotti(self):
        msg = QMessageBox()
        msg.setWindowTitle("WARNING")
        msg.setText("Nessun prodotto corrisponde ai criteri di ricerca. \n\nProva con altri filtri")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Yes)
        msg.setDefaultButton(QMessageBox.Yes)
        msg.exec_()

    def closeEvent(self, event):
        self.controller_lista_ordini.save_data()
        self.controller_lista_prodotti.save_data()
