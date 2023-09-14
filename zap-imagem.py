from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os
import time
import csv

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
time.sleep(60)


#Midia = imagem, pdf, documento, video (caminho do arquivo, lembrando que mesmo no windows o caminho deve ser passado com barra invertida */* ) 
midia = "C:/imagem/bomdia.jpg"


#ENCONTRAR A CAIXA PESQUISA DE CONTATO
caixa_de_pesquisa = driver.find_element(By.CSS_SELECTOR, "div[title='Caixa de texto de pesquisa']")

#Funcao que envia midia como mensagem
def enviar_midia(midia):
   driver.find_element(By.CSS_SELECTOR, "span[data-testid='attach-menu-plus']").click() #novo elemento 
   attach = driver.find_element(By.CSS_SELECTOR, ("input[type='file']"))
   attach.send_keys(midia)
   time.sleep(3)
   send = driver.find_element(By.CSS_SELECTOR, ("span[data-icon='send']"))
   send.click()    

#PERCORRER A LISTA DE TELEFONES
#ENVIAR A MENSAGEM
#layout arquivo csv
#telefones,nm,codigocliente

if os.path.exists('telefones.csv'):
    with open('telefones.csv', mode='r') as csvfile:
        # Passando o arquivo CSV para o leitor CSV padrão do Python
        leitor_csv = csv.reader(csvfile)
        print(f"Abriu o arquivo csv")

        for indice, linha in enumerate(leitor_csv):
            print(f"Lendo o arquivo csv.... ")
            if indice == 0:  # cabeçalho
                print(f"A primeira linha tem os cabeçalhos, e o primeiro campo é: {linha[0]}")
                print(f"A primeira linha tem os cabeçalhos, e o segundo campo é: {linha[1]}")
            else:
                caixa_de_pesquisa.clear() # linha incluida 
                print(f"Numero do telefone: {linha[0]}")
                caixa_de_pesquisa.send_keys(linha[0])
                caixa_de_pesquisa.send_keys(Keys.ENTER)
                time.sleep(2)
                
                caixa_de_msg = driver.find_element(By.CSS_SELECTOR, "div[title='Mensagem']")
                time.sleep(1)
                
                print(f"Nome contato: {linha[1]}")
<<<<<<< HEAD
                mensagem = f"{linha[1]} Essas são as notícias de hoje...Novo teste - Um abençoado dia :)"
=======

                ###exemplo de mensagem com uma linha
                #mensagem = f"{linha[1]} Essas são as notícias de hoje...Novo teste - Um abençoado dia :)"

                ### string multiplas linhas --- utilizar aspas tripas e para quebra de linha \n
              #  mensagem = f"""{linha[1]} Essas são as notícias de hoje...Novo teste - Um abençoado dia \n
               #                           continuando a mensagem na outra linha\n
               #                           continuando... \n
               #                           continuando... \n:)"""

                ### string multiplas linhas --- utilizar aspas tripas e para quebra de linha \n
                mensagem = f"""Prezado(a) {linha[1]}, \n
                               Paz e bem!\n
                               Mantenha-se conectado conosco! Salve o contato do Dízimo Paroquial (11) 4595-7272\n
                               para continuar recebendo nossas mensagens e comunicados importantes da Paróquia Nossa Senhora de Lourdes.\n\n
                               Convidamos você e sua família para o Tríduo em honra à nossa padroeira, a Comunidade Rainha dos Apóstolos, Jardim Bertioga.\n
                               De 19 a 22 de agosto de 2023.\n\n 
                               Veja a programação:\n\n
                               Dia 19 - Sábado\n
                               Tema: Maria, Rainha dos Apóstolos, modelo de vocação.\n
                               Terço às 17h30\n
                               Missa Assunção de Nossa Senhora (Vigília) às 18h00\n\n
                               Dia 20 - Domingo\n
                               Tema: Maria, Rainha dos Apóstolos, vocação é graça de Deus.\n
                               Terço às 7h30\n
                               Missa Assunção de Nossa Senhora (Dia) às 8h00\n\n
                               Dia 21 - Segunda-feira\n
                               Tema: Maria, Rainha dos Apóstolos, vocação é missão.\n
                               Terço às 19h00\n
                               Santa Missa às 19h30\n\n
                               Dia 22 - Terça-feira\n
                               Concentração para Procissão na Comunidade Nossa Senhora de Guadalupe (Jd. Aimoré) às 18h00\n
                               Missa e Coroação da Rainha dos Apóstolos às 18h30\n\n
                               Será um momento especial de reflexão e celebração. Agradecemos sua presença!\n
                               Para continuar recebendo nossas mensagens, responda "SIM". Caso contrário, \n
                               se não desejar mais receber, responda com um "NÃO". \n
                               Agradecemos por fazer parte da nossa comunidade.\n\n
                               Desejamos muitas bênçãos,\n
                               Equipe Dízimo da Paróquia Nossa Senhora de Lourdes\n:)"""

>>>>>>> origin/master

                caixa_de_msg.send_keys(mensagem)
                time.sleep(1)
                
                enviar_midia(midia)
                time.sleep(1)
                
                caixa_de_msg.send_keys(Keys.ENTER)
                time.sleep(1)
        

            # LIMPAR A CAIXA DE PESQUISA
            caixa_de_pesquisa.click()
            ActionChains(driver).send_keys(Keys.ESCAPE).perform()

            # Recomeçar
            time.sleep(5)
else:
  print(f"Erro ao tentar abrir o arquivo csv")

# Encerra o webdriver
driver.quit()