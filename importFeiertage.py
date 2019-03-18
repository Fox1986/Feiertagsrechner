#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import des Scriptes:

import berechnung_feiertage as bf

# Initialisierung der Klasse und Übergabe der
# gewünschten Parameter. Im Beispiel werden die
# Feiertage für Sachsen im Jahr 2010 abgefragt

holidays = bf.Holidays(2010, 'SN')

# Abruf einer Liste, die alle Feiertage enthält. Die Liste
# hat das Format [[datetime-Objekt, Bezeichnung],]

liste = holidays.get_holiday_list()
# Ausgabe der Liste. Die Ausgabe kann natürlich beliebig
# angepasst werden.

for feiertag in liste:
     print feiertag