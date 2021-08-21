import requests
import json

# Gebietscode von https://www.xrepository.de/api/xrepository/urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:rs_2021-07-31/download/Regionalschl_ssel_2021-07-31.json
# ab Stelle 6 nur Nullen verwenden!
ninaBaseUrl = "https://warnung.bund.de/api31"
gebietscodeAugsburg="097720000000"
mowasBaseUrl = "https://warnung.bund.de/bbk.mowas/"
 
# aktuelle Warnmeldungen abrufen nach Gebietscode
response = requests.get(ninaBaseUrl+"/dashboard/"+gebietscodeAugsburg+".json")
# TODO: hier pruefen, ob Abruf erfolgreich war
# wenn Abruf erfolgreich war, erhalten wir ein JSON
warnungen = response.json()
# iteriere über alle Warnmeldungen
for warnung in warnungen:
    # komplette Warnmeldung ausgeben
    # print(warnung)
    # Der Dashboard-Abruf enthält nur eine Kurzform der Warnmeldung
    # Deshalb rufen wir hier die Details ab:
    ## Annahme: MOWAS Warnmeldung, TODO: Erweiterung um andere Quellen
    # das Feld "id" fängt bei MOWAS Meldungen mit "mow." an.
    # die für den folgenden Abruf nötige MOWAS ID fängt nach dem "." an. 
    id = warnung["payload"]["id"].split(".")[1] 
    # Detailmeldung abrufen (TODO: Fehlerhandling ergaenzen)
    meldung = requests.get(mowasBaseUrl+id+".json").json()
    # Das Info-Feld ist ein Array, es ist unklar, ob dies in Realitaet mehrere Elemente enthalten kann;
    # diese Beispiel liest nur das erste Info Element aus:
    meldung = meldung["info"][0]["event"]+": "+meldung["info"][0]["headline"]+" (Sent: "+meldung["sent"]+", Status: "+meldung["status"]+")"
    print("- "+meldung)
