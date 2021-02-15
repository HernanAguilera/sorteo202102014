import json
import random

def sorteo():
    f = open('participantes.json', 'r')
    participantes = json.loads(f.read())

    apariciones = []
    for participante in participantes:
        for n in range(0, participante['count']):
            apariciones.append(participante['user'])
    f.close()
    
    print('Ganador(a)', random.choice(apariciones))

sorteo()