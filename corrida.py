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

# Função para calcular o valor da inscrição
def calcular_valor_inscricao(lote, distancia, idade):
    if lote == "1":
        valor = 80.00
    elif lote == "2":
        valor = 100.00
    else:
        raise ValueError("Lote inválido.")

    if distancia == "10km":
        valor += 20.00

    if idade >= 60:
        valor *= 0.5
    return valor

#Função para converte o tempo da corrida em segundos
def tempo_em_segundos(tempo):
    partes = tempo.split(":")
    if len(partes) != 3:
        raise ValueError("Formato de tempo inválido. Use HH:MM:SS.")

    try:
        horas, minutos, segundos = map(int, partes)
    except ValueError:
        raise ValueError("O tempo deve conter somente números e dois pontos")

    if horas < 0 or not (0 <= minutos <= 59) or not (0 <= segundos <= 59):
        raise ValueError("Minutos e segundos devem estar entre 00 e 59.")

    if len(partes[0]) != 2 or len(partes[1]) != 2 or len(partes[2]) != 2:
        raise ValueError("Use exatamente dois dígitos em cada parte: HH:MM:SS.")
    return horas * 3600 + minutos * 60 + segundos

#Função para verificar se o corredor foi premiado 
def verificar_premiacao(idade, distancia, tempo_segundos):
    categoria = calcular_categoria(idade)
    limites = {
        "Juvenil": {"5km": "00:25:00", "10km": "00:52:00"},
        "Adulto": {"5km": "00:22:00", "10km": "00:46:00"},
        "Master": {"5km": "00:25:00", "10km": "00:52:00"},
        "Veterano": {"5km": "00:30:00", "10km": "01:03:00"}
    }

    tempo_limite = tempo_em_segundos(limites[categoria][distancia])
    return tempo_segundos <= tempo_limite

#Função para calcular o Pace
def calcular_pace(tempo_segundos, distancia):
    """Calcula o pace médio em minutos e segundos por quilômetro."""
    if distancia == "5km":
        quilometros = 5
    elif distancia == "10km":
        quilometros = 10
    else:
        return None

    pace_segundos = tempo_segundos // quilometros
    minutos = pace_segundos // 60
    segundos = pace_segundos % 60

    return f"{minutos:02d}:{segundos:02d} min/km"

#Função para formatar segundos como HH:MM:SS
def formatar_tempo(segundos):
    segundos = int(segundos)
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60

    return f"{horas:02d}:{minutos:02d}:{segundos_restantes:02d}"

# Função para calcular o resumo da sessão
def calcular_resumo(inscritos):
    """Retorna a quantidade de inscrições e o total arrecadado."""
    quantidade = len(inscritos)
    arrecadacao = sum(p["valor"] for p in inscritos)

    return quantidade, arrecadacao

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
        distancia = input("Digite a distância da corrida que deseja participar(5km ou 10km): ").strip().lower()
        
        if distancia == "5":
            distancia = "5km"
        elif distancia == "10":
            distancia = "10km"

        if distancia not in ["5km", "10km"]:
            print("Distância inválida. Digite 5km ou 10km.")
            continue

        #Validação do lote do participante
        while True:
            lote = input("Digite o lote que deseja (1° lote - R$ 80,00 / 2° lote - R$ 100,00): ").strip()

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
            
            #Calculo para o valor final da inscrição
            valor = calcular_valor_inscricao(lote, distancia, idade)

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
        print(f"Valor a pagar: R$ {calcular_valor_inscricao(lote, distancia, idade):}")

    #Cálculo do resultado da corrida
    elif opcao == "2":
        print("\n-------------------- Resultado da Corrida --------------------")
        try:
            idade = int(input("Digite a idade do participante: "))
        except ValueError:
            print("Idade Inválida. Digite um número inteiro")
            continue 

        if idade < 16:
            print("A idade mínima para participar é de 16 anos.")
            continue
        distancia = input("Digite a distância (5km ou 10km): ").strip().lower()

        if distancia == "5":
            distancia = "5km"
        elif distancia == "10":
            distancia = "10km"

        if distancia not in ["5km", "10km"]:
            print("Distância inválida.")
            continue
        tempo = input("Digite o tempo da prova (HH:MM:SS): ").strip()
        try:
            segundos = tempo_em_segundos(tempo)
        except ValueError as erro:
            print(erro)
            continue

        categoria = calcular_categoria(idade)
        pace = calcular_pace(segundos, distancia)
        premiado = verificar_premiacao(idade, distancia, segundos)

        print(f"\nCategoria: {categoria}")
        print(f"Tempo em segundos: {segundos}")
        print(f"Pace: {pace}")
        if premiado:
            print("O corredor atingiu o tempo para premiação!")
        else:
            print("O corredor não atingiu o tempo para premiação.")
    
    #Saída do sistema
    elif opcao == "3":
        print("Saindo do sistema...Até logo!")
        break

    else:
        print("Opção inválida. Escolha 1, 2 ou 3.")

        