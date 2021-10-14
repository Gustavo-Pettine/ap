# Funções

def delta(automato, estado, simbolo, pilha):
    try:
        return automato[3][(estado, simbolo, pilha)]
    except:
        return (None,None)


def movimento(automato, palavra):
    estados, alfabeto_automato, alfabeto_pilha, transicoes, estado_atual, estado_inical_pilha, estado_final = automato

    if len(palavra) > 1:

        simbolo = palavra.pop(0)

        chaves = transicoes.keys()

        resultado = []

        for alfabeto in alfabeto_pilha:
            chave_aux = (estado_atual, simbolo, alfabeto)
            if chave_aux in chaves:
                novo_estado, nova_pilha = delta(automato, estado_atual, simbolo, alfabeto)
                movimentos = movimento((estados, alfabeto_automato, alfabeto_pilha, transicoes, novo_estado, nova_pilha, estado_final), palavra)
                # movimentos_estado = movimento[0][0]

                #if len(movimentos) > 0:
                    #movimentos_palavra = movimentos[0][1]
                    #movimentos_pilha = movimentos[0][2]
                aux = (estado_atual, [simbolo] + palavra, nova_pilha + [estado_inical_pilha])
                resultado.append([aux] + movimentos)

        return resultado

    else:
        return [(estado_atual, [''], [estado_inical_pilha])]


def aceita(automato, estado, simbolo, pilha):
    print()
    
def computacao(automato, estado, simbolo, pilha):
    print()

def pf2pn(automato):
    print()
