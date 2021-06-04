def jogador(tabuleiro):
    quantidade_x = 0
    quantidade_o = 0
    for i in tabuleiro:
        for j in i:
            if j == 'X':
                quantidade_x += 1
            elif j == 'O':
                quantidade_o += 1
    if quantidade_x > quantidade_o:
        return 'O'
    return 'X'

def acoes(tabuleiro):
    acoes_permitidas = []
    for row, i in enumerate(tabuleiro):
        for col, j in enumerate(i):
            if j == ' ':
                acoes_permitidas.append((row,col)) #row and column
    return acoes_permitidas

def resultado(tabuleiro, acao):
    row, col = acao
    novo_tabuleiro = [row[:] for row in tabuleiro] #making an "deep" copy of the matrix tabuleiro
    player_mark = jogador(tabuleiro)
    novo_tabuleiro[row][col] = player_mark
    return novo_tabuleiro

def ganhador(tabuleiro):
    rows_check = 0
    cols_check = [0,0,0]
    diagonal_check = [0,0]
    for i in tabuleiro:

        #checking the columns
        for k in range(3):
            if i[k] == 'X':
                cols_check[k] += 1
            if i[k] == 'O':
                cols_check[k] -= 1

        #checking the rows
        rows_check = 0
        for j in i:
            if j == 'X':
                rows_check += 1
            elif j == 'O':
                rows_check -= 1
        if rows_check == 3:
            return 'X'
        if rows_check == -3:
            return 'O'

    for k in range(3):
        if cols_check[k] == 3:
            return 'X'
        elif cols_check[k] == -3:
            return 'O'
        
    #checking the diagonal
    for i in range(3):
        if tabuleiro[i][i] == 'X':
            diagonal_check[0] += 1
        elif tabuleiro[i][i] == 'O':
            diagonal_check[0] -=1

        if tabuleiro[i][2-i] == 'X':
            diagonal_check[1] += 1
        elif tabuleiro[i][2-i] == 'O':
            diagonal_check[1] -= 1
    
    for i in range(2):
        if diagonal_check[i] == 3:
            return 'X'
        elif diagonal_check[i] == -3:
            return 'O'
    return ' '

def final(tabuleiro):
    win = ganhador(tabuleiro)
    end = True
    for i in tabuleiro:
        for j in i:
            if j == ' ':
                end = False

    if end or win != ' ': # If there are no more free positions or someone wins
        return True
    return False

def custo(tabuleiro):
    win = ganhador(tabuleiro)
    if win == 'X':
        return 1
    elif win == 'O':
        return -1
    return 0

def maxValor(tabuleiro):
    acao_escolhida = None
    valor_escolhido = -1
    acoes_permitidas = acoes(tabuleiro)
    if final(tabuleiro) == False:
        if len(acoes_permitidas) > 1:
            for acao in acoes_permitidas:
                acao_retorno, valor_retorno = minimax(resultado(tabuleiro, acao))
                if valor_retorno >= valor_escolhido:
                    valor_escolhido = valor_retorno
                    acao_escolhida = acao_retorno
            return acao_escolhida, valor_escolhido

        else:
            return acoes_permitidas[0], custo(resultado(tabuleiro,acoes_permitidas[0]))
    else:
        return None, -1

def minValor(tabuleiro):
    acao_escolhida = None
    valor_escolhido = 1
    acoes_permitidas = acoes(tabuleiro)
    if final(tabuleiro) == False:
        if len(acoes_permitidas) > 1:
            for acao in acoes_permitidas:
                acao_retorno, valor_retorno = minimax(resultado(tabuleiro, acao))
                if valor_retorno <= valor_escolhido:
                    valor_escolhido = valor_retorno
                    acao_escolhida = acao_retorno
            return acao_escolhida, valor_escolhido

        else:
            return acoes_permitidas[0], custo(resultado(tabuleiro,acoes_permitidas[0]))
    else:
        return None, 1

def minimax(tabuleiro):
    player = jogador(tabuleiro)
    if player == 'X':
        acao, valor = maxValor(tabuleiro)
        return acao
    elif player == 'O':
        acao, valor = minValor(tabuleiro)
        return acao

tabuleiro = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
a = [['X',' ',' '],[' ',' ',' '],[' ',' ',' ']]