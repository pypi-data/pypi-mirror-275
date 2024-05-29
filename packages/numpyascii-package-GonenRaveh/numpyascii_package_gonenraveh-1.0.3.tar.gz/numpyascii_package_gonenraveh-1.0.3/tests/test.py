import numpy as np
from numpyascii_GonenRaveh import numpyascii as npa
npa.selftest()

x = npa.np3(
'''             
   +---+---+----+
  /   /   /   2/| 
 /   /   /    / .
+---+---+---+/ /|
| 0 |...| 8 | / .
+---+---+---+/ /|
|...|   |   | / .
+---+---+---+/ /
|10 |   |   | /
+---+---+---+/
''')
print('computed shape=',x.shape, 'SUCCESS=', x.shape==(1+10-0,1+8-0,1+2-0))
