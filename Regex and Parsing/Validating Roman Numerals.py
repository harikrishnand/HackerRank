regex_pattern = r"^M{0,3}(C{1}M{0,1})?C{0,1}D{0,1}X{0,1}C{0,3}X{0,1}L{0,1}I{0,1}X{0,3}I{0,1}V{0,1}I{0,3}$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))


############################Alternate solution ######################################


import re

thousand = 'M{0,3}'
hundred = '(C[MD]|D?C{0,3})'
ten = '(X[CL]|L?X{0,3})'
digit = '(I[VX]|V?I{0,3})'
print (bool(re.match(thousand + hundred+ten+digit +'$', input())))
