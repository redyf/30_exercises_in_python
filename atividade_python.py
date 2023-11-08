import math

# 1. Faça um Programa que mostre a mensagem "Alo mundo" na tela.
# print("Alo mundo")


# 2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
# pergunta = input("Por favor digite um número ")
# print(f"O número informado foi {pergunta}")


# 3. Faça um Programa que peça dois números e imprima a soma.
# def soma(a, b):
#     print(a + b)
#
#
# soma(2, 3)


# 4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
# def media(nota1, nota2, nota3, nota4):
#     soma_das_notas = nota1 + nota2 + nota3 + nota4
#     print(f"A sua média é: {soma_das_notas / 4}")
#
#
# media(6, 7.5, 6.7, 9)


# 5. Faça um Programa que converta metros para centímetros.
# def meters_to_cm(comprimento):
#     print(f"A sua medida em centímetros é: {comprimento * 100}cm")
#
#
# meters_to_cm(3.5)


# 6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
# def raio_circulo():
#     raio = float(input("Digite o raio do círculo: "))
#
#     area = math.pi * (raio**2)
#
#     print(f"A área do círculo com raio {raio} é {area:.2f}")
#
#
# raio_circulo()


# 7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
# def area_quadrado():
#     base = float(input("Qual a base do quadrado? "))
#     altura = float(input("Qual a altura do quadrado? "))
#     area = base * altura
#     print(f"A área do quadrado é: {area}")
#
#
# area_quadrado()


# 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
# def salario():
#     valor_por_hora = int(input(("Quanto você ganha por hora? ")))
#     horas_trabalhadas = int(input("Quantas horas você trabalhou no mês? "))
#     valor_mensal = valor_por_hora * horas_trabalhadas
#     print(f"O seu salário este mês foi de {valor_mensal}")
#
#
# salario()


# 9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#    C = 5 * ((F-32) / 9).
# def fahrenheit_to_celsius(temperatura):
#     F = temperatura
#     C = 5 * ((F - 32) / 9)
#     print(C)
#
#
# fahrenheit_to_celsius(145)


# 10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# def celsius_to_fahrenheit(temperatura):
#     celsius = temperatura
#     converter = celsius * 1.8 + 32
#     print(converter)
#
#
# celsius_to_fahrenheit(45)


# 11. Faça um Programa que peça dois números e imprima o maior deles.
# def imprima_maior_numero():
#     primeiro_numero = input("Digite o primeiro número: ")
#     segundo_numero = input("Digite o segundo número: ")
#     maior_numero = max(primeiro_numero, segundo_numero)
#     print(f"O maior número é {maior_numero}")
#
#
# imprima_maior_numero()
#


# 12. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
# def positivo_negativo():
#     pergunta = int(input("Digite algum valor númerico: "))
#     if pergunta > 0:
#         print(f"O valor digitado {pergunta} é positivo!")
#     elif pergunta == 0:
#         print(f"O valor digitado {pergunta} é neutro!")
#     else:
#         print(f"O valor digitado {pergunta} é negativo")
#
#
# positivo_negativo()


# 13. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
# def verique_letra_digitada(letra):
#     if letra == "F":
#         print("Sexo Feminino")
#     elif letra == "M":
#         print("Sexo Masculino")
#     else:
#         print("Sexo Inválido")
#
#
# verique_letra_digitada("M")


# 14. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
# def vogal_ou_consoante(letra):
#     vogais = ["a", "e", "i", "o", "u"]
#
#     if letra in vogais:
#         print("A letra é uma vogal")
#     else:
#         print("A letra é uma consoante")
#
#
# vogal_ou_consoante("e")


# 15. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#    A mensagem "Reprovado", se a média for menor do que sete;
#    A mensagem "Aprovado com Distinção", se a média for igual a dez.
# def media_do_aluno():
#     nota1 = float(input("Qual foi sua primeira nota parcial? "))
#     nota2 = float(input("Qual foi sua segunda nota parcial? "))
#     media_das_notas = (nota1 + nota2) / 2
#     if media_das_notas == 10:
#         print(
#             f"A média alcançada pelo aluno foi {media_das_notas}, portanto está Aprovado com Distinção"
#         )
#     elif media_das_notas >= 7:
#         print(
#             f"A média alcançada pelo aluno foi {media_das_notas}, portanto está Aprovado!"
#         )
#     else:
#         print(
#             f"A média alcançada pelo aluno foi {media_das_notas}, portanto está Reprovado!"
#         )
#
#
# media_do_aluno()


# 16. Faça um Programa que leia três números e mostre o maior deles.
# def maior_numero(x, y, z):
#     maior_de_todos = max(x, y, z)
#     print(maior_de_todos)
#
#
# maior_numero(243, 294, 921)


# 17. Faça um Programa que leia três números e mostre o maior e o menor deles.
# def maior_menor(x, y, z):
#     maior_de_todos = max(x, y, z)
#     menor_de_todos = min(x, y, z)
#     print(f"O maior número é {maior_de_todos} e o menor de todos é {menor_de_todos}")
#
#
# maior_menor(5, 7, 5)


# 18. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
# def produtos():
#     preco_do_produto1 = float(input("Qual o preço do primeiro produto?"))
#     preco_do_produto2 = float(input("Qual o preço do segundo produto?"))
#     preco_do_produto3 = float(input("Qual o preço do terceiro produto?"))
#
#     produto_mais_barato = min(preco_do_produto1, preco_do_produto2, preco_do_produto3)
#     print(f"O produto mais barato é {produto_mais_barato}")
#
#
# produtos()


# 19. Faça um Programa que leia três números e mostre-os em ordem decrescente.
# def ordem_decrescente():
#     lista = [1, 2, 3, 4, 5, 6]
#     print(lista[::-1])
#
#
# ordem_decrescente()


# 20. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
# def pergunta_turno(turno):
#     if turno == "M":
#         print("Bom Dia!")
#     elif turno == "V":
#         print("Boa Tarde!")
#     elif turno == "N":
#         print("Boa Noite!")
#     else:
#         print("Valor inválido")
#
#
# pergunta_turno("N")


# 21. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
# def pedir_nota():
#     nota = int(input("Digite uma nota entre 0 e 10: "))
#     if nota < 0 or nota > 10:
#         print("Valor inválido")
#     while nota < 0 or nota > 10:
#         nota = int(input("Digite uma nota entre 0 e 10: "))
#
#
# pedir_nota()


# 22. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
# def login():
#     while True:
#         nome_usuario = input("Digite o nome de usuário: ")
#         senha = input("Digite a senha: ")
#
#         if nome_usuario == senha:
#             print(
#                 "Erro: A senha não pode ser igual ao nome de usuário. Tente novamente."
#             )
#         else:
#             print("Cadastro bem-sucedido!")
#         break
#
#
# login()


# 23. Faça um programa que leia e valide as seguintes informações:
#    Nome: maior que 3 caracteres;
#    Idade: entre 0 e 150;
#    Salário: maior que zero;
#    Sexo: 'f' ou 'm';
#    Estado Civil: 's', 'c', 'v', 'd';


# 24. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
# def populacao():
#     countryA = 80000
#     taxa_anual_de_crescimentoA = 0.03
#     countryB = 200000
#     taxa_anual_de_crescimentoB = 0.015
#     anos = 0
#
#     while countryA < countryB:
#         countryA += countryA * taxa_anual_de_crescimentoA
#         countryB += countryB * taxa_anual_de_crescimentoB
#         anos += 1
#
#     print(f"Após {anos} anos, o país A superou a população do país B.")
#
#
# populacao()


# 25. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
# def populacao():
#     countryA = int(input("Informe a população do país A: "))
#     taxa_anual_de_crescimentoA = float(
#         input("informe a taxa de crescimento do país A: ")
#     )
#     countryB = int(input("Informe a população do país B: "))
#     taxa_anual_de_crescimentoB = float(
#         input("Informe a taxa de crescimento do país B: ")
#     )
#     anos = 0
#
#     while countryA < countryB:
#         countryA += countryA * taxa_anual_de_crescimentoA
#         countryB += countryB * taxa_anual_de_crescimentoB
#         anos += 1
#
#     print(f"Após {anos} anos, o país A superou a população do país B.")
#
#
# populacao()


# 26. Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.
# def imprime_numero_abaixo_do_outro():
#     for i in range(1, 21):
#         print(i)
#
#
# imprime_numero_abaixo_do_outro()

# 27. Faça um programa que leia 5 números e informe o maior número.
# def imprima_maior_numero(x, y, z, w, t):
#     maior_numero = max(x, y, z, w, t)
#     print(f"O maior número é {maior_numero}")


# imprima_maior_numero(2, 5, 32, 2225, 23242)


# 28. Faça um programa que leia 5 números e informe a soma e a média dos números.
# def soma_e_media(x, y, z, w, t):
#     soma_dos_numeros = x + y + z + w + t
#     media_dos_numeros = (soma_dos_numeros) / 5
#
#     print(
#         f"A soma dos números é {soma_dos_numeros} e a média dos mesmos é {media_dos_numeros}"
#     )
#
#
# soma_e_media(1, 2, 3, 4, 5)


# 29. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
# def numeros_impares():
#     for i in range(1, 51):
#         if i % 2 == 1:
#             print(i)
#
#
# numeros_impares()


# 30. Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
# def intervalo():
#     numero1 = int(input("Digite o primeiro número inteiro: "))
#     numero2 = int(input("Digite o segundo número inteiro: "))
#
#     inicio = min(numero1, numero2)
#     fim = max(numero1, numero2)
#
#     print("Números inteiros no intervalo entre", inicio, "e", fim, "são:")
#     for numero in range(inicio, fim + 1):
#         print(numero)
#
#
# intervalo()
