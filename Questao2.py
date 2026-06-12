# Essas funções ajudam a controlar a divisão de tarefas entre os moradores.
# Permite verificar o total de tarefas concluídas e calcular todas as tarefas feitas. 
def contar_concluidas(lista_status):
    contador = 0

    for status in lista_status:
        if status == True:
            contador += 1
    return contador

def calcular_porcetagem(concluidas, total):
    porcetagem = (concluidas * 100) / total
    return porcetagem 

tarefas_concluidas = [
    True,
    False,
    True,
    False,
    True,
    False,
    True,
    False
]

total_tarefas = len(tarefas_concluidas)

quantidade_concluidas = contar_concluidas(tarefas_concluidas)

porcetagem = calcular_porcetagem(
    quantidade_concluidas,
     total_tarefas
)

print("Total de Tarefas:", total_tarefas)
print("Tarefas Concluidas:", quantidade_concluidas)
print("Porcetagem Concluidas:", porcetagem, "%")