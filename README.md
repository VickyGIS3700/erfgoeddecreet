# erfgoeddecreet
pythonscript om het erfgoeddecreet toe te passen op locale data via QGIS

Er is een nieuw Vlaams onroerenderfgoeddecreet. Deze verplicht om bij vergunningaanvragen met ingreep in de bodem een archeologisch onderzoek uit te laten voeren, afhankelijk van de oppervlakte en de zone van het project. 
Met behulp van bijhorend pythonscript kan je heel snel de zones afbakenen waar je verplicht bent om een archeologisch onderzoek uit te voeren én de zones waar het niet nodig is om een archeologisch onderzoek uit te laten voeren.

Na uitvoering van het script, kan je de projectboom als hulpmiddel gebruiken.

# Volgende lagen/shapes zijn nodig voor het doorvoeren van het project: 
Adp: Administratieve  percelen van je eigen gemeente > 'Adp.shp'  LINK: https://download.agiv.be/Producten/Detail?id=386&title=GRB_Adp_administratief_perceel 

Gwp: Gewestplan > 'Gwp.shp'  LINK: https://download.agiv.be/Producten/Detail?id=710&title=Gewestplan_vector_toestand_01_01_2002_correctie_18_06_2014 

gga: Gebieden waar geen archeologische >'gga.shp' LINK: https://dev-geo.onroerenderfgoed.be/geoserver/vioe_geoportaal/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=vioe_geoportaal:gebieden_geen_archeologie&outputFormat=shape-zip 

vast-az: Vastgestelde inventaris van archeologische zones  > 'vast_az.shp'  LINK: https://geo.onroerenderfgoed.be/downloads/aanduidingsobjecten.zip 

bes-ach_site: Beschermde archeologische sites > 'bes_arch_site.shp'  LINK: https://geo.onroerenderfgoed.be/downloads/aanduidingsobjecten.zip  

RUPenBPA-basis: Ruimtelijke uitvoeringsplan en Bijzonder plan van aanleg. 
Filter uit intern databeheer systeem  van de stad
de zone wel woon-of recreatie > 'wrzja.shp' en
de zone geen woon-of recreatie > 'wrzneen.shp'

Let op het coördinatenstelsel (vb alles in EPSG:31340)!!
Voorbeeld van een eindresultaat: http://geotic.maps.arcgis.com/apps/webappviewer/index.html?id=cacc6e1fb5714e5ab640da12619d5c5a
