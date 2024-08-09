from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os
import time
import csv
import sys
import datetime
from selenium.common.exceptions import NoSuchElementException



driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
time.sleep(10)
driver.maximize_window()
time.sleep(60)

#para imprimir no log a data e horario
# Obtenha a data e hora atual
agora = datetime.datetime.now()
# Crie um formato de string para incluir data e hora no nome do arquivo
formato_data_hora = agora.strftime("%Y-%m-%d_%H-%M-%S")
# Crie o nome do arquivo com a data e hora formatadas
nome_arquivo = f"C:/arquivos-log/output_{formato_data_hora}.txt"


#Midia = imagem, pdf, documento, video (caminho do arquivo, lembrando que mesmo no windows o caminho deve ser passado com barra invertida / ) 
#midia = "C:/imagem/bomdia.jpg"


#ENCONTRAR A CAIXA PESQUISA DE CONTATO
caixa_de_pesquisa = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[3]/div/div[1]/div/div[2]/div[2]/div/div[1]")

#Função tecla tab
def tab_x(valor):
    for i in range(valor):
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB).perform()

# Função de tecla dow
def down_x(valor):
    for i in range(valor):
        actions = ActionChains(driver)
        actions.send_keys(Keys.DOWN).perform()

def enter():
    try:
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER).perform()
        print("ENTER key sent successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    time.sleep(2)

#Função escrever texto
def write_word(midia):
    actions = ActionChains(driver)
    actions.send_keys(midia).perform()
    time.sleep(1)  # Aguarda 1 segundo (ou ajuste conforme necessário)

#Função decla tab
def tab_x(valor):
    for i in range(valor):
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB).perform()

# Função de tecla dow
def down_x(valor):
    for i in range(valor):
        actions = ActionChains(driver)
        actions.send_keys(Keys.DOWN).perform()

#Funçãode enter
def enter():
    actions = ActionChains(driver)
    actions.send_keys(Keys.ENTER).perform()
    time.sleep(2)  # Aguarda 2 segundos (ou ajuste conforme necessário)

#Função escrever texto
def write_word(midia):
    actions = ActionChains(driver)
    actions.send_keys(midia).perform()
    time.sleep(1)  # Aguarda 1 segundo (ou ajuste conforme necessário)

#Funcao que envia midia como mensagem
def enviar_midia(midia):
   #driver.find_element(By.CSS_SELECTOR, "span[data-testid='attach-menu-plus']").click() #novo elemento 
   driver.find_element(By.CSS_SELECTOR, "span[data-icon='attach-menu-plus']").click() #novo elemento 11/09
   #attach = driver.find_element(By.CSS_SELECTOR, ("input[type='file']")) #elemento file
   attach = driver.find_element(By.XPATH, ("//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']")) #elemento foto e video
   attach.send_keys(midia)
   time.sleep(3)
   send = driver.find_element(By.CSS_SELECTOR, ("span[data-icon='send']"))
   send.click()    

#PERCORRER A LISTA DE TELEFONES
#ENVIAR A MENSAGEM
#layout arquivo csv
#telefones,nm,codigocliente

# Abra um arquivo de texto para escrita
#with open('C:/arquivos-log/output.txt', 'w') as file:
with open(nome_arquivo, 'w') as file:
    # Redirecione a saída padrão para o arquivo
    sys.stdout = file

    if os.path.exists('telefones.csv'):
        #with open('telefones.csv', mode='r') as csvfile:
        with open('telefones.csv', mode='r', encoding='utf-8') as csvfile:
            # Passando o arquivo CSV para o leitor CSV padrão do Python
            leitor_csv = csv.reader(csvfile)
            print(f"Abriu o arquivo csv")

            for indice, linha in enumerate(leitor_csv):
                print(f"Lendo o arquivo csv.... ")
                if indice == 0:  # cabeçalho
                    print(f"A primeira linha tem os cabeçalhos, e o primeiro campo é: {linha[0]}")
                    print(f"A primeira linha tem os cabeçalhos, e o segundo campo é: {linha[1]}")
                    print(f"A primeira linha tem os cabeçalhos, e o terceiro campo é: {linha[2]}")
                else:
                    # caixa_de_pesquisa.clear() # linha incluida 
    
                    print(f"Numero do telefone: {linha[0]}")
                    caixa_de_pesquisa.send_keys(linha[0])
                    caixa_de_pesquisa.send_keys(Keys.ENTER)
                    time.sleep(2)

                    ### if para verificar encontra o número do telefone nos contatos do whats
                    try:
                        print (f"entrou aquii no try")
                        caixa_de_msg = driver.find_element(By.CSS_SELECTOR, "div[title='Mensagem']")
                        time.sleep(1)
                        
                        print(f"Nome contato: {linha[1]}")

                        ###exemplo de mensagem com uma linha
                        mensagem = f"{linha[1]} Essas são as notícias de hoje...Novo teste - Um abençoado dia :)"

                        ### string multiplas linhas --- utilizar aspas tripas e para quebra de linha \n
                        #mensagem = f"""{linha[1]} Essas são as notícias de hoje...Novo teste - Um abençoado dia \n
                        #           continuando a mensagem na outra linha\n
                        #           continuando... \n
                        #           continuando... \n."""

                        
                        #se desejar o envio da midia antes da mensagem de texto
                        enviar_midia(midia)
                        time.sleep(3)

                        caixa_de_msg.send_keys(mensagem)
                        print(f"Nome contato Mensagem OK: {linha[1]}")
                        print(f"Código dizimista Mensagem OK: {linha[2]}")
                        time.sleep(6) #diminui para 3 sleep dia 03/06

                        #se desejar o envio da midia após a msg de texto                
                        #enviar_midia(midia)
                        #time.sleep(3)

                        time.sleep(5) # aumentei para 5 dia 08/08
                        ActionChains(driver).send_keys(Keys.ESCAPE).perform() #inclui dia 08/08
                        print (f"Entrou aquii no ESCAPE")
                        time.sleep(4) #diminui para 4 dia 29/05

                        # LIMPAR A CAIXA DE PESQUISA
                        caixa_de_pesquisa.click()                       
                        time.sleep(1) #INCLUI ESSA LINHA 13/09
                        ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                
                    except NoSuchElementException:
                        print (f"Entrou aquii no except")
                        print(f"Telefone contato no except: {linha[0]}")
                        print(f"Nome contato no except: {linha[1]}")
                        print(f"Código dizimista no except: {linha[2]}")
                        driver.find_element(By.XPATH, "//*[@id='pane-side']/div").click() #novo elemento 
                        time.sleep(1)

                        # LIMPAR A CAIXA DE PESQUISA
                        caixa_de_pesquisa.click()
                        ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                        time.sleep(1)
                        continue
                # Recomeçar
                time.sleep(4) #diminui para 4 dia 29/05
    else:
        print(f"Erro ao tentar abrir o arquivo csv")

    # Encerra o webdriver
    driver.quit()

# Lembre-se de restaurar a saída padrão para o terminal após terminar de escrever no arquivo
sys.stdout = sys.__stdout__

print(f"O arquivo '{nome_arquivo}' foi criado com sucesso.")