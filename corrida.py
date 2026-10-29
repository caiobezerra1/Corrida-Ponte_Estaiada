dados_inscritos = [
    {"nome": "MARIA CLARA SOUSA", "idade": 34, "distancia": "5km", "lote": "1° lote", "codigo": "MARSOU34", "categoria": "Adulto", "valor": 80.0, "tempo": "00:21:30"},
    {"nome": "JOSÉ RIBAMAR LIMA", "idade": 62, "distancia": "10km", "lote": "2° lote", "codigo": "JOSLIM62", "categoria": "Veterano", "valor": 60.0, "tempo": "01:02:59"},
    {"nome": "ANA BEATRIZ COSTA", "idade": 19, "distancia": "10km", "lote": "1° lote", "codigo": "ANACOS19", "categoria": "Juvenil", "valor": 100.0, "tempo": "00:51:00"},
    {"nome": "PAULO HENRIQUE ROCHA", "idade": 60, "distancia": "5km", "lote": "1° lote", "codigo": "PAUROC60", "categoria": "Veterano", "valor": 40.0, "tempo": "00:29:15"}]

codigos_usados = {"MARSOU34", "JOSLIM62", "ANACOS19", "PAUROC60"}

tempos_limite = (
    ("Juvenil", "5km", "00:25:00"),
    ("Juvenil", "10km", "00:52:00"),
    ("Adulto", "5km", "00:22:00"),
    ("Adulto", "10km", "00:46:00"),
    ("Master", "5km", "00:25:00"),
    ("Master", "10km", "00:52:00"),
    ("Veterano", "5km", "00:30:00"),
    ("Veterano", "10km", "01:03:00")
)

#Função Menu de inscrição
def menu_inscrição():
    print("-------------------- Menu Principal --------------------")
    print("\n1. Cadastrar corredor")
    print("2. Listar inscritos")
    print("3. Buscar corredor pelo código")
    print("4. Registrar tempo de prova")
    print("5. Contar inscritos por categoria")
    print("6. Mostrar resumo dos tempos")
    print("7. Mostrar classificação geral")
    print("8. Mostrar pódio por categoria")
    print("9. Sair")

    opcao = input("\nEscolha uma opção: ").strip()
    return opcao

#Função para calcular categoria do participante com base na idade
def calcular_categoria(idade):
    """Retorna a categoria do corredor a partir da idade."""
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
    """Calcula o valor da inscrição pelo lote, distância e idade (meia-inscrição a partir de 60)."""
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
    if len(tempo) != 8 or tempo[2] != ":" or tempo[5] != ":":
        raise ValueError("Formato inválido. Use HH:MM:SS.")

    try:
        horas = int(tempo[0:2])
        minutos = int(tempo[3:5])
        segundos = int(tempo[6:8])
    except ValueError:
        raise ValueError("O tempo deve conter números e dois pontos.")

    if horas < 0 or not (0 <= minutos <= 59) or not (0 <= segundos <= 59):
        raise ValueError("Minutos e segundos devem estar entre 00 e 59.")
    return horas * 3600 + minutos * 60 + segundos


#Função para verificar se o corredor foi premiado 
def verificar_premiacao(idade, distancia, tempo_segundos):
    """Retorna True se o tempo é menor ou igual ao limite da categoria na distância."""
    categoria = calcular_categoria(idade)

    for cat, dist, tempo in tempos_limite:
        if cat == categoria and dist == distancia:
            limite = tempo_em_segundos(tempo)
            return tempo_segundos <= limite

    return False

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

    return f"{minutos}'{segundos:02d}\"/km"

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


# Função para listar os inscritos
def listar_inscritos():
    if not dados_inscritos:
        print("Não existem corredores inscritos.")
        return

    for participante in dados_inscritos:
        print("\n-------------------- Corredor --------------------")
        print(f"Nome: {participante['nome']}")
        print(f"Código: {participante['codigo']}")
        print(f"Idade: {participante['idade']}")
        print(f"Categoria: {participante['categoria']}")
        print(f"Distância: {participante['distancia']}")
        print(f"Tempo: {participante['tempo']}")

#Função para procurar corredor
def buscar_corredor(codigo):
    for participante in dados_inscritos:
        if participante["codigo"] == codigo:
            return participante
    return None

# Função para contar inscritos por categoria
def contar_por_categoria():
    categorias = {
        "Juvenil": 0,
        "Adulto": 0,
        "Master": 0,
        "Veterano": 0}

    for participante in dados_inscritos:
        categoria = participante["categoria"]
        categorias[categoria] += 1

    print("\n-------------------- Inscritos por categoria --------------------")
    for categoria, quantidade in categorias.items():
        print(f"{categoria}: {quantidade}")

# Função para mostrar corredores com tempo e premiados
def mostrar_resumo_tempos():
    corredores_com_tempo = [
        p for p in dados_inscritos
        if p["tempo"] is not None
    ]

    corredores_premiados = [
        p for p in dados_inscritos
        if p["tempo"] is not None
        and verificar_premiacao(
            p["idade"],
            p["distancia"],
            tempo_em_segundos(p["tempo"])
        )
    ]

    print("\n-------------------- Corredores com tempo registrado --------------------")
    for p in corredores_com_tempo:
        print(p["nome"], "-", p["tempo"])

    print("\n-------------------- Corredores premiados --------------------")
    for p in corredores_premiados:
        print(p["nome"], "-", p["categoria"])

# Função para mostrar a classificação geral por distância
def mostrar_classificacao():
    for distancia in ("5km", "10km"):
        corredores = [
            p for p in dados_inscritos
            if p["distancia"] == distancia and p["tempo"] is not None
        ]
        corredores.sort(key=lambda p: tempo_em_segundos(p["tempo"]))

        print(f"\n---------- Classificação geral: {distancia} ----------")

        if not corredores:
            print("Nenhum corredor possui tempo registrado.")
            continue
        for posicao, corredor in enumerate(corredores, start=1):
            print(
                f"{posicao}º - {corredor['nome']} | "
                f"Tempo: {corredor['tempo']} | "
                f"Categoria: {corredor['categoria']}")

# Função para mostrar o pódio por categoria e distância
def mostrar_podio():
    categorias = ("Juvenil", "Adulto", "Master", "Veterano")

    for distancia in ("5km", "10km"):
        for categoria in categorias:
            corredores = [
                p for p in dados_inscritos
                if p["distancia"] == distancia
                and p["categoria"] == categoria
                and p["tempo"] is not None]
            corredores.sort(key=lambda p: tempo_em_segundos(p["tempo"]))

            print(f"\n--- Pódio {categoria} - {distancia} ---")

            if not corredores:
                print("Nenhum corredor com tempo registrado.")
                continue
            for posicao, corredor in enumerate(corredores[:3], start=1):
                print(
                    f"{posicao}º lugar: {corredor['nome']} | "
                    f"Tempo: {corredor['tempo']}")

# Função para mostrar o relatório final
def relatorio_final():
    quantidade, arrecadacao = calcular_resumo(dados_inscritos)

    print("\n========== RELATÓRIO FINAL DA CORRIDA ==========")
    print(f"Total de inscritos: {quantidade}")
    print(f"Arrecadação total: R$ {arrecadacao:.2f}".replace(".", ","))

    for distancia in ("5km", "10km"):
        corredores = [
            p for p in dados_inscritos
            if p["distancia"] == distancia and p["tempo"] is not None]
        print(f"\n--- Resultados da distância {distancia} ---")

        if not corredores:
            print("Nenhum tempo registrado para esta distância.")
            continue

        tempos = [
            tempo_em_segundos(p["tempo"])
            for p in corredores
        ]

        media = round(sum(tempos) / len(tempos))
        
        mais_rapido = min(
            corredores,
            key=lambda p: tempo_em_segundos(p["tempo"])
        )

        print(f"Tempo médio: {formatar_tempo(media)}")
        print(f"Corredor mais rápido: {mais_rapido['nome']}")
        print(f"Tempo do mais rápido: {mais_rapido['tempo']}")

    print("\n========== FIM DO RELATÓRIO ==========")

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
            elif lote == "2":
                lote_texto = "2° lote"
            else:
                print("Lote inválido. Digite 1 ou 2.")
                continue

            try:
                valor = calcular_valor_inscricao(lote, distancia, idade)
                break
            except ValueError as e:
                print(e)

        #Armazenamento dos dados do participante na lista de inscritos
        codigo = codigo_corredor(nome_completo, idade)

        if codigo is None:
            continue

        codigo_base = codigo
        contador = 1

        while codigo in codigos_usados:
            codigo = f"{codigo_base}{contador:02d}"
            contador += 1

        codigos_usados.add(codigo)
        
        categoria = calcular_categoria(idade)
        primeiro_nome = nome_completo.split()[0]

        participante = {
            "nome": nome_completo,
            "idade": idade,
            "distancia": distancia,
            "lote": lote_texto,
            "codigo" : codigo,
            "categoria" : categoria,
            "valor": valor,
            "tempo": None
        }
        dados_inscritos.append(participante)

        #Comprovante de inscrição
        print("\n-------------------- Comprovante de Inscrição --------------------")
        print(f"Nome: {primeiro_nome}")
        print(f"Idade: {idade}")
        print(f"Código do Corredor: {codigo}")
        print(f"Categoria: {categoria}")
        print(f"Distância: {distancia}")
        print(f"Valor a pagar: R$ {valor:.2f}".replace(".", ","))

    # Listar inscritos
    elif opcao == "2":
        listar_inscritos()

    # Buscar corredor pelo código
    elif opcao == "3":
        codigo = input("Digite o código do corredor: ").strip().upper()
        participante = buscar_corredor(codigo)

        if participante is None:
            print("Corredor não encontrado. Verifique o código informado.")
            continue

        print(f"Nome: {participante['nome']}")
        print(f"Código: {participante['codigo']}")
        print(f"Categoria: {participante['categoria']}")
        print(f"Tempo: {participante['tempo']}")

    # Registrar tempo de prova
    elif opcao == "4":
        codigo = input("Digite o código do corredor: ").strip().upper()
        participante = buscar_corredor(codigo)

        if participante is None:
            print("Corredor não encontrado. Verifique o código informado.")
            continue

        tempo = input("Digite o tempo da prova (HH:MM:SS): ").strip()

        try:
            segundos = tempo_em_segundos(tempo)
        except ValueError as erro:
            print(erro)
            continue

        participante["tempo"] = tempo

        pace = calcular_pace(segundos, participante["distancia"])
        premiado = verificar_premiacao(
            participante["idade"],
            participante["distancia"],
            segundos)

        print(f"Tempo: {tempo}")
        print(f"Tempo em segundos: {segundos}")
        print(f"Pace: {pace}")

        if premiado:
            print("O corredor atingiu o tempo para premiação!")
        else:
            print("O corredor não atingiu o tempo para premiação.")

    #Contar inscritos por categoria
    elif opcao == "5":
        contar_por_categoria()


   # Mostrar resumo dos tempos
    elif opcao == "6":
        mostrar_resumo_tempos()

    # Mostrar classificação geral
    elif opcao == "7":
        mostrar_classificacao()

    # Mostrar pódio por categoria
    elif opcao == "8":
        mostrar_podio()

    # Sair do sistema
    elif opcao == "9":
        relatorio_final()
        print("Saindo do sistema... Até logo!")
        break

    else:
        print("Opção inválida. Escolha uma opção de 1 a 9.")
