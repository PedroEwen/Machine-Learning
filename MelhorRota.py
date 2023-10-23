from sklearn.tree import DecisionTreeClassifier
        #Metros, Desvios, Semáforos
treino = [
        [10, 1, 3],   #Caminho A
        [10, 2, 0],   #Caminho B
        [12, 1, 3],   #Caminho C
        [15, 0, 2],   #Caminho D
        [11, 2, 1],   #Caminho E
        [10, 1, 0]    #Caminho F
]
         #Melhor solução:  10,0,1   
rot = [0, 1, 2, 3, 4, 5]

#modelo de árvore de decisão
decisão = DecisionTreeClassifier()     

#Treina o modelo
decisão.fit(treino, rot)

decisãoCarregada = decisão

#melhor rota
ponto_decisão = [10,0,0]

#definação de melhor para o sistema
rota = decisãoCarregada.predict([ponto_decisão])

rotas = ["A", "B", "C", "D", "E","F"]
melhor_rota_nome = rotas[rota[0]]

print("A melhor rota a tomar é:", melhor_rota_nome)
