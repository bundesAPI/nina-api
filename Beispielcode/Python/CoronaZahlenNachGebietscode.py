import requests
import json

baseUrl = "https://warnung.bund.de/api31"
# Gebietscode von https://www.xrepository.de/api/xrepository/urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:rs_2021-07-31/download/Regionalschl_ssel_2021-07-31.json
# ab Stelle 6 nur Nullen verwenden!
codeMuenchen="091620000000"
# aktuelle Coronameldungen abrufen nach Gebietscode
coronaInfoAPI = "/appdata/covid/covidrules/DE/"
responseMuenchen = requests.get(baseUrl+coronaInfoAPI+codeMuenchen+".json").json() # TODO: add error handling
#print(responseMuenchen) # ganzes JSON ausgeben
outputString = responseMuenchen["level"]["headline"]+"\n"+responseMuenchen["level"]["range"]
print(outputString)

### Beispiel-Output:
# Infektionsgefahr Stufe 3
# Sieben-Tage-Inzidenz Kreis: 48,5
# Sieben-Tage-Inzidenz Bundesland: 38,3
