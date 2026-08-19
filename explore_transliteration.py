from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

sample_devanagari = "उनी लजालु केटी थिइन्, तर पनि उनी सार्वजनिक रूपमा बोल्न सक्षम थिए।"

roman = transliterate(sample_devanagari, sanscript.DEVANAGARI, sanscript.ITRANS)
print(roman)