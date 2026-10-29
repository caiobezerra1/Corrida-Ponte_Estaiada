*Sistema de Corridas Noturna da Ponte Estaiada*

Sistema de inscrições e resultados da Corrida Noturna da Ponte Estaiada, desenvolvido em Python para a disciplina de Programação I do curso de Engenharia de Software do Centro Universitário Santo Agostinho (UNIFSA)

O projeto tem como objetivo automatizar o cadastro dos corredores, organizar as informações das inscrições e facilitar o cálculo dos resultados da corrida, reduzindo erros de cobrança, classificação e premiação.

*Objetivo do Projeto*

Desenvolver um sistema capaz de gerenciar as inscrições e os resultados dos participantes da Corrida Noturna da Ponte Estaiada, aplicando os conceitos de lógica de programação, estruturas de dados e funções em Python

🛠️ *Tecnologias Utilizadas*

Linguagem: Python
Controle de versão: Git
Repositório: GitHub

*Como Executar ?*

Python 3 instalado no computador
Git instalado, caso deseje clonar o repositório.

⚙️ *Funcionalidades do Sistema*

Etapa 1 — Inscrição e resultado de um corredor

Menu principal com opções para inscrição, cálculo de resultado e saída.
Cadastro de participantes com nome completo e idade.
Validação da idade mínima de 16 anos.
Seleção da distância da corrida: 5 km ou 10 km.

Seleção do lote de inscrição:
1º lote: R$ 80,00.
2º lote: R$ 100,00.

Classificação dos participantes por faixa etária:
Juvenil: 16 a 19 anos.
Adulto: 20 a 39 anos.
Master: 40 a 59 anos.
Veterano: 60 anos ou mais.

Geração de código identificador do corredor.
Exibição do comprovante de inscrição.
Armazenamento dos participantes em uma lista de dicionários.

Etapa 2 - Em desenvolvimento 

💻 *Exemplo de uso*

-------------------- Menu Principal --------------------

1. Inscrever participante
2. Calcular resultado
3. Sair

Escolha uma opção: 1

-------------------- Inscrição do Participante --------------------

Digite a idade do participante: 20
Digite o nome completo do participante: João Silva
Digite a distância da corrida (5km ou 10km): 5
Digite o lote (1° lote - R$ 80,00 / 2° lote - R$ 100,00): 1

-------------------- Comprovante de Inscrição --------------------

Nome: JOÃO
Idade: 20
Código do Corredor: JOASIL20
Categoria: Adulto
Distância: 5km
Valor a pagar: R$ 80,00

*Regras de negócio*

A idade mínima para participar é de 16 anos.
As distâncias disponíveis são 5 km e 10 km.
O valor-base depende do lote selecionado.
A prova de 10 km possui um acréscimo de R$ 20,00.
Participantes com 60 anos ou mais pagam metade do valor total da inscrição.
A categoria é determinada pela idade do participante.
A premiação depende do tempo realizado, da categoria e da distância percorrida.
O código do corredor é formado pelas três primeiras letras do primeiro nome, pelas três primeiras letras do último sobrenome e pela idade, conforme as regras da atividade.

👥 Autores

Integrante 1: Caio Bezerra — caiobezerra1 https://github.com/caiobezerra1
Integrante 2: Whallace Rauan — whallacewr https://github.com/whallacewr

*Contexto acadêmico*

Projeto desenvolvido para a disciplina de Programação I do curso de Engenharia de Software do Centro Universitário Santo Agostinho (UNIFSA), com base na atividade proposta para o Sistema da Corrida Noturna da Ponte Estaiada.