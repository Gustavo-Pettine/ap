# Exemplo de AP
import sys
sys.path.append('../')
from tc.ap import *


Q = {'q0', 'q1'}
S = {'0', '1'}
G = {'0', '1', 'X'}
D = {
  ('q0', '1', 'X'): ('q1', ['X', 'X']),
  ('q0', '0', 'X'): ('q0', []),
}

M1 = (Q, S, G, D, 'q0', 'Z0', {'q1'})


Q = {'q0', 'q1'}
S = {'0', '1', ''}
G = {'X', 'Z'}
D = {
  ('q0', '1', 'Z'): ('q0', ['X', 'Z']),
  ('q0', '1', 'X'): ('q0', ['X', 'X']),
  ('q0', '', 'X'): ('q1', ['X']),
  ('q1', '0', 'X'): ('q1', []),
}

M2 = (Q, S, G, D, 'q0', 'Z', {})

'''
q0 - 1100 - Z
q0 - 100 - XZ --> q1 - 100 - XZ
q0 - 00 - XXZ --> q1 - 00 - XXZ
q1 - 0 -  XZ
q1 - E - Z
'''

print(movimento(M2, list('1100')))