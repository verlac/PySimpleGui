import PySimpleGUI as sg

valor = 0
cotacao = 0

# Criando o layout da janela principal
layout_janela_principal = [
    # primeira linha da janela
    [sg.Text('Pegar Cotação da Moeda')],
    # segunda linha da janela, que vai mostrar o campo pro usuário digitar uma moeda
    [sg.InputText()],
    # terceira linha, onde vão aparecer dois botões
    [sg.Button('Pegar Cotação'), sg.Button('Cancelar')],
    # quarta linha, onde vai exibir o valor da cotação para a moeda informada pelo usuário
    [sg.Text(f'A cotação do valor {valor} é {cotacao}.')],
]

# Código que vai exibir a janela com o layout definido acima
janela = sg.Window('Aqui vai o título da janela', layout_janela_principal)

# Lógica do programa
while True:
    # read() é a função que vai observar/capturar todos os eventos que acontecerem na janela e atribuí-los à variável 'evento'. E os valores que forem informados serão atribuídos à variável 'valores'.
    evento, valores = janela.read()

    # sg.WIN_CLOSED se refere ao 'X' de fechar janela, que aparece canto superior direito da janela (no Windows)
    # SE o 'evento' for igual ao click do mouse no 'botão fechar' ou no botão 'Cancelar', o programa vai ser interrompido
    if evento == sg.WIN_CLOSED or evento == 'Cancelar':
        break

janela.close()