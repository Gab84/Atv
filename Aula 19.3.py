"""x_1 =- 1  #(podemos usar quelquer valor/ o x é apenas uma variavel de exemplo)  // (sempre declarar algo para declarar, nesse caso o 'x' está sendo comparado no while abaixo) // 
while x_1<=5: #while é indeterminado / enquanto // podemos usar qualquer definição, esse é apenas um exemplo
    x_1+=1 #igual a x= x+1  // sempre colocar contador se nao vai ir infinito // sempre colocar o TAB


print(x_1)
"""
#ler os alunos

"""x=0
while x<=3 : # sempre colocar codigo abaixo do while // esse codigo vai ser repetido 4 vezes, pois o while vai repetir até o (x for maior 3), ele repetiu 4 vezes pois começou com zero
    nome = input('digite seu nome ')
    cpf = int(input('digite seu cpf '))
    print(nome, cpf)
    x= x+1
    """
    
#somar numero com while

"""x_2=1
soma = 0

while x_2<=3 :
    
    numero = int(input('Digite um Numero: '))
    soma = soma+numero #soma começou com 0 e está armazenando o valor de '0 + o numero digitado' e vai fazer isso 3 vezes proceduramente 
    x_2= x_2+1
print(soma)
"""

#somar dois numero com while

"""x_3=1 #sempre declarar varialve antes de começar o while
soma = 0

while x_3<=3 :
    
    numero = int(input('Digite um Numero: '))
    numero1 = int(input('Digite o segundo numero: '))
    soma = numero+numero1 # essa linha vai somar o numero o primeiro e o segundo numero e atribuir o valor a variavel soma
    print(soma) #vai mostrar o resultado da soma dos numero na tela 3 vezes, toda vez que você digitar os 2 numeros
    x_3= x_3+1 #sempre finalizar com uma condição
    """
#numeros par ou impar com while

i = 0  #  Variavel 'i' apenas porque eu quis colocar esse nome 
while i<=3 : # repetição, enquanto 'i' for menor ou igual a 3 vai repetir
    n1= int(input('Digite um numero pra saber se é par '))
    div = n1%2
    if  div != 0: print(f'o numero {n1} é impar! ') 
    else: print(f'o numero {n1} é par! ')
    i = i+1
    