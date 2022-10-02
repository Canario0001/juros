#!/usr/bin/env python3
def header(num):
        print('┅'*num)

def capital(j, i, t):
    return j / (i *  t)

def montante(c, j):
    return c + j

def juros(c, i, t):
    return c * i * t

def taxa(j, c, t):
    return j / (c * t)

def tempo(j, c, i):
    return j / (c * i)

def lista():
    print('\n\nA lista estará da seguinte maneira:\nabreviação: o que significa\nDigite no formato abreviação:valor\n')
    print('j: Juros\nc: Capital (quantia inicial)')
    print('i: Taxa (tem que estar na mesma medida que o tempo, se for mensal o tempo será em meses) (além disso, deve estar em porcentagem)\n(coloque OBRIGATORIAMENTE em porcentagem (não precisa do sinal). Decimal vai quebrar tudo)')
    print('t: Tempo (tem que estar na mesma medida que a taxa)\nm: Montante (Capital + Juros)')

def jeremias(j, c, i, t, m):
    # j → juros
    # c → capital
    # i → taxa
    # t → tempo
    # m → montante
    
    err = 'Não foi possível encontrar.'
    
    if not j:
        try:
            j = juros(c, i, t)
        except (ValueError, TypeError):
            try:
                j = m - c
            except (ValueError, TypeError):
                j = err

    if not c:
        try:
            c = capital(j, i, t)
        except (ValueError, TypeError):
            try:
                c = m - j
            except (ValueError, TypeError):
                c = err

    if not i:
        try:
            i = taxa(j, c, t)
        except (ValueError, TypeError):
            i = err

    if not t: 
        try:
            t = tempo(j, c, i)
        except (ValueError, TypeError):
            t = err

    if not m: 
        try:
            m = montante(c, j)
        except (ValueError, TypeError):
            m = err

    result = {
            'j': j,
            'c': c,
            'i': i*100,
            't': t,
            'm': m
    }

    if i == err: result['i'] = err

    return result

def anotar(nome, resultado):
    texto = f'Resultados\n\nJuros: R${resultado["j"]}\nCapital: R${resultado["c"]}\nTaxa: {resultado["i"]}%\nTempo: {resultado["t"]}\nMontante: R${resultado["m"]}\n'
    with open(f'{nome}.txt', 'w') as f: f.write(texto)

def main():
    header(35)
    print('  Calculadora de Juros Simples!')
    header(35)
    print('\nDeseja ver a lista de abreviações ou quer começar agora?\n')
    print('[0] - Ver a lista de abreviações\n[1] - Começar sem ver a lista\n')
    choice = int(input('>>> '))
    if choice == 0: lista()
    elif choice == 1: pass
    else:
        print('Insira um valor válido. Tente novamente.')
        exit()

    j = None
    c = None
    i = None
    t = None
    m = None
    print('\n\nDigite as informações que você possui de acordo com a lista de abreviações. Digite "q" se tiver terminado.\n')
    while True:
        # comp → composto
        comp = input('>>> ').strip().lower()
        if comp == 'q': break

        if comp.startswith('j'):
            _, j = comp.split(':')
            j = float(j)

        elif comp.startswith('c'):
            _, c = comp.split(':')
            c = float(c)

        elif comp.startswith('i'):
            _, i = comp.split(':')
            i = float(i)
            i = i/100

        elif comp.startswith('t'):
            _, t = comp.split(':')
            t = float(t)

        elif comp.startswith('m'):
            _, m = comp.split(':')
            m = float(m)

        else: print('Digite uma informação válida!')

    resultado = jeremias(j, c, i, t, m)
    print('\n')
    header(30)
    print('  Resultados')
    header(30)
    print('')
    print(f'  Juros: R${resultado["j"]}')
    print(f'  Capital: R${resultado["c"]}')
    print(f'  Taxa: {resultado["i"]}%')
    print(f'  Tempo: {resultado["t"]}')
    print(f'  Montante: R${resultado["m"]}')
    print('\n\nVocê quer escrever os resultados num arquivo de texto?\n\n[0] - Sim\n[1] - Não\n')
    choice = int(input('>>> ').strip())
    if choice == 0:
        print('\nQual será o nome do arquivo?\n')
        nome = input('>>> ').strip()
        anotar(nome, resultado)
        print(f'\nResultados salvos no arquivo {nome}.txt!')
    elif choice == 1: pass
    else: print('Opção inválida. Operação cancelada.')

    print('\nObrigado por usar!\nFeito por: Cristian (aka Canário)')

if __name__ == '__main__':
    main()
