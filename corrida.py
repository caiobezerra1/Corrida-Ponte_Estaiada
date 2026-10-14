dados_inscritos = []

#Menu de inscrição
def menu_inscrição():
    print("-------------------- Menu de Inscrição --------------------")
    print("\n1. Inscrever participante")
    print("2. Listar participantes inscritos")
    print("3. Sair")
    opcao = input("\nEscolha uma opção: ").strip()
    return opcao

#Loop principal do Menu de Inscrição 
while True:
    opcao = menu_inscrição()

#Criação da inscrição do participante
    if opcao == "1":
        idade = int(input("Digite a idade do participante: "))
        if idade < 16:
            print("Desculpe, mas infelizmente a idade mínima para participar da corrida é de 16 anos.")
            continue 
        nome = input("Digite o nome completo do participante: ").strip()
        distancia = input("Digite a distância da corrida (5km ou 10km): ").strip()
        if distancia not in ["5km", "10km"]:
            print("Desculpe, mas a distância da corrida deve ser 5km ou 10km.")
            continue
        lote = input("Digite o lote do Participante (1° lote R$ 80,00 / 2° lote R$ 100,00 ): ")
        if lote not in ["1° lote", "2° lote"]:
            print("Desculpe, mas o lote do participante deve ser 1° lote ou 2° lote.")
            continue

        participante = {
        "nome" : nome,
        "idade" : idade,
        "distancia" : distancia,
        "lote" : lote
        }

        dados_inscritos.append(participante)
        print("Participante inscrito com sucesso!")

    elif opcao == "2":
        if not dados_inscritos:
               print("Nenhum participante inscrito.")
        else:
            print("\n-------------------- Participantes inscritos --------------------")
            for p in dados_inscritos: 
                print(f"Nome: {p['nome']} | Idade: {p['idade']} | Distância: {p['distancia']} | Lote: {p['lote']}")
                
    elif opcao == "3":
       print("Saindo do sistema...")
       break
    else:
        print("Opção inválida. Escolha 1, 2 ou 3.")