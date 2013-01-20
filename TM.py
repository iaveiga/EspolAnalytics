#mi propia implementación de las funciones a usar para textmining



'''
Devuelve el corpus de una lista
'''
def corpus(ls):
    corpus = []
    for i in range(0,len(ls)):
        ls[i] = ls[i].split()
        for word in ls[i]:
            corpus.append(word)
    return corpus


'''
Devuelve un conjunto de términos
'''
def tdm(corpus):
    tdm = []
    tdm = set(corpus)
    return set(corpus)

#usando el corpus y el tdm se saca la frecuencia de las palabras para
#dibujar el tag cloud
'''
Carga las palabras vacías desde el archivo spanish.dat
y retorna un conjunto de dichas palabras.
'''
def loadSW():
    sw = []
    f = open("spanish.dat","r",encoding="utf8")
    for line in f:
        sw.append(line)
    f.close()
    for i in range(0,len(sw)):
        sw[i] = sw[i].rstrip("\n")
    return set(sw)

'''
Retorna la frecuencia de términos
'''

def frequence(corpus,tdm):
    freq = dict()
    while len(tdm) != 0:
            word = tdm.pop()
            freq.update({word:corpus.count(word)})
    return freq
