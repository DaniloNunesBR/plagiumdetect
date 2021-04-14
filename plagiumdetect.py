import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    valor_total = 0
    var = 0
    while var <= 5:
        valor = as_a[var] - as_b[var]
        if valor < 0:
            valor = valor * -1
            var = var + 1
            valor_total = valor_total + valor
        else:
            valor_total = valor_total + valor
            var = var + 1

    grau_similaridade = valor_total/6
    return grau_similaridade
    
    pass

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    #tamanho médio das palavras
    lista_sentencas = separa_sentencas(texto)
    
    lista_frases = []
    for x in lista_sentencas:
        lista_frases = lista_frases + separa_frases(x)
        
    lista_palavras = []
    for x in lista_frases:
        lista_palavras = lista_palavras + separa_palavras(x)
        
    tamanho_palavras = 0
    num_palavras = len(lista_palavras)
    for x in lista_palavras:
        tamanho_palavras = tamanho_palavras + len(x)
    media = tamanho_palavras/num_palavras

    #Relação Type-Token
    palavras_diferentes = n_palavras_diferentes(lista_palavras)
    type_token = palavras_diferentes/num_palavras

    #Razão Hapax Legomana
    palavras_unicas = n_palavras_unicas(lista_palavras)
    hapax_legomana = palavras_unicas/num_palavras

    #Tamanho médio de sentença
    tamanho_sentencas = 0
    for x in lista_sentencas:
        tamanho_sentencas = tamanho_sentencas + len(x)
    num_sentencas = len(lista_sentencas)
    media_sentenca = tamanho_sentencas/num_sentencas

    #Complexidade de sentença
    num_frases = len(lista_frases)
    complexidade_sentenca = num_frases/num_sentencas

    #Tamanho médio de frase
    tamanho_frase = 0
    for x in lista_frases:
        tamanho_frase = tamanho_frase + len(x)
    media_frase = tamanho_frase/num_frases

    return [media, type_token, hapax_legomana, media_sentenca, complexidade_sentenca, media_frase]
    pass

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    grau_similaridade = 999
    copiah = 0
    iteração = 0
    for x in textos:
        as_a = calcula_assinatura(x)
        as_b = ass_cp
        grau = compara_assinatura(as_a, as_b)
        iteração = iteração + 1
        if grau < grau_similaridade:
            copiah = iteração
            grau_similaridade = grau
    print("O texto",copiah,"é o que possui mais similaridade com o texto principal !")
    pass   

def main():
    a = calcula_assinatura(input("Digite o texto principal: "))
    b = le_textos()
    avalia_textos(b, a)
main()
