import re
import fileinput

#EXPRESSOES REGULARES
operadores = re.compile("\+|-|\*\*|\*|>=|>|<=|<|==|=|\(|\)|:|[][]|,")
stringR1 = re.compile(r'r"(.*?)"')
stringR2 = re.compile(r"r'(.*?)'")
string1 = re.compile(r'"(\\.|[^\\"])*"')
string2 = re.compile(r"'(\\.|[^\\'])*'")
numero = re.compile("[0-9]+")
nomes = re.compile("[a-zA-Z][a-zA-Z0-9]*")
espacos = re.compile(r"\s+")          
comentario = re.compile("#.*")
ponto = re.compile("[.]")
#EXPRESSOES REGULARES

#IMPLEMENTACAO
for line in fileinput.input(): #ler o arquivo na linha de comando
    i = 0

    while i < len(line):
        m = numero.match(line[i:]) #expressao regular de numeros
        if m:
            print("NUMERO", m.group(0))
            i += m.end()
            continue
        
        m = espacos.match(line[i:]) #expressao regular de espacos
        if m:
            print("SPACE", m.group(0))
            i += m.end()
            continue

        m = stringR1.match(line[i:]) #expressao regular de strings cruas com aspas duplas
        if m:
            print("RAW STRING", m.group(0))
            i += m.end()
            continue

        m = stringR2.match(line[i:]) #expressao regular de strings cruas com aspas simples
        if m:
            print("RAW STRING", m.group(0))
            i += m.end()
            continue

        m = nomes.match(line[i:]) #expressao regular de nomes
        if m:
            print("NOME", m.group(0))
            i += m.end()
            continue

        m = operadores.match(line[i:]) #expressao regular de nomes
        if m:
            print("OPERADOR", m.group(0))
            i += m.end()
            continue

        m = comentario.match(line[i:]) #expressao regular de nomes
        if m:
            print("COMENTARIO", m.group(0))
            i += m.end()
            continue

        m = string1.match(line[i:]) #expressao regular de strings com aspas duplas
        if m:
            print("STRING", m.group(0))
            i += m.end()
            continue

        m = string2.match(line[i:]) #expressao regular de strings com aspas simples
        if m:
            print("STRING", m.group(0))
            i += m.end()
            continue

        m = ponto.match(line[i:]) #expressao para um ponto
        if m:
            print("PONTO", m.group(0))
            i += m.end()
            continue
