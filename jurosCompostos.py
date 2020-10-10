import matplotlib.pyplot as plt
 
def juros_compostos(montante_inicial, taxa, aporte, tempo):
  
  ''' Essa função calcula o rendimento e exibe o gráfico da evolução'''
 
  print()
  print()
  print("+=" * 50)
  print(f"Tabela de Rendimento Mensal a Juros Compostos ao longo de {tempo} meses:")
  print("+=" * 50)
  x = []
  y = []
  montante = montante_inicial
  for i in range(tempo):
    total_mes = (montante * (1+taxa)) + aporte
    total_conf = format(total_mes,".2f")
    totalprint = str(total_conf).replace(".",",")
    print(f"Após o {i+1}º período, o seu montante, com a incidência de juros compostos é: R${totalprint}")
    montante = total_mes
    x.append(i+1)
    y.append(total_mes)
  plt.xlabel("Meses")
  plt.ylabel("Montante (R$)")
  plt.title("Evolução do Dinheiro com Juros Compostos")
  plt.rcParams['figure.figsize'] = (15,10)
  plt.plot(x, y)
  plt.show()
 
def exibir_dados ():
  
  ''' Essa função organiza os dados e imprime na tela.'''
 
  print()
  print()
  print()
  print("+=" * 50)
  print(f"Dados adotados para cálculo dos juros compostos")
  print("+=" * 50)
  m = montante_inicial
  mont_conf = format(m,".2f")
  valor = str(mont_conf).replace(".",",")
  print(f"O seu montante inicial é de R${valor}.")
  tx = taxa * 100
  print (f"A sua taxa de rendimento mensal é de {tx}%.")
  a = aporte
  a_conf = format(a,".2f")
  a_mes = str(a_conf).replace(".",",")
  print(f"O seu aporte mensal para a aplicação é de R${a_mes}.")
  print(f"A aplicação incidirá juros compostos por um período de {tempo} meses.")
 
 
 
 
 
montante_inicial = float(input(f"Informe o valor do seu montante inicial: "))
taxa = float(input(f"Infome a taxa mensal aplicada: "))/100
if taxa <= 0:
  while (taxa <= 0):
    taxa = float(input(f"Em uma aplicação com incidência de juros, o valor da taxa tem que ser superior a zero. Infome a taxa mensal aplicada: "))/100
aporte = float(input(f"Infome o aporte mensal a ser adotado para o investimento: "))
tempo = int(input(f"Informe o número de meses desta aplicação: "))
if tempo <= 0:
  while (tempo <= 0):
    tempo = int(input(f"Essa aplicação é mensal, portanto, informe um valor inteiro superior a zero. Infome o número de meses desta aplicada: "))
 
 
exibir_dados()
juros_compostos(montante_inicial, taxa, aporte, tempo)