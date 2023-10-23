import decimal
class ContoCorrente:  
    def __init__(self, saldoIniziale, proprietario, nConto):
        self.proprietario = proprietario
        self.nConto = nConto
        self.saldoAttuale = self.saldoIniziale
        self.movimenti = []

    def __str__(self):
        return f"\nIl conto N°{self.nConto} appartiene a {self.proprietario}. Ci sono {self.saldoAttuale:.2f}€"

    def effettuaOperazione(self, prelievo):
        while True:
            importo = input("\nInserisci l'importo desiderato: ")
            if importo.strip() == "":
                print("Inserimento errato: devi inserire un importo")
            else:
                errore = False
                try:    
                    importo = int(importo)
                    if importo < 0:
                        print("Inserimento errato: devi inserire un importo numerico > 0")
                        errore = True
                except ValueError:    
                    try:    
                        importo = float(importo)
                        if importo < 0:
                            print("Inserimento errato: devi inserire un importo numerico > 0")
                            errore = True
                    except ValueError: 
                        print("Inserimento errato: devi inserire un importo numerico > 0")
                        errore = True
            if not errore:
                if prelievo:
                    self.prelievo(importo)
                else:
                    self.versamento(importo)
                break
        
    def prelievo(self, importo):
        if (importo <= self.saldoAttuale):
            self.saldoAttuale -= importo
            self.movimenti.append(-importo)
            print("Prelievo effettuato")
        else:
            print(f"Prelievo non effettuato: puoi ritirare al massimo {self.saldoAttuale:.2f}€")

    def versamento(self, importo):
        self.saldoAttuale += importo
        self.movimenti.append(importo)
        print("Versamento effettuato")

    def stampaSaldo(self):
        print(f"Attualmente nel conto ci sono {self.saldoAttuale:.2f}€")

    def ultime5operazioni(self):
        print("\nUltime 5 operazioni effettuate:")
        ultimeOp = self.movimenti if len(self.movimenti) <= 5  else self.movimenti[-5:]
        for op in ultimeOp:
            if op < 0:
                print(f"Hai prelevato {-op:.2f}€")
            else:
                print(f"Hai depositato {op:.2f}€")


def mostraMenu():
    print("\nBenvenuto nel tuo conto\n1) Versa\n2) Preleva\n3) Saldo Attuale\n4) Ultimi 5 movimenti\n5) Info Conto\n0) Esci")



correntista = ContoCorrente(0, "Paolo Neri", "FGH457848")
while True:
    mostraMenu()
    scelta = input("\nScegli l'operazione da svolgere, inserendo un numero da 0 a 5: ")
    if scelta.strip() == "" or not scelta.strip().isdigit():
        print("Inserimento errato: devi inserire un numero!")
    elif int(scelta.strip()) < 0 or int(scelta.strip()) > 5:
        print("Inserimento errato: devi inserire un numero da 0 a 5!")
    else:
        scelta = int(scelta)
        if scelta == 1:
            correntista.effettuaOperazione(False)
        elif scelta == 2:
            correntista.effettuaOperazione(True)
        elif scelta == 3:
            correntista.stampaSaldo()
        elif scelta == 4:
            correntista.ultime5operazioni()
        elif scelta == 5:
            print(f"{correntista}")
        else:
            print("Hai terminato. Arrivederci")
            break