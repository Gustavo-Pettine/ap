import tc.ap as ap
import exemplos.apExemplos as exp

def test_delta():
  # fazer 10 testes
  assert ap.delta(exp.M1, 'q0', '1', 'X') == ('q1', ['X', 'X']) #1
  assert ap.delta(exp.M1, 'q0', '0', 'X') == ('q0', []) #2
