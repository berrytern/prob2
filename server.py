import math
import scipy.stats as st

print("""
Questão 1:
Um criador tem constatado uma proporção de 10% do rebanho com verminose. O
veterinário alterou a dieta dos animais e acredita que a doença diminuiu de
intensidade. Um exame em 100 cabeças do rebanho, escolhidas ao acaso, indicou 8
delas com verminose. Ao nível de 8%, há indícios de que a proporção diminuiu?""")

p = 0.1
n = 100
po = 8/n
a = 0.08
Z = (po-p)/(math.sqrt((p*(1-p))/n))
print(f"Z = {Z}")
print(f"RC = Z < {st.norm.ppf(a)}")
if (Z < st.norm.ppf(a)):
    print("Hipotese nula Rejeitada")
else:
    print("""Hipotese nula aceita.\n\tAdotando um nível de signicância de 8% concluímos a partir da
amostra que a proporção do rebanho com verminose tem indícios de diminuição com
a nova dieta.""")

"""
Questão 2:
Sabe-se que o tempo necessário para percorrer uma determinada rota no final da tarde
pode ser estudado por um modelo Normal com desvio padrão de 17 min. Foram
instalados sensores para controlar o tempo de abertura dos semáforos presentes na
rota, e deseja-se verificar se o tempo gasto para completar o percurso diminuiu.
Estudos anteriores indicam que o tempo deve continuar se comportando segundo um
modelo Normal, com mesmo desvio padrão. Com os sensores desativados, 11
veículos de mesmo ano e marca, denominado Grupo Controle, tiveram o tempo gasto
no percurso anotado. Em seguida, os sensores foram ativados e outros 13 veículos
(Grupo Teste) percorreram a mesma rota. Os tempos observados, em minutos, foram
os seguintes:

Indique se o uso dos sensores contribui para diminuir o tempo médio de percurso
utilizando o nível de 5%."""

d = 17 # min
n1 = 11
n2 = 13
t1 = [38,26,20,70,16,26,38,32,45,49,32]
X1 = sum(t1)/len(t1)
d1 = sum([i-(sum(t1)/len(t1)) for i in t1])/(len(t1)-1)
t2 = [17,31,28,21,50,21,20,51,10,22,18,35,29]
X2 = sum(t2)/len(t2)
d2 = sum([i-(sum(t2)/len(t2)) for i in t2])/(len(t2)-1)
Z = ((X1 - X2) - 0)/math.sqrt((d**2/n1)+(d**2/n2))
print(f"Zobs = {Z}")
ncdf = 1-st.norm.cdf(Z)
print(f"""
Com um nível descritivo de α∗ = {ncdf}, temos que, não há evidências o suficiente para sugerir que o efeito do uso dos sensores
na diminuição do tempo para um nível de significância a um nível de 5%.
""")
"""
Questão 3:
Você quer comprar um forno de micro-ondas e escolherá o Modelo A se os custos de
reparo forem mais baixos que os custos de reparo do Modelo B. Você pesquisa os
custos de reparo de 47 fornos do Modelo A e 55 fornos do Modelo B. O custo médio
do reparo do modelo A é $ 75 e, do modelo B, $ 80. Ao nível de 1%, você compraria o
Modelo A? Considere que o desvio padrão populacional para o modelo A é $ 12,50 e
para o modelo B é $ 20."""

"""
Questão 4:
Uma amostra com 10 observações de uma variável aleatória Normal forneceu média
de 5,5 e variância amostral 4. Deseja-se testar, ao nível de significância de 5%, se a
média na população é igual ou é menor que 6. Qual é a conclusão?"""

"""
Questão 5:
Em uma pesquisa sobre possuidores de videocassete, encontram-se 120 das 200
casas pesquisadas do bairro X e 240 das 500 residências do bairro Y. Há diferença
significativa entre a proporção de possuidores de vídeo nos dois bairros a um nível de
10%?"""