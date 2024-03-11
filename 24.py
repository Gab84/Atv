#1 - Escreva um algoritmo em PORTUGOL para determinar se um dado número N (recebido através do teclado) é POSITIVO, NEGATIVO ou NULO

"""Python
Pergunte qual o numero
se o numero for maior que 0
escreva ' o numero é positivo'
se for menor que 0 
escreve ' o numero é positivo'
se não 
escreva 'o número é nulo'"""

print('--------------FIM----------------')
#2 -Faça um algoritmo que leia um número N e imprima “F1”, “F2” ou “F3”, conforme a condição:F1, se N<= 10F2, se N> 10 e N<=100F3, se N>100
"""
N2 = int(input('digite um numero'))
if N2 <= 10:
    print('F1')
elif N2 > 10 and N<=100:
    print('F2')
elif N2>100:
    print('F3')
"""
print('--------------FIM----------------')

#3. Construa um algoritmo que receba como entrada três valores e os imprima em ordem crescente.


"""n1_3 =int(input('Digite Um numero Diferente'))
n2_3 =int(input('Digite Um numero Diferente'))
n3_3 =int(input('Digite Um numero Diferente'))

valores = [n1_3,n2_3,n3_3] #variavel lista
print('lista em forma crescente',sorted(valores)) #lista em forma crescente
print('lista em forma decrescente',sorted(valores,reverse=True))#lista em forma decrescente
print('valores originais',valores)
valores.sort()
print(f'os valores depois de estarem em forma crescentes{valores}')"""
print('--------------FIM----------------')

#forma feita pelo professor
"""print("Os valores devem ser diferentes: ")
n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))
n3 = float(input("Digite o terceiro valor: "))
if n1 > n2 and n1 > n3 and n2>n3:
 print(f'A ordem crescente é: {n3}, {n2}, {n1}')
elif n2 > n1 and n2 > n3 and n3<n1:
 print(f'A ordem crescente é: {n3}, {n1}, {n2}')
elif n2 > n1 and n2 > n3 and n3 > n1:
 print(f'A ordem crescente é: {n1}, {n3}, {n2}')
elif n2 > n1 and n2 < n3 and n3 > n1:
 print(f'A ordem crescente é: {n1}, {n2}, {n3}')
elif n2 < n1 and n2 < n3 and n3 > n1:
 print(f'A ordem crescente é: {n2}, {n1}, {n3}')
else:
 print(f'A ordem crescente é: {n2}, {n3}, {n1}')"""


"""
n1 = int(input('Digite um número ')) 
n2 = int(input('Digite outro ')) 
n3 = int(input('Digite outro '))  
n4 = int(input('Digite outro ')) 
n5 = int(input('Digite outro ')) 
 
Lsta=[n1,n2,n3,n4,n5] 
print('Essa é a lista original:',Lsta) 
print('Essa é a lista com sorted():',sorted(Lsta)) 
print('Essa é a lista após o sorted():',Lsta) 
print('Resultado usando Lsta.sort():',Lsta.sort()) 
print('Essa é a lista após o .sort():',Lsta) """
print('--------------FIM----------------')

#4 -Ler dois valores para as variáveis A e B, e efetuar as trocas dos valores de forma que a variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor da variável A. Apresentar os valores trocados.
"""
A_4 = int(input('Digite um valor A: '))
B_4 = int(input('Digite um valor B: '))
print(f'os valores inseridos são: {A_4, B_4}')
A_4 = B_4
B_4 = A_4
print(f'os valores invertidos são: {A_4, B_4}')"""
print('--------------FIM----------------')
#5 - Ler dois números e informar qual maior e qual e o menor.
"""
n1_5 = int(input('Digite um numero: '))
n2_5 = int(input('Digite outro numero pra saber qual é maior: '))
if n1_5 > n2_5 :
    print(f'O maior número é: {n1_5} e o menor é {n2_5}')
else:
    print('o segundo numero é maior ')"""

"""n1_5 = int(input('Digite um numero: '))
n2_5 = int(input('Digite outro numero pra saber qual é maior: ')) 
if n1_5 == n2_5 :print('são iguais')
n1_5 = 'o primeiro é maior' if n1_5 > n2_5 else 'o segundo é maior'
print(n1_5)


    
print(f'{14*"-"}FIM{14*"-"}')"""
#6 - Considere que o último concurso vestibular apresentou três provas: Português, Matemática e Conhecimentos Gerais. Considerando que para cada candidato tem-se um registro contendo o seu nome e as notas obtidas em cada uma das provas, construa um algoritmo que forneça:
"""
nome = input('digite seu nome')
port = int(input('Digite sua nota em Português :'))
mat = int(input('Digite sua nota em matematica :'))
conG = int(input('Digite sua nota em conhecimentos gerais :'))
mednotas = (port+mat+conG)/3
aprov = 7
print(f'seu nome é {nome} e suas notas em portugues, matematica, e conhecimentos gerais respectivamente são {port},{mat},{conG}')
print(f'a média do aluno é {mednotas}')
if mednotas >= aprov:
    print ('Aprovado! ')
else:
    print('Reprovado! ')"""   

print('--------------FIM----------------')    

#7 - Ler os nomes e os pesos de duas pessoas e imprimir os dados da pessoa mais pesada
"""nome1_7 = input('Digite seu nome: ')
peso1_7 = int(input('Digite seu peso: '))
nome2_7 = input('Digite seu nome: ')
peso2_7 = int(input('Digite seu peso: '))

#comparar pesos
if peso1_7 > peso2_7 : print(f'a {nome1_7} é mais pesada que {nome2_7} e seu peso é {peso1_7} ')
else:
    print(f'a {nome2_7} é mais pesada que {nome1_7} e seu peso é {peso2_7} ')"""

#8 - Ler os anos de nascimento de duas pessoas e calcular suas idades. Imprimir o nome e a idade de cada uma e indicar qual é a maior nova 
"""Nome1_8 = input('digite seu nome')
nasc1_8 = int(input('Digite seu ano de nascimento'))
Nome2_8 = input('digite seu nome')
nasc2_8 = int(input('Digite seu ano de nascimento'))
idade1_8 = (2024 - nasc1_8)
idade2_8 = (2024 - nasc2_8)
print(f'seus nomes são {Nome1_8} e {Nome2_8} suas idades são {idade1_8} e {idade2_8}')
if idade1_8 < idade2_8: print(f'seu nome é {Nome1_8} sua idade é {idade1_8} e você é a mais nova')
else: print(f'seu nome é {Nome2_8} sua idade é {idade2_8} e você é a mais nova')
    """
#9 - Suponha que o conceito de um aluno seja determinado em função da sua nota. Suponha, também, que esta nota seja um valor inteiro na faixa de 0 a 100, conforme a seguinte faixa:Nota Conceito 0 a 49 Insuficiente50 a 69 Regular 70 a 84 Bom 85 a 100 Ótimo Crie um algoritmo que apresente o conceito e a nota do aluno.
"""nota = int(input('digite sua nota: '))
conceito = None
if nota >= 0 and nota <= 49:
    conceito = 'insuficiente'
elif nota >= 50 and nota <= 69:
    conceito = 'Regular'
elif nota >= 70 and nota <= 84:
    conceito = 'Bom'
elif nota >= 85 and nota <= 100:
    conceito = 'Ótimo' 
else:
    raise ValueError('nota inválida '+ str ( nota ))
    
print(f' a sua nota é {nota} ')
print(f'o conceito é {conceito} ')"""
#10 - Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino  ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
print(' M - Matutino \n V - Vespertino \n N - Noturno ')
turno = input('que turno você estuda? (Apenas a Letra!) ').lower()
if turno == 'm':
    print('Bom dia!')
elif turno == 'v' :
    print('Boa tarde !')
elif turno == 'n':
    print('Boa noite!')
else:
    print('Valor invalido! ')
