s = 1
m = s*60
g = m*60
d = g*24
r = d*365
from datetime import datetime

uro=datetime(2000,4,17,18,00)  #data w formacie rrrr.m.dd.hh.mm
life=datetime.now() - uro
print("1 godzina ma", g, "sekund")
print("1 doba ma", d, "sekund")
print("1 rok ma", r, "sekund")
print("Moje życie ma", life.total_seconds(), "sekund")