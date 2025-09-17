jog1 = str(input())
jog2 = str(input())

if jog1 == jog2 :
    print ("empate")
elif jog1 == "tesoura" and jog2 == "papel" or jog1 == "pedra" and jog2 == "tesoura" or jog1 == "papel" and jog2 == "pedra" :
    print ("jogador 1 venceu")
else:
    print ("jogador 2 venceu")