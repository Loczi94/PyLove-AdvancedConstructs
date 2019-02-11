from collections import namedtuple

# class Ojciec:
#     def __init__(self, imie, nazwisko, data_ur):
#         self.imie = imie
#         self.nazwisko = nazwisko
#         self.data_ur = data_ur

Ojciec = namedtuple('Ojciec', ['imie', 'nazwisko', 'data_ur'])
o = Ojciec('Mateusz', 'G.', '5.12.1994')
print(o)