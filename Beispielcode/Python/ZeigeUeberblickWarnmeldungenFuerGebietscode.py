import requests
import json

# Gebietscode von https://www.xrepository.de/api/xrepository/urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:rs_2021-07-31/download/Regionalschl_ssel_2021-07-31.json
# ab Stelle 6 nur Nullen verwenden!
ninaBaseUrl = "https://warnung.bund.de/api31"
gebietscodeAugsburg="097720000000"
 
# aktuelle Warnmeldungen abrufen nach Gebietscode
response = requests.get(ninaBaseUrl+"/dashboard/"+gebietscodeAugsburg+".json") # TODO: hier pruefen, ob Abruf erfolgreich war

# wenn Abruf erfolgreich war, erhalten wir ein JSON
warnungen = response.json()

# iteriere über alle Warnmeldungen
for warnung in warnungen:
    # Der Dashboard-Abruf enthält nur eine Kurzform der Warnmeldung
    # Deshalb rufen wir hier die Details ab:
    id = warnung["payload"]["id"]
    warningDetails = requests.get(ninaBaseUrl+"/warnings/"+id+".json").json() # TODO: Fehlerbehandlung ergaenzen
    # headline und description Felder aus dem JSON fuer die Ausgabe zusammensetzen
    meldungsText = warningDetails["info"][0]["headline"]+ ": "+warningDetails["info"][0]["description"]
    print("- "+meldungsText)

### Beispiel-Output:
# - Coronavirus: Informationen des Bundesministeriums für Gesundheit: Die Zahl der mit dem Corona-Virus infizierten Menschen steigt gegenwärtig stark an. Es wächst daher die Gefahr einer weiteren Verbreitung der Infektion und - je nach Einzelfall - auch von schweren Erkrankungen.
# - Vorübergehende Änderung der Trinkwasserqualität: Chlorung besteht weiterhin: Die Chlorung besteht weiterhin.
# - Hochwasserinformation Bayern: Die Hochwasserwellen an Iller, Donau, Isar und Inn laufen ab. In deren Einzugsgebieten befinden sich noch einzelne Pegel in Meldestufe 1 und 2. ::: Es liegen Warnungen der Wasserwirtschaftsämter vor.