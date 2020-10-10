def format_impressao (renda_total, total_moradia, total_educacao, total_transporte):

  ''' Essa função formata os valores e imprime na tela.'''

  rendaa = format(renda_total,".2f")
  renda_f = str(rendaa).replace(".",",")
  moradia = format(total_moradia,".2f")
  moradia_f = str(moradia).replace(".",",")
  educacaoo = format(total_educacao,".2f")
  educacao_f = str(educacaoo).replace(".",",")
  transporte = format(total_transporte,".2f")
  transporte_f = str(transporte).replace(".",",")
  print()
  print()
  print()
  print("+=" * 25)
  print(f"Dados Mensais")
  print("+=" * 25)
  print(f"Sua renda mensal total: R$ {renda_f}.")
  print(f"Seus gastos totais com moradia: R$ {moradia_f}.")
  print(f"Seus gastos totais com educação: R$ {educacao_f}.")
  print(f"Seus gastos totais com transporte: R$ {transporte_f}.") 



def diagnostico_financeiro (renda_total, total_moradia, total_educacao, total_transporte):

  ''' Essa função demonstra o diagnóstico financeiro com base nos dados informados.'''

  print()
  print()
  print()
  print("+=" * 70)
  print(f"Diagnóstico Financeiro")
  print("+=" * 70)

  p_moradia = (total_moradia / renda_total)*100
  percentual_m = round(p_moradia,1)
  p_educacao = (total_educacao / renda_total)*100
  percentual_e = round(p_educacao,1)
  p_transporte = (total_transporte / renda_total)*100
  percentual_t = round(p_transporte,1)
 
  maxm = (renda_total * 0.3)
  fmaxm = format(maxm,".2f")
  maxmf = str(fmaxm).replace(".",",")

  maxe = (renda_total * 0.2)
  fmaxe = format(maxe,".2f")
  maxef = str(fmaxe).replace(".",",")

  maxt = (renda_total * 0.15)
  fmaxt = format(maxt,".2f")
  maxtf = str(fmaxt).replace(".",",")

  if p_moradia <= 30 and p_educacao <= 20 and p_transporte <= 15:
    print(f'Os seus gastos estão dentro da margem recomendada! Continue assim e garantirá uma boa saúde financeira.')
  else:
    if p_moradia > 30:
      print(f'Seus gastos totais com moradia comprometem {percentual_m}% de sua renda total. O máximo recomendado é de 30%. Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R${maxmf}.') 
    else:
      print(f'Seus gastos com moradia estão dentro da margem recomendada.') 
    if p_educacao > 20:
      print(f'Seus gastos totais com educação comprometem {percentual_e}% de sua renda total. O máximo recomendado é de 20%. Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R${maxef}.') 
    else:
      print(f'Seus gastos com educação estão dentro da margem recomendada.') 
    if p_transporte > 15:
      print(f'Seus gastos totais com transporte comprometem {percentual_t}% de sua renda total. O máximo recomendado é de 15%. Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R${maxtf}.') 
    else:
      print(f'Seus gastos com transporte estão dentro da margem recomendada.') 
  soma = total_moradia + total_educacao + total_transporte
  if soma > renda_total:
    print()
    print()
    print("#" * 10)
    valoracima = soma - renda_total
    acimaformatada = format((valoracima),".2f")
    printacima = str(acimaformatada).replace(".",",")
    print(f"Seus gastos mensais superam em R${printacima} seus ganhos mensais. Isso significa que você está acumulando dívidas. Cuide de suas finanças.")
  


  

renda_total = float(input(f"Informe sua renda total mensal: "))
if renda_total <= 0:
  while (renda_total <= 0):
    renda_total = float(input(f"O valor de sua renda total mensal deve ser superior a zero. Informe um valor válido para sua renda total mensal: "))
total_moradia = float(input(f"Informe seu gasto mensal total com moradia: "))
if total_moradia < 0:
  while (total_moradia < 0):
    total_moradia = float(input(f"O valor de sue gasto mensal com moradia deve ser maior ou igual a zero. Informe um valor válido para o seu gasto mensal com moradia: "))
total_educacao = float(input(f"Informe seu gasto mensal total com educação: "))
if total_educacao < 0:
  while (total_educacao < 0):
    total_educacao = float(input(f"O valor de sue gasto mensal com educação deve ser maior ou igual a zero. Informe um valor válido para o seu gasto mensal com educação: "))
total_transporte = float(input(f"Informe seu gasto mensal total com transporte: "))
if total_transporte < 0:
  while (total_transporte < 0):
    total_transporte = float(input(f"O valor de sue gasto mensal com transporte deve ser maior ou igual a zero. Informe um valor válido para o seu gasto mensal com transporte: "))   
 


format_impressao (renda_total, total_moradia, total_educacao, total_transporte)
diagnostico_financeiro (renda_total, total_moradia, total_educacao, total_transporte)