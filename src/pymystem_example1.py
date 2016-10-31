# -*- coding: utf-8 -*-

from pymystem3 import Mystem
# text = "some good newses"
text = "Красивая мама красиво мыла раму"
m = Mystem()
lemmas = m.lemmatize(text)
print(''.join(lemmas))
