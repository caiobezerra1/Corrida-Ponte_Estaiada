dados_inscritos = []

#Menu de inscrição
def menu_inscrição():
    print("-------------------- Menu de Inscrição --------------------")
    print("\n1. Inscrever participante")
    print("2. Calcular resultado")
    print("3. Sair")
    opcao = input("\nEscolha uma opção: ").strip()
    return opcao

#Função para calcular categoria do participante com base na idade
def calcular_categoria(idade):
    if 16 <= idade <= 19:
        return "Juvenil"
    elif 20 <= idade <= 39: 
        return "Adulto"
    elif 40 <= idade <= 59:
        return "Master"
    elif idade >= 60:
        return "Veterano"
    else:
        return "Idade inválida"

#Loop principal do menu de inscrição
while True:
    opcao = menu_inscrição()

#Criação da inscrição do participante
    #Validação da idade do participante
    if opcao == "1":
        try:
            idade = int(input("Digite a idade do participante: "))
        except ValueError:
            print("Idade inválida. Digite um número inteiro.")
            continue
        if idade < 16:
            print("Desculpe, a idade mínima para participar da corrida é de 16 anos.")
            continue

        nome = input("Digite o nome completo do participante: ").strip()

        #Validação da distância da corrida
        distancia = input("Digite a distância da corrida (5km ou 10km): ").strip().lower()
        if distancia == "5":
            distancia = "5km"
        elif distancia == "10":
            distancia = "10km"

        if distancia not in ["5km", "10km"]:
            print("Distância inválida. Digite 5km ou 10km.")
            continue

        #Validação do lote do participante
        while True:
            lote = input("Digite o lote (1° lote - R$ 80,00 / 2° lote - R$ 100,00): ").strip()
            if lote in ["1", "2"]:
                if lote == "1":
                    lote = "1° lote"
                else:
                    lote = "2° lote"
                break
            else:
                print("Lote inválido. Digite 1° lote ou 2° lote.")

        #Armazenamento dos dados do participante
        participante = {
            "nome": nome,
            "idade": idade,
            "distancia": distancia,
            "lote": lote}

        dados_inscritos.append(participante)
        print("Participante inscrito com sucesso!")

    #Listagem dos participantes inscritos
    elif opcao == "2":
        
    #Saída do sistema
    elif opcao == "3":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Escolha 1, 2 ou 3.")