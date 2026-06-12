# A condição escolhida foi basicamente verificar quais tarefas já foram concluídas. 
# Para acompanharmos o andamento das atividades. 
tarefas = [
    "1. Lavar Louça"
    "\n2. Lavar Roupas"
    "\n3. Varer a casa"
    "\n4. Passar pano na casa"
    "\n5. Recolher Lixo"
    "\n6. Lavar Quintal"
    "\n7. Lavar o Banheiro"
    "\n8. Arrumar os Quartos"
]

print("Lista de Tarefas:")
 
for tarefa in tarefas:
 print (tarefa)

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

contador = 0
for status in tarefas_concluidas:
    if status == True:
        contador += 1

print("Quantidades de Tarefas concluídas:", contador)
    