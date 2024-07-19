# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login


# importar as bibliotecas
    # autigui para automatizar o teclado e o mouse
    # pandas para ler a base de dados
    # time para dar um tempo entre as ações
import pyautogui
import time
import pandas as pd

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
# pyautogui.PAUSE -> define pausa entre os comandos em segundos
pyautogui.PAUSE = 0.6

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# intervalo de segurança para o carregamento da página
time.sleep(5)

# entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# intervalo de segurança para o carregamento da página
time.sleep(3)


# Passo 2: Fazer login
# selecionar o campo de email na tela com o mouse

screen_width, screen_height = pyautogui.size() # descobrir o tamanho da tela
x = int(screen_width * 0.5) # 50% da tela
y = int(screen_height * 0.45) # 45% da tela
pyautogui.click(x=x, y=y) # clicar no campo de email com base na posição relariva da tela


# escrever o seu email
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("sua senha")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.press("enter")# clique no botao de login
time.sleep(3)

# Passo 3: Importar a base de produtos pra cadastrar


tabela = pd.read_csv("Aula 1/produtos.csv")

print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index: # Passo 5: Repetir o processo de cadastro até o fim da base de dados
    # clicar no campo de código
    x = int(screen_width * 0.5) # 50% da tela
    y = int(screen_height * 0.3) # 30% da tela
    pyautogui.click(x=x, y=y) # clicar no campo de codigo com base na posição relariva da tela

    # pegar da tabela o valor do campo que a gente quer preencher
    for coluna in tabela.columns:  # Repetir o processo de cadastro para cada coluna da base de dados
        valor = str(tabela.loc[linha, coluna]) if not pd.isnull(tabela.loc[linha, coluna]) else ""

        pyautogui.write(valor)  # Escrever o valor da célula
        pyautogui.press("tab")  # Passar para o próximo campo

    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(screen_width)
