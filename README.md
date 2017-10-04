# erfgoeddecreet
pythonscript om het erfgoeddecreet toe te passen op locale data via QGIS

Er is een nieuw Vlaams onroerenderfgoeddecreet. Deze verplicht om bij vergunningaanvragen met ingreep in de bodem een archeologisch onderzoek uit te laten voeren, afhankelijk van de oppervlakte en de zone van het project. De bedoeling is een webapplicatie te maken met een gebruiksvriendelijke interface die informatie geeft op perceelniveau over de geldende normen van het decreet .

# Volgende lagen zijn nodig voor het doorvoeren van het project: 
Adp: Administratieve  percelen van je eigen gemeente > 'Adp.shp'
    LINK: https://download.agiv.be/Producten/Detail?id=386&title=GRB_Adp_administratief_perceel 

Gwp: Gewestplan > 'Gwp.shp'
    LINK: https://download.agiv.be/Producten/Detail?id=710&title=Gewestplan_vector_toestand_01_01_2002 _correctie_18_06_2014 

gga: Gebieden waar geen archeologische >'gga.shp' 
    LINK: https://dev-geo.onroerenderfgoed.be/geoserver/vioe_geoportaal/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=vioe_geoportaal:gebieden_geen_archeologie&outputFormat=shape-zip 

vast-az: Vastgestelde inventaris van archeologische zones  > 'vast_az.shp'
    LINK: https://inventaris.onroerenderfgoed.be/bestanden/gis/shape/aanduidingsobjecten.zip 

bes-ach_site: Beschermde archeologische sites > 'bes_arch_site.shp'
    LINK: https://inventaris.onroerenderfgoed.be/bestanden/gis/shape/aanduidingsobjecten.zip  

RUPenBPA-basis: Ruimtelijke uitvoeringsplan en Bijzonder plan van aanleg 
    Uit intern databeheer systeem : Cipal/Nestor
    filter hieruit de zone wel woon-of recreatie > 'wrzja.shp' 
    en de zone geen woon-of recreatie > 'wrzneen.shp'
