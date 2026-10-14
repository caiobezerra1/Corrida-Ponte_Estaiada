dados_inscritos = []

#Função Menu de inscrição
def menu_inscrição():
    print("-------------------- Menu Principal --------------------")
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

#Função para o código do corredor 
def codigo_corredor(nome_completo, idade): 
    partes_do_nome = nome_completo.split()
    if len(partes_do_nome) < 2:
        print("Digite o nome completo do participante (pelo menos primeiro e último nome).")
        return None

    primeiro_nome = partes_do_nome[0]
    ultimo_nome = partes_do_nome[-1]

    codigo_nome = primeiro_nome[:3].upper()
    codigo_ultimo_nome = ultimo_nome[:3].upper()
    return f"{codigo_nome}{codigo_ultimo_nome}{idade}"

#Loop principal do menu de inscrição
while True:
    opcao = menu_inscrição()

    #Criação da inscrição do participante
    if opcao == "1":
        print("\n-------------------- Inscrição do Participante --------------------")

        #Validação da idade
        try:
            idade = int(input("\nDigite a idade do participante: "))
        except ValueError:
            print("Idade inválida. Digite um número inteiro.")
            continue
        if idade < 16:
            print("Desculpe, a idade mínima para participar da corrida é de 16 anos.")
            continue

        #Validação do nome do participante 
        nome_completo = input("Digite o nome completo do participante: ").strip().upper()
        if not nome_completo: 
            print("O nome não pode estar vazio. Digite um nome válido.")
            continue 

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
            if lote == "1":
                lote_texto = "1° lote"
                valor = 80.00
                break
            elif lote == "2":
                lote_texto = "2° lote"
                valor = 100.00
                break
            else:
                print("Lote inválido. Digite 1° lote ou 2° lote.")

        #Armazenamento dos dados do participante na lista de inscritos
        codigo = codigo_corredor(nome_completo, idade)
        categoria = calcular_categoria(idade)
        primeiro_nome = nome_completo.split()[0]

        participante = {
            "nome": nome_completo,
            "idade": idade,
            "distancia": distancia,
            "lote": lote_texto,
            "codigo" : codigo,
            "categoria" : categoria,
            "valor": valor 
            }
        dados_inscritos.append(participante)

        #Comprovante de inscrição
        print("\n-------------------- Comprovante de Inscrição --------------------")
        print(f"Nome: {primeiro_nome}")
        print(f"Idade: {idade}")
        print(f"Código do Corredor: {codigo}")
        print(f"Categoria: {categoria}")
        print(f"Distância: {distancia}")
        print(f"Valor a pagar: R$ {valor:.2f}")

    #Cálculo do resultado da corrida
    
    #Saída do sistema
    elif opcao == "3":
        print("Saindo do sistema...Até logo!")
        break

    else:
        print("Opção inválida. Escolha 1, 2 ou 3.")