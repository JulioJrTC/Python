"""Desafio 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionario com as seguintes informações:

- Quantidade de notas

- A maior nota

- A menor nota

- A média da turma

- A situação (opcional)

Adicione tambem as docstrings da função."""

def notas(*n,sit=True):
    
    #Dicionario
    nota={"Quantidade de notas":[],"Maior Nota":[],"Menor Nota":[],"Media de notas":[],"Situação":[]}
    
    #Indentificando a quantidade de notas inseridas como metodos
    quantNotas=len(n)
    nota["Quantidade de notas"].append(quantNotas)

    #Identificando maior e menor nota
    maiorNota=max(n)
    menorNota=min(n)
    nota["Maior Nota"].append(maiorNota)
    nota["Menor Nota"].append(menorNota)

    #Identificando media de notas
    mediaNotas=(maiorNota+menorNota)/2
    nota["Media de notas"].append(mediaNotas)
    print(f"Media de notas: {mediaNotas}")

    if sit:
        if mediaNotas<5.0:
            nota["Situação"].append("REPROVADO")            
        elif mediaNotas > 5.0 and mediaNotas <=6.9:            
            nota["Situação"].append("RECUPERAÇÃO")
        else:            
            nota["Situação"].append("APROVADO")
            
    
    
    return nota

print(notas(2.5,7.9,10,2.1,sit=False))