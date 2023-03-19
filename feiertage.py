#!/usr/bin/env python
# -*- coding: utf-8 -*-

#----------------------------------------------------------------------------------------------------------------------#

# Titel:            feiertage.py
# Beschreibung:     Mit diesem Script können die Feiertage in Deutschland berechnet und ausgegeben werden.
# Autor:            Hinrik Taeger
# Version:          1.0
# Kategorie:        Calendar
# Probs:            Stephan John, Heiner Lichtenberg
# Ziel:             MacOS

# Wird dem Script ein Bundesland übergeben, werden alle Feiertage dieses Bundeslandes ausgegeben.
# Wird kein Bundesland übergeben, so werden nur die bundeseinheitlichen Feiertage ausgegeben.

#----------------------------------------------------------------------------------------------------------------------#

#                           Importe

import datetime

#----------------------------------------------------------------------------------------------------------------------#

#                           Globale Variablen
bundesland_dict = {
    'Baden-Württemberg': 'BW',
    'Bayern': 'BY',
    'Berlin': 'BE',
    'Brandenburg': 'BB',
    'Bremen': 'HB',
    'Hamburg': 'HH',
    'Hessen': 'HE',
    'Mecklenburg-Vorpommern': 'MV',
    'Niedersachsen': 'NI',
    'Nordrhein-Westfalen': 'NW',
    'Rheinland-Pfalz': 'RP',
    'Saarland': 'SL',
    'Sachsen': 'SN',
    'Sachsen-Anhalt': 'ST',
    'Schleswig-Holstein': 'SH',
    'Thüringen': 'TH',
}

#----------------------------------------------------------------------------------------------------------------------#

#                           Funktionen


# Berechnet die Feiertage für ein Jahr und ein bestimmtes Bundesland.#
# Beides muss entsprechend in die Klasse übergeben werden.
class Feiertage:
    # Constructor der Klasse
    def __init__(self, jahr, bland_id):
        self.jahr = int(jahr)
        # Das Jahr muss größer 1970 sein
        if self.jahr < 1970:
            self.jahr = 1970
        # Prüfen und Festlegen der Bundesland-ID
        if bland_id:
            self.bland_id = bland_id.upper()
            if self.bland_id not in list(bundesland_dict.values()):
                self.bland_id = None
        # Berechnen von Ostern
        ostern = Ostern(self.jahr)
        self.ostern = ostern.get_date()
        # Liste für die Feiertage
        self.feiertage_list = []
        # Berechnen der bundesweiten Feiertage
        self.bundesweite_feiertage()
        # Berechnen der spezifischen Feiertage
        if bland_id:
            self.get_heilige_drei_koenige(bland_id)
            self.get_mariae_himmelfahrt(bland_id)
            self.get_reformationstag(bland_id)
            self.get_allerheiligen(bland_id)
            self.get_buss_und_bettag(bland_id)
            self.get_fronleichnam(bland_id)
            self.get_frauentag(bland_id)
            self.get_weltkindertag(bland_id)
            self.get_tag_der_befreiung(bland_id)  # nur für das Jahr 2020 in Berlin

    # Ausgabe-Funktion der Klasse
    def get_feiertage_list(self):
        self.feiertage_list.sort()
        return self.feiertage_list

    # Funktion für die bundesweiten Feiertage
    def bundesweite_feiertage(self):
        # feste Feiertage:
        neujahr = datetime.date(self.jahr, 1, 1)
        self.feiertage_list.append([neujahr, 'Neujahr'])
        erster_mai = datetime.date(self.jahr, 5, 1)
        self.feiertage_list.append([erster_mai, '1. Mai'])
        tag_der_deutschen_einheit = datetime.date(self.jahr, 10, 3)
        self.feiertage_list.append([tag_der_deutschen_einheit, 'Tag der deutschen Einheit'])
        erster_weihnachtstag = datetime.date(self.jahr, 12, 25)
        self.feiertage_list.append([erster_weihnachtstag, 'Erster Weihnachtsfeiertag'])
        zweiter_weihnachtstag = datetime.date(self.jahr, 12, 26)
        self.feiertage_list.append([zweiter_weihnachtstag, 'Zweiter Weihnachtsfeiertag'])

        # bewegliche Feiertage:
        self.feiertage_list.append([self.get_feiertag(2, korrektur='minus'), 'Karfreitag'])
        self.feiertage_list.append([self.ostern, 'Ostersonntag'])
        self.feiertage_list.append([self.get_feiertag(1), 'Ostermontag'])
        self.feiertage_list.append([self.get_feiertag(39), 'Christi Himmelfahrt'])
        self.feiertage_list.append([self.get_feiertag(49), 'Pfingstsonntag'])
        self.feiertage_list.append([self.get_feiertag(50), 'Pfingstmontag'])

    # Berechnung der Feiertage, deren Datum abhängig von Ostersonntag sind.
    # Korrektur gibt an, ob die Tag hinzugezählt oder abgezogen werden müssen.
    def get_feiertag(self, tage, korrektur='plus'):
        delta = datetime.timedelta(days=tage)
        if korrektur == 'minus':
            return self.ostern - delta
        else:
            return self.ostern + delta

    # Berechnung der individuellen Feiertage
    # valid = Bundesländer, in denen die Feiertage gelten
    def get_heilige_drei_koenige(self, bland_id):
        valid = ['BY', 'BW', 'ST']
        if bland_id in valid:
            drei_koenige = datetime.date(self.jahr, 1, 6)
            self.feiertage_list.append([drei_koenige, 'Heilige Drei Könige'])

    def get_mariae_himmelfahrt(self, bland_id):
        valid = ['BY', 'SL']
        if bland_id in valid:
            mariae_himmelfahrt = datetime.date(self.jahr, 8, 15)
            self.feiertage_list.append([mariae_himmelfahrt, 'Mariä Himmelfahrt'])

    def get_reformationstag(self, bland_id):
        valid = ['BB', 'MV', 'SN', 'ST', 'TH', 'HH', 'HB', 'SH', 'NI']
        if bland_id in valid:
            reformationstag = datetime.date(self.jahr, 10, 31)
            self.feiertage_list.append([reformationstag, 'Reformationstag'])

    def get_allerheiligen(self, bland_id):
        valid = ['BW', 'BY', 'NW', 'RP', 'SL']
        if bland_id in valid:
            allerheiligen = datetime.date(self.jahr, 11, 1)
            self.feiertage_list.append([allerheiligen, 'Allerheiligen'])

    def get_buss_und_bettag(self, bland_id):
        valid = ['SN']
        if bland_id in valid:
            first_possible_day = datetime.date(self.jahr, 11, 16)
            buss_und_bettag = first_possible_day
            weekday = buss_und_bettag.weekday()
            step = datetime.timedelta(days=1)
            while weekday != 2:
                buss_und_bettag = buss_und_bettag + step
                weekday = buss_und_bettag.weekday()
            self.feiertage_list.append([buss_und_bettag, 'Buß und Bettag'])

    def get_fronleichnam(self, bland_id):
        valid = ['BW', 'BY', 'HE', 'NW', 'RP', 'SL']
        if bland_id in valid:
            fronleichnam = self.get_feiertag(60)
            self.feiertage_list.append([fronleichnam, 'Fronleichnam'])

    def get_frauentag(self, bland_id):
        valid = ['BE', ]
        if bland_id in valid:
            frauentag = datetime.date(self.jahr, 3, 8)
            self.feiertage_list.append([frauentag, 'Frauentag'])

    def get_weltkindertag(self, bland_id):
        valid = ['TH', ]
        if bland_id in valid:
            weltkindertag = datetime.date(self.jahr, 9, 20)
            self.feiertage_list.append([weltkindertag, 'Weltkindertag'])

    # nur im Jahr 2020
    def get_tag_der_befreiung(self, bland_id):
        valid = ['BE', ]
        if bland_id in valid:
            tag_der_befreiung = datetime.date(2020, 5, 8)
            self.feiertage_list.append([tag_der_befreiung, 'Tag der Befreiung'])


# Berechnung von Ostersonntag gem. Heiner Lichtenberg. Siehe auch http://de.wikipedia.org/wiki/Gaußsche_Osterformel
class Ostern:
    # Constructor für die Klasse
    def __init__(self, jahr):
        self.jahr = jahr

    # Säkularzahl: K(X) = X div 100
    def get_saekularzahl(self):
        saekularzahl = self.jahr // 100
        return saekularzahl

    #säkulare Mondschaltung: M(K) = 15 + (3K + 3) div 4 - (8K + 13) div 25
    def get_sek_mondschaltung(self):
        saekularzahl = self.get_saekularzahl()
        sek_mondschaltung = 15 + (3 * saekularzahl + 3) // 4 - (8 * saekularzahl + 13) // 25
        return sek_mondschaltung

    # säkulare Sonnenschaltung: S(K) = 2 - (3K + 3) div 4
    def get_sek_sonnenschaltung(self):
        saekularzahl = self.get_saekularzahl()
        sek_sonnenschaltung = 2 - (3 * saekularzahl + 3) // 4
        return sek_sonnenschaltung

    # Mondparameter: A(X) = X mod 19
    def get_mondparameter(self):
        mondparameter = self.jahr % 19
        return mondparameter

    # Keim für den ersten Vollmond im Frühling: D(A,M) = (19A + M) mod 30
    def get_erter_vollmomd_fruehling(self):
        mondparameter = self.get_mondparameter()
        sek_mondschaltung = self.get_sek_mondschaltung()
        erter_vollmomd_fruehling = (19 * mondparameter + sek_mondschaltung) % 30
        return erter_vollmomd_fruehling

    # kalendarische Korrekturgröße: R(D,A) = D div 29 + (D div 28 - D div 29) (A div 11)
    def get_kal_korrekturgroesse(self):
        mondparameter = self.get_mondparameter()
        erter_vollmond_fruehling = self.get_erter_vollmomd_fruehling()
        kal_korrekturgroesse = erter_vollmond_fruehling // 29 + (erter_vollmond_fruehling // 28 -
                                                                 erter_vollmond_fruehling // 29) * (mondparameter // 11)
        return kal_korrekturgroesse

    # Ostergrenze: OG(D,R) = 21 + D - R
    def get_ostergrenze(self):
        erter_vollmond_fruehling = self.get_erter_vollmomd_fruehling()
        kal_korrekturgroesse = self.get_kal_korrekturgroesse()
        ostergrenze = 21 + erter_vollmond_fruehling - kal_korrekturgroesse
        return ostergrenze

    # erster Sonntag im März: SZ(X,S) = 7 - (X + X div 4 + S) mod 7
    def get_erster_sonntag_maerz(self):
        sek_sonnenschaltung = self.get_sek_sonnenschaltung()
        erster_sonntag_maerz = 7 - (self.jahr + self.jahr // 4 + sek_sonnenschaltung) % 7
        return erster_sonntag_maerz

    # Entfernung des Ostersonntags von der Ostergrenze (Osterentfernung in Tagen): OE(OG,SZ) = 7 - (OG - SZ) mod 7
    def get_entfernung_ostersonntag_ostergrenze(self):
        ostergrenze = self.get_ostergrenze()
        erster_sonntag_maerz = self.get_erster_sonntag_maerz()
        entfernung_ostersonntag_ostergrenze = 7 - (ostergrenze - erster_sonntag_maerz) % 7
        return entfernung_ostersonntag_ostergrenze

    # Datum des Ostersonntags als Märzdatum (32. März = 1. April usw.): OS = OG + OE
    def get_ostersontag_maerzdatum(self):
        ostergrenze = self.get_ostergrenze()
        entfernung_ostersonntag_ostergrenze = self.get_entfernung_ostersonntag_ostergrenze()
        ostersontag_maerzdatum = ostergrenze + entfernung_ostersonntag_ostergrenze
        return ostersontag_maerzdatum

    # Ausgabe des Ostersonntags als datetime-Objekt
    def get_date(self):
        ostersontag_maerzdatum = self.get_ostersontag_maerzdatum()
        if ostersontag_maerzdatum > 31:
            month = 4
            day = ostersontag_maerzdatum - 31
        else:
            month = 3
            day = ostersontag_maerzdatum
        ostern = datetime.date(int(self.jahr), int(month), int(day))
        return ostern

#----------------------------------------------------------------------------------------------------------------------#

#                           MAIN


if __name__ == '__main__':
    aktjahr = datetime.datetime.today().year
    mein_bundesland = "BY"
    # Berechnen der Feiertage durch Erzeugen einer entsprechenden Klasse
    feiertage = Feiertage(aktjahr, mein_bundesland)
    # Aufruf der Ausgabefunktion der Klasse zum Erhalt der Ergebnisse
    feiertage_list = feiertage.get_feiertage_list()
    # Ausgabe der Ergebnisse
    for ft in feiertage_list:
        print(ft[1], ft[0])
