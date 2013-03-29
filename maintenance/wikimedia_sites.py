# -*- coding: utf-8  -*-
"""
This script checks the language list of each Wikimedia multiple-language site
against the language lists
"""
#
# (C) Pywikipedia bot team, 2008-2010
#
# Distributed under the terms of the MIT license.
#
__version__ = '$Id$'

import sys, re

sys.path.insert(1, '..')
import pywikibot
import codecs

familiesDict = {
    'wikipedia':  'wikipedias_wiki.php',
    'wiktionary': 'wiktionaries_wiki.php',
    'wikiquote':  'wikiquotes_wiki.php',
    'wikisource': 'wikisources_wiki.php',
    'wikibooks':  'wikibooks_wiki.php',
    'wikinews':   'wikinews_wiki.php',
    'wikiversity':'wikiversity_wiki.php',
}
exceptions = ['www']

def update_family(families):
    if not families:
        families = familiesDict.keys()
    for family in families:
        pywikibot.output('Checking family %s:' % family)

        original = pywikibot.Family(family).languages_by_size
        obsolete = pywikibot.Family(family).obsolete

        url = 'http://s23.org/wikistats/%s' % familiesDict[family]
        uo = pywikibot.MyURLopener
        f = uo.open(url)
        text = f.read()

        if family == 'wikipedia':
            p = re.compile(r"\[\[:([a-z\-]{2,}):\|\1\]\].*?'''([0-9,]{1,})'''</span>\]", re.DOTALL)
        else:
            p = re.compile(r"\[http://([a-z\-]{2,}).%s.org/wiki/ \1].*?'''([0-9,]{1,})'''\]" % family, re.DOTALL)

        new = []
        for lang, cnt in p.findall(text):
            if lang in obsolete or lang in exceptions:
                # Ignore this language
                continue
            new.append(lang)
        if original == new:
            pywikibot.output(u'The lists match!')
        else:
            pywikibot.output(u"The lists don't match, the new list is:")
            missing = set(original) - set(new)
            new += missing
            text = u'        self.languages_by_size = [\r\n'
            line = ' ' * 11
            for lang in new:
                if len(line)+len(lang) <= 76:
                    line += u" '%s'," % lang
                else:
                    text += u'%s\r\n' % line
                    line = ' ' * 11
                    line += u" '%s'," % lang
            text += u'%s\r\n' % line
            text += u'        ]'
            pywikibot.output(text)
            if missing:
                pywikibot.output(u"WARNING: ['%s'] not listed at wikistats.\n"
                                 u"Now listed as last item\n"
                                 % "', '".join(missing))
            family_file_name = '../families/%s_family.py' % family
            family_file = codecs.open(family_file_name, 'r', 'utf8')
            old_text = family_text = family_file.read()
            old = re.findall(ur'(?msu)^ {8}self.languages_by_size.+?\]',
                             family_text)[0]
            family_text = family_text.replace(old, text)
            family_file = codecs.open(family_file_name, 'w', 'utf8')
            family_file.write(family_text)
            family_file.close()

if __name__ == '__main__':
    try:
        fam = []
        for arg in pywikibot.handleArgs():
            if arg in familiesDict.keys() and arg not in fam:
                fam.append(arg)
        update_family(fam)
    finally:
        pywikibot.stopme()
