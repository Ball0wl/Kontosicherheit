from konto import *

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
