cont_a = 0
soma_idade = 0
cont_pessoas_ruim = 0
cont_pessoas_pessimo = 0
maior_idade_bom = 0.00
menor_idade_regular = 121
menor_idade_ruim = 121
media_idade_ruim = 0
porcentagem_pessimo = 0
dif_idade = 0

for pessoas in range(1,101,1):
    idade = int(input("Digite sua idade(superior ou igual a 14 anos):"))
    while idade < 14 or idade > 120:
        print("Idade Inválida!!")
        idade = int(input("Digite sua idade(superior ou igual a 14 anos):"))

    print("\n\nNota                 Significado ")
    print(" A                      Ótimo        ")
    print(" B                      Bom          ")
    print(" C                      Regular      ")
    print(" D                      Ruim         ")
    print(" E                      Péssimo    \n")

    opiniao = input("Digite sua opnião segundo a tabela a cima:").upper()

    while (opiniao != "A" and opiniao != "B" and opiniao != "C" and opiniao != "D" and opiniao != "E"):
        print("Nota Inválida!!")
        opiniao = input("Digite sua opnião segundo a tabela a cima:").upper()


    if opiniao == "A":
        cont_a += 1

    if opiniao == "D":
        soma_idade = soma_idade + idade
        cont_pessoas_ruim += 1

    if opiniao == "E":
        cont_pessoas_pessimo += 1 

    if opiniao == "B" and idade > maior_idade_bom:
        maior_idade_bom = idade
    

    if opiniao == "C" and idade < menor_idade_regular:
        menor_idade_regular = idade

    if opiniao == "D" and idade < menor_idade_ruim:
        menor_idade_ruim = idade

print("n\nFormulario Encerrado!!n\n")


if cont_pessoas_ruim > 0:
 media_idade_ruim = soma_idade / cont_pessoas_ruim


if cont_pessoas_pessimo > 0:
  porcentagem_pessimo = (cont_pessoas_pessimo * pessoas)/100


if menor_idade_regular >= menor_idade_ruim:

 dif_idade = menor_idade_regular - menor_idade_ruim

else:
    dif_idade = menor_idade_ruim - menor_idade_regular


print("a-)A quantidade de resposta ótimo é de:",cont_a)
print("b-)A média de idade das pessoas que responderam Ruim de:",media_idade_ruim)
print("c-)A porcentagem de respostas Péssimo é de:",porcentagem_pessimo,"%")
print("d-)A maior idade entre as pessoas que responderam Bom é de:",maior_idade_bom)
print("e-)a diferença entre a menor idade que respondeu Regular e a menor idade que respondeu Ruim é de:",dif_idade,"anos")

