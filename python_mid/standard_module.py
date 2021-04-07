from math import log10, cos
import re


pattern = re.compile('^[A-Za-z]+$')
print(pattern.match('I'))
print(pattern.match('love'))
print(pattern.match('python3'))

