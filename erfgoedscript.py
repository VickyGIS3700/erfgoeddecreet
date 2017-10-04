# BIBLIOTHEKEN INITIALISEREN
import processing
from qgis import *
from qgis.utils import *
from qgis.core import *
from qgis.gui import *

#INITIALISEER PARAMETERS
#de link naar je rootfolder
root = 'G:/geo-ict-Qgis/'
# werk je met verschillende mappen, benoem ze hier
paths = ['import/', 'projectlagen/']
#deze shapes heb je nodig om te starten
shapefiles = ['Adp.shp','Gwp.shp','vast_az.shp','gga.shp','bes_arch_site.shp','wrzja.shp', 'wrzneen.shp']

#BASISLAGEN nodig voor de start van het project. Verkorte wijze van noteren.
adp = QgsVectorLayer(root + paths[0] + shapefiles[0], shapefiles[0], 'ogr')
gwp = QgsVectorLayer(root + paths[0] + shapefiles[1], shapefiles[1], 'ogr')
zone= QgsVectorLayer(root + paths[0] + shapefiles[2], shapefiles[2], 'ogr')
gebieden= QgsVectorLayer(root + paths[0] + shapefiles[3], shapefiles[3], 'ogr')
site= QgsVectorLayer(root + paths[0] + shapefiles[4], shapefiles[4], 'ogr')

#LAAD SHAPEFILES
QgsMapLayerRegistry.instance().addMapLayers([adp, gwp, zone, gebieden, site])

#IMPORT lagen reeds voorbereid
wrzja = QgsVectorLayer(paths[0] + shapefiles[5], shapefiles[5], 'ogr')
wrzneen = QgsVectorLayer(paths[0] + shapefiles[6], shapefiles[6], 'ogr')

#PROJECTLAGEN (werk-shapes)worden opgesteld tijdens dit script. Bepaal waar de lagen weggeschreven worden.
#Uitgebreide versie van notering onderaan. Niet zo praktisch als bovenstaande werkwijze.

bbox='G:/geo-ict-Qgis/projectlagen/BoundingBox.shp'
gwpclip='G:/geo-ict-Qgis/projectlagen/gwpclip.shp'
zoneclip='G:/geo-ict-Qgis/projectlagen/zoneclip.shp'
gebiedenclip='G:/geo-ict-Qgis/projectlagen/gebiedenclip.shp'
siteclip='G:/geo-ict-Qgis/projectlagen/siteclip.shp'
siteneen='G:/geo-ict-Qgis/projectlagen/siteneen.shp'
siteja='G:/geo-ict-Qgis/projectlagen/siteja.shp'
gganeen='G:/geo-ict-Qgis/projectlagen/gganeen.shp'
ggaja='G:/geo-ict-Qgis/projectlagen/ggaja.shp'
zoneneen='G:/geo-ict-Qgis/projectlagen/zoneneen.shp'
zoneja='G:/geo-ict-Qgis/projectlagen/zoneja.shp'
bufzoneneg='G:/geo-ict-Qgis/projectlagen/bufzoneneg.shp'
cleanzone='G:/geo-ict-Qgis/projectlagen/cleanzoneja.shp'
bufgganeg='G:/geo-ict-Qgis/projectlagen/bufgganeg.shp'
cleangga='G:/geo-ict-Qgis/projectlagen/cleanggaja.shp'
bufsiteneg='G:/geo-ict-Qgis/projectlagen/bufsiteneg.shp'
cleansite='G:/geo-ict-Qgis/projectlagen/cleansiteja.shp'


# ACTIES

#Boundingbox
outputs_QGISPOLYGONFROMLAYEREXTENT_1=processing.runalg('qgis:polygonfromlayerextent', adp,False,bbox)
qgis.utils.iface.addVectorLayer(bbox, 'BBox', 'ogr')

#Bepaal CRS van actieve laag
myLayer = qgis.utils.iface.activeLayer()
myLayer.setCrs(QgsCoordinateReferenceSystem(31370, QgsCoordinateReferenceSystem.EpsgCrsId))

#CRS van canvas
my_crs = core.QgsCoordinateReferenceSystem(31370, core.QgsCoordinateReferenceSystem.EpsgCrsId)
iface.mapCanvas().mapRenderer().setDestinationCrs(my_crs)

#Clip
outputs_QGISCLIP_1 = processing.runalg('qgis:clip', gwp,bbox,gwpclip)
outputs_QGISCLIP_2 = processing.runalg('qgis:clip', zone,bbox,zoneclip)
outputs_QGISCLIP_3 = processing.runalg('qgis:clip',gebieden,bbox,gebiedenclip)
outputs_QGISCLIP_4 = processing.runalg('qgis:clip',site,bbox,siteclip)

#Verschil met qgis
outputs_QGISDIFFERENCE_1 = processing.runalg('qgis:difference', adp,site,True,siteneen)
outputs_QGISDIFFERENCE_2 = processing.runalg('qgis:difference', adp,siteneen,True,siteja)
outputs_QGISDIFFERENCE_3 = processing.runalg('qgis:difference', siteneen,gebieden,True,gganeen)
outputs_QGISDIFFERENCE_4 = processing.runalg('qgis:difference', siteneen,gganeen,True,ggaja)
outputs_QGISDIFFERENCE_5 = processing.runalg('qgis:difference', gganeen,zone,True,zoneneen)
outputs_QGISDIFFERENCE_6 = processing.runalg('qgis:difference', gganeen,zoneneen,True,zoneja)

#Saga difference
outputs_SAGADIFFERENCE_1 = processing.runalg('saga:difference', bbox,zoneclip,True,bufzoneneg)
outputs_SAGADIFFERENCE_2 = processing.runalg('saga:difference', zoneja,bufzoneneg,True,cleanzone)
outputs_SAGADIFFERENCE_3 = processing.runalg('saga:difference', bbox,gebiedenclip,True,bufgganeg)
outputs_SAGADIFFERENCE_4 = processing.runalg('saga:difference', ggaja,bufgganeg,True,cleangga)
outputs_SAGADIFFERENCE_5 = processing.runalg('saga:difference', bbox,siteclip,True,bufsiteneg)
outputs_SAGADIFFERENCE_6 = processing.runalg('saga:difference', siteja,bufsiteneg,True,cleansite)

#Import (voorbewerkingen met arcmap) wrz-ja en wrz-neen

# resultaat visualiseren
gemShp4 = QgsVectorLayer(wrzja, 'wrz-ja', 'ogr')
gemShp3 = QgsVectorLayer(wrzneen, 'wrz-neen', 'ogr')
gemShp2 = QgsVectorLayer(cleanzone, 'zone-ja', 'ogr')
gemShp1 = QgsVectorLayer(cleansite, 'site-ja', 'ogr')
gemShp = QgsVectorLayer(cleangga, 'gga-ja', 'ogr')

QgsMapLayerRegistry.instance().addMapLayers([gemShp4, gemShp3, gemShp2, gemShp1,gemShp])
