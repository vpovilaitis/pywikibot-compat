# -*- coding: utf-8  -*-

__version__ = '$Id$'

import family


# The Wikimedia i18n family
class Family(family.Family):

    def __init__(self):
        family.Family.__init__(self)
        self.name = 'i18n'
        self.langs = {
            'i18n': 'translatewiki.net',
        }

        self.namespaces[4] = {
            '_default': [u'Project'],
        }
        self.namespaces[5] = {
            '_default': [u'Project talk'],
        }
        self.namespaces[6] = {
            '_default': [u'File'],
        }
        self.namespaces[7] = {
            '_default': [u'File talk'],
        }
        self.namespaces[90] = {
            '_default': [u'Thread'],
        }
        self.namespaces[91] = {
            '_default': [u'Thread talk'],
        }
        self.namespaces[92] = {
            '_default': [u'Summary'],
        }
        self.namespaces[93] = {
            '_default': [u'Summary talk'],
        }
        self.namespaces[100] = {
            '_default': [u'Portal'],
        }
        self.namespaces[101] = {
            '_default': [u'Portal talk'],
        }
        self.namespaces[202] = {
            '_default': [u'Property'],
        }
        self.namespaces[203] = {
            '_default': [u'Property talk'],
        }
        self.namespaces[206] = {
            '_default': [u'Form'],
        }
        self.namespaces[207] = {
            '_default': [u'Form talk'],
        }
        self.namespaces[208] = {
            '_default': [u'Concept'],
        }
        self.namespaces[209] = {
            '_default': [u'Concept talk'],
        }
        self.namespaces[420] = {
            '_default': [u'Layer'],
        }
        self.namespaces[421] = {
            '_default': [u'Layer talk'],
        }
        self.namespaces[1102] = {
            '_default': [u'Translating'],
        }
        self.namespaces[1103] = {
            '_default': [u'Translating talk'],
        }
        self.namespaces[1198] = {
            '_default': [u'Translations'],
        }
        self.namespaces[1199] = {
            '_default': [u'Translations talk'],
        }
        self.namespaces[1200] = {
            '_default': [u'Voctrain'],
        }
        self.namespaces[1201] = {
            '_default': [u'Voctrain talk'],
        }
        self.namespaces[1202] = {
            '_default': [u'FreeCol'],
        }
        self.namespaces[1203] = {
            '_default': [u'FreeCol talk'],
        }
        self.namespaces[1204] = {
            '_default': [u'Nocc'],
        }
        self.namespaces[1205] = {
            '_default': [u'Nocc talk'],
        }
        self.namespaces[1206] = {
            '_default': [u'Wikimedia'],
        }
        self.namespaces[1207] = {
            '_default': [u'Wikimedia talk'],
        }
        self.namespaces[1208] = {
            '_default': [u'StatusNet'],
        }
        self.namespaces[1209] = {
            '_default': [u'StatusNet talk'],
        }
        self.namespaces[1210] = {
            '_default': [u'Mantis'],
        }
        self.namespaces[1211] = {
            '_default': [u'Mantis talk'],
        }
        self.namespaces[1212] = {
            '_default': [u'Mwlib'],
        }
        self.namespaces[1213] = {
            '_default': [u'Mwlib talk'],
        }
        self.namespaces[1214] = {
            '_default': [u'Commonist'],
        }
        self.namespaces[1215] = {
            '_default': [u'Commonist talk'],
        }
        self.namespaces[1216] = {
            '_default': [u'OpenLayers'],
        }
        self.namespaces[1217] = {
            '_default': [u'OpenLayers talk'],
        }
        self.namespaces[1218] = {
            '_default': [u'FUDforum'],
        }
        self.namespaces[1219] = {
            '_default': [u'FUDforum talk'],
        }
        self.namespaces[1220] = {
            '_default': [u'Okawix'],
        }
        self.namespaces[1221] = {
            '_default': [u'Okawix talk'],
        }
        self.namespaces[1222] = {
            '_default': [u'Osm'],
        }
        self.namespaces[1223] = {
            '_default': [u'Osm talk'],
        }
        self.namespaces[1224] = {
            '_default': [u'WikiReader'],
        }
        self.namespaces[1225] = {
            '_default': [u'WikiReader talk'],
        }
        self.namespaces[1226] = {
            '_default': [u'Shapado'],
        }
        self.namespaces[1227] = {
            '_default': [u'Shapado talk'],
        }
        self.namespaces[1228] = {
            '_default': [u'iHRIS'],
        }
        self.namespaces[1229] = {
            '_default': [u'iHRIS talk'],
        }
        self.namespaces[1230] = {
            '_default': [u'Mifos'],
        }
        self.namespaces[1231] = {
            '_default': [u'Mifos talk'],
        }
        self.namespaces[1232] = {
            '_default': [u'Wikia'],
        }
        self.namespaces[1233] = {
            '_default': [u'Wikia talk'],
        }
        self.namespaces[1234] = {
            '_default': [u'OpenImages'],
        }
        self.namespaces[1235] = {
            '_default': [u'OpenImages talk'],
        }
        self.namespaces[1236] = {
            '_default': [u'Europeana'],
        }
        self.namespaces[1237] = {
            '_default': [u'Europeana talk'],
        }
        self.namespaces[1238] = {
            '_default': [u'Pywikibot'],
        }
        self.namespaces[1239] = {
            '_default': [u'Pywikibot talk'],
        }
        self.namespaces[1240] = {
            '_default': [u'Intuition'],
        }
        self.namespaces[1241] = {
            '_default': [u'Intuition talk'],
        }
        self.namespaces[1242] = {
            '_default': [u'EOL'],
        }
        self.namespaces[1243] = {
            '_default': [u'EOL talk'],
        }
        self.namespaces[1244] = {
            '_default': [u'Kiwix'],
        }
        self.namespaces[1245] = {
            '_default': [u'Kiwix talk'],
        }
        self.namespaces[1246] = {
            '_default': [u'Mozilla'],
        }
        self.namespaces[1247] = {
            '_default': [u'Mozilla talk'],
        }
        self.namespaces[1249] = {
            '_default': [u'FrontlineSMS talk'],
        }
        self.namespaces[1250] = {
            '_default': [u'EtherpadLite'],
        }
        self.namespaces[1251] = {
            '_default': [u'EtherpadLite talk'],
        }
        self.namespaces[1252] = {
            '_default': [u'Vicuna'],
        }
        self.namespaces[1253] = {
            '_default': [u'Vicuna talk'],
        }
        self.namespaces[1254] = {
            '_default': [u'FUEL'],
        }
        self.namespaces[1255] = {
            '_default': [u'FUEL talk'],
        }
        self.namespaces[1256] = {
            '_default': [u'Blockly'],
        }
        self.namespaces[1257] = {
            '_default': [u'Blockly talk'],
        }
        self.namespaces[1258] = {
            '_default': [u'MathJax'],
        }
        self.namespaces[1259] = {
            '_default': [u'MathJax talk'],
        }

    def version(self, code):
        return "1.23alpha"
