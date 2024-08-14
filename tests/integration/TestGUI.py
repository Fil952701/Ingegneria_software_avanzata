from asyncio import subprocess
import pyautogui
import time
import subprocess
import multiprocessing


# TEST da effettuare

# Metodo che esegue il file principale del gestionale
def runProgram():
    subprocess.run(["python3.8", 'main.py'])
21

# metodo che esegue tutti i test di interfaccia
def runTest():
    time.sleep(6)
    test_listaprodotti()
    time.sleep(2)
    test_ordini()
    time.sleep(2)
    test_login()
    time.sleep(2)
    test_listadelpersonale()
    time.sleep(2)
    test_logout()


# Test per effettuare procedura di login


def test_login():
    # coordinate centrali del pulsante login
    login_button_coords = pyautogui.locateCenterOnScreen('immagini_test/login_button.jpg')
    # spostamento sul pulsante login
    #pyautogui.moveTo(login_button_coords.x, login_button_coords.y, 1)
    # click sul login
    pyautogui.click(login_button_coords)
    time.sleep(0.3)
    # coordinate centrali della form username
    user_form_coords = pyautogui.locateCenterOnScreen('immagini_test/user_form.jpg')
    # spostamento sulla form username
    pyautogui.moveTo(user_form_coords.x, user_form_coords.y, 1)
    # click su username
    pyautogui.click(user_form_coords)
    time.sleep(0.3)
    # scrittura dell'username
    pyautogui.write("filippo", 0.3)
    # coordinate centrali della form password
    pass_form_coords = pyautogui.locateCenterOnScreen('immagini_test/pass_form.jpg')
    # spostamento sul campo password
    pyautogui.moveTo(pass_form_coords.x, pass_form_coords.y, 0.5)
    # click su password
    pyautogui.click(pass_form_coords)
    time.sleep(0.3)
    # scrittura password
    pyautogui.write("outfield85", 0.3)

    # coordinate centrali del pulsante accedi
    loginto_button_coords = pyautogui.locateCenterOnScreen('immagini_test/loginto_button.jpg')
    # spostamento sul pulsante di accesso
    pyautogui.moveTo(loginto_button_coords.x, loginto_button_coords.y, 0.5)
    # click su pulsante di accesso per entrare nel gestionale
    pyautogui.click(loginto_button_coords)


# Test sezione ordini


def test_ordini():
    ordini_button_coords = pyautogui.locateCenterOnScreen('immagini_test/ordini.jpg')
    pyautogui.moveTo(ordini_button_coords.x, ordini_button_coords.y, 0.3)
    pyautogui.click(ordini_button_coords)
    time.sleep(0.5)
    nuovo_button_coords = pyautogui.locateCenterOnScreen('immagini_test/nuovo.jpg')
    pyautogui.moveTo(nuovo_button_coords.x, nuovo_button_coords.y, 0.3)
    pyautogui.click(nuovo_button_coords)
    time.sleep(0.5)
    codice_fattura_form= pyautogui.locateCenterOnScreen('immagini_test/codice_fattura_form.jpg')
    pyautogui.moveTo(codice_fattura_form.x, codice_fattura_form.y, 0.3)
    pyautogui.click(codice_fattura_form)
    pyautogui.write("212", 0.1)
    time.sleep(0.3)
    codice_fornitore_form= pyautogui.locateCenterOnScreen('immagini_test/codice_fornitore_form.jpg')
    pyautogui.moveTo(codice_fornitore_form.x, codice_fornitore_form.y, 0.3)
    pyautogui.click(codice_fornitore_form)
    pyautogui.write("1", 0.1)
    inserisci_prodotto_ordini= pyautogui.locateCenterOnScreen('immagini_test/inserisci_prodotto_ordini.jpg')
    pyautogui.moveTo(inserisci_prodotto_ordini.x, inserisci_prodotto_ordini.y, 0.3)
    pyautogui.click(inserisci_prodotto_ordini)
    time.sleep(0.3)
    codice_prodotto_form= pyautogui.locateCenterOnScreen('immagini_test/codice_prodotto_form.jpg')
    pyautogui.moveTo(codice_prodotto_form.x, codice_prodotto_form.y, 0.3)
    pyautogui.click(codice_prodotto_form)
    pyautogui.write("22", 0.1)
    quantita_form= pyautogui.locateCenterOnScreen('immagini_test/quantita.jpg')
    pyautogui.moveTo(quantita_form.x, quantita_form.y, 0.3)
    pyautogui.click(quantita_form)
    pyautogui.write("10", 0.1)
    pyautogui.scroll(-5)
    prezzo_acquisto_form= pyautogui.locateCenterOnScreen('immagini_test/prezzo_acquisto_form.jpg')
    pyautogui.moveTo(prezzo_acquisto_form.x, prezzo_acquisto_form.y, 0.3)
    pyautogui.click(prezzo_acquisto_form)
    pyautogui.write("50", 0.1)
    salva_prodotti= pyautogui.locateCenterOnScreen('immagini_test/salva_prodotti_ordine.jpg')
    time.sleep(0.3)
    pyautogui.moveTo(salva_prodotti.x, salva_prodotti.y, 0.3)
    pyautogui.click(salva_prodotti)
    salva= pyautogui.locateCenterOnScreen('immagini_test/salva.jpg')
    pyautogui.moveTo(salva.x, salva.y, 0.3)
    pyautogui.click(salva)
    time.sleep(0.3)
    in_arrivo= pyautogui.locateCenterOnScreen('immagini_test/In_arrivo.jpg')
    pyautogui.moveTo(in_arrivo.x, in_arrivo.y, 0.3)
    pyautogui.click(in_arrivo)
    ordine_test= pyautogui.locateCenterOnScreen('immagini_test/ordine_test.jpg')
    pyautogui.moveTo(ordine_test.x, ordine_test.y, 0.3)
    pyautogui.click(ordine_test)
    apri= pyautogui.locateCenterOnScreen('immagini_test/apri.jpg')
    pyautogui.moveTo(ordine_test.x, ordine_test.y, 0.3)
    pyautogui.click(apri)
    time.sleep(0.3)
    elimina= pyautogui.locateCenterOnScreen('immagini_test/elimina_ordine.jpg')
    pyautogui.moveTo(elimina.x, elimina.y, 0.3)
    pyautogui.click(elimina)
    time.sleep(0.3)
    yes= pyautogui.locateCenterOnScreen('immagini_test/yes.jpg')
    pyautogui.moveTo(yes.x, yes.y, 0.3)
    pyautogui.click(yes)
    time.sleep(0.3)
    home= pyautogui.locateCenterOnScreen('immagini_test/home.jpg')
    pyautogui.moveTo(home.x, home.y, 0.3)
    pyautogui.click(home)


# Test sezione prodotti


def test_listaprodotti():
    prodotti = pyautogui.locateCenterOnScreen('immagini_test/prodotti.jpg')
    pyautogui.click(prodotti)
    time.sleep(3)
    in_negozio = pyautogui.locateCenterOnScreen('immagini_test/in_negozio_prodotti.jpg')
    pyautogui.click(in_negozio)
    time.sleep(6)
    in_arrivo = pyautogui.locateCenterOnScreen('immagini_test/in_arrivo_prodotti.jpg')
    time.sleep(6)
    pyautogui.click(in_arrivo)
    time.sleep(6)
    home= pyautogui.locateCenterOnScreen('immagini_test/home.jpg')
    pyautogui.moveTo(home.x, home.y, 0.3)
    pyautogui.click(home)


# Test sezione personale


def test_listadelpersonale():
    personale= pyautogui.locateCenterOnScreen('immagini_test/personale.jpg')
    pyautogui.moveTo(personale.x, personale.y, 0.3)
    pyautogui.click(personale)
    time.sleep(0.5)
    utente_test= pyautogui.locateCenterOnScreen('immagini_test/utente_test.jpg')
    pyautogui.moveTo(utente_test.x, utente_test.y, 0.3)
    pyautogui.click(utente_test)
    apri= pyautogui.locateCenterOnScreen('immagini_test/apri.jpg')
    pyautogui.moveTo(apri.x, apri.y, 0.3)
    pyautogui.click(apri)
    time.sleep(0.5)
    modifica_utente= pyautogui.locateCenterOnScreen('immagini_test/modifica_utente.jpg')
    pyautogui.moveTo(modifica_utente.x, modifica_utente.y, 0.3)
    pyautogui.click(modifica_utente)
    time.sleep(0.5)
    annulla_utente= pyautogui.locateCenterOnScreen('immagini_test/annulla_utente.jpg')
    pyautogui.moveTo(annulla_utente.x, annulla_utente.y, 0.3)
    pyautogui.click(annulla_utente)
    time.sleep(0.5)
    yes= pyautogui.locateCenterOnScreen('immagini_test/yes.jpg')
    pyautogui.moveTo(yes.x, yes.y, 0.3)
    pyautogui.click(yes)
    time.sleep(0.5)
    pyautogui.hotkey('alt','f4')
    #f4= pyautogui.locateCenterOnScreen('immagini_test/f4.jpg')
    #pyautogui.moveTo(f4.x, f4.y, 0.3)
    #pyautogui.click(f4)
    time.sleep(0.5)
    home= pyautogui.locateCenterOnScreen('immagini_test/home.jpg')
    pyautogui.moveTo(home.x, home.y, 0.3)
    pyautogui.click(home)


# Test procedura di logout


def test_logout():
    logout= pyautogui.locateCenterOnScreen('immagini_test/logout.jpg')
    pyautogui.moveTo(logout.x, logout.y, 0.3)
    pyautogui.click(logout)
    time.sleep(0.6)
    yes= pyautogui.locateCenterOnScreen('immagini_test/yes2.jpg')
    pyautogui.moveTo(yes.x, yes.y, 0.3)
    pyautogui.click(yes)
    time.sleep(0.5)
    pyautogui.hotkey('alt','f4')
    time.sleep(0.6)
    yes= pyautogui.locateCenterOnScreen('immagini_test/yes3.jpg')
    pyautogui.click(yes)


# Creo due multi-processi
p1 = multiprocessing.Process(target=runProgram)
p2 = multiprocessing.Process(target=runTest)

# Avvio i due processi in parallelo
p1.start()
p2.start()
