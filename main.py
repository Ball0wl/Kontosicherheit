class Konto:
    """Eigenschaften vor Zugriff sichern"""
    __geldbestand = 0

    def __init__(self, kontonummer, kontostand=0):
        self.__kontonummer = kontonummer
        self.__kontostand = kontostand

    def geld_abheben(self, betrag):
        self.__kontostand -= betrag
        Konto.__geldbestand -= betrag

    def geld_einzahlen(self, betrag):
        self.__kontostand += betrag
        Konto.__geldbestand += betrag

    def kontostand_anzeigen(self):
        print("aktueller Kontostand: ", self.__kontostand)
        print("aktueller Geldbestand der Bank: ", Konto.__geldbestand, "\n")

    def kontostand_aktuell(self):
        return self.__kontostand


class Pluskonto(Konto):
    """konto welches noicht überzogen werden kann"""

    def __init__(self, kontonummer, kontostand=0):
        """über elternkalsse initialisieren"""
        super().__init__(kontonummer, kontostand=0)

    def geld_abheben(self, betrag):
        print("Geld soll vom Pluskonto abgehoben werden:", betrag)
        print("Max betrag ist momentan: ", self.kontostand_aktuell())

        if self.kontostand_aktuell() - betrag >= 0:
            print("Auszahlen von Pluskonto: ", betrag)
            super().geld_abheben(betrag)
        else:
            print("Konto kann nicht überzogen werden! Ihr verfügbares Guthaben: ", self.kontostand_aktuell())


kunde_ulmer = Konto("003891241")
kunde_ulmer.kontostand_anzeigen()
kunde_ulmer.geld_einzahlen(4000)
kunde_ulmer.kontostand_anzeigen()
kunde_ulmer.geld_einzahlen(250)
kunde_ulmer.kontostand_anzeigen()
kunde_ulmer.geld_abheben(1300)
kunde_ulmer.kontostand_anzeigen()

kunde_minderjaehrig = Pluskonto("939393777")
kunde_minderjaehrig.kontostand_anzeigen()
kunde_minderjaehrig.geld_einzahlen(150)
kunde_minderjaehrig.geld_abheben(100)
kunde_minderjaehrig.kontostand_anzeigen()
kunde_minderjaehrig.geld_abheben(50)
kunde_minderjaehrig.kontostand_anzeigen()
