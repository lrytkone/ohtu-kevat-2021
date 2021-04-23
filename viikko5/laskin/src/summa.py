class Summa:
    def __init__(self, sovelluslogiikka, syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.syote = syote

    def suorita(self):
        try:
            luku = int(self.syote())
        except:
            luku = 0
        self.sovelluslogiikka.plus(luku)