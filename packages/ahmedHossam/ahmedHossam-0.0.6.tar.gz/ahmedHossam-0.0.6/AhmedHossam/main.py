import re

def saba7(name):
    return 'Saba7 ya ' + name

def sheel_tashkeel(text):
    arabic_diacritics = re.compile(r'[\u0617-\u061A\u064B-\u0652\u0670]')
    return re.sub(arabic_diacritics, '', text.replace('>','').replace('<','').replace('^','').replace('؞',''))