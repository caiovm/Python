def situacao_eleitoral (idade):
    if idade < 16:
      print ()
      print ("=-" * 30)
      print(f"Não tem direito a voto.")
      print ("=-" * 30)
    elif idade >= 16 and idade < 18 or idade >= 70:
      print ()
      print ("=-" * 30)
      print (f"Não tem obrigação de votar.")
      print ("=-" * 30)
    elif idade >= 18 and idade < 70:
      print ()
      print ("=-" * 30)
      print(f"Tem obrigação de votar.")
      print ("=-" * 30)
idade = int(input(f"Informe a idade do(a) cidadão(ã): "))
if idade <= 0:
  while idade < 0:
    idade = int(input(f"O valor informado não é uma idade válida. Informe um valor maior que zero:"))
situacao_eleitoral(idade)