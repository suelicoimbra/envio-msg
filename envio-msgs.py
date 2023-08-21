from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os
import time
import csv
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
time.sleep(60)


#Midia = imagem, pdf, documento, video (caminho do arquivo, lembrando que mesmo no windows o caminho deve ser passado com barra invertida */* ) 
#midia = "C:/imagem/bomdia.jpg"
midia = "C:/imagem/imagem-triduo-jd-bertioga.jpg" 


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
            else:
                caixa_de_pesquisa.clear() # linha incluida 
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
                    #mensagem = f"{linha[1]} Essas são as notícias de hoje...Novo teste - Um abençoado dia :)"

                    ### string multiplas linhas --- utilizar aspas tripas e para quebra de linha \n
                    #  mensagem = f"""{linha[1]} Essas são as notícias de hoje...Novo teste - Um abençoado dia \n
                    #                           continuando a mensagem na outra linha\n
                    #                           continuando... \n
                    #                           continuando... \n:)"""

                    ### string multiplas linhas --- utilizar aspas tripas e para quebra de linha \n
                    mensagem = f"""Prezado(a) {linha[1]}, Paz e bem!\n
                                Mantenha-se conectado conosco! Salve o contato do Dízimo Paroquial (11) 4595-7272 para continuar recebendo nossas mensagens e comunicados importantes da Paróquia Nossa Senhora de Lourdes.\n\n
                                Convidamos você e sua família para o Tríduo em honra à nossa padroeira, a Comunidade Rainha dos Apóstolos, Jardim Bertioga. De 19 a 22 de agosto de 2023. Veja a programação:
                                Dia 19 - Sábado - Tema: Maria, Rainha dos Apóstolos, modelo de vocação. Terço às 17h30 e Missa Assunção de Nossa Senhora (Vigília) às 18h00
                                Dia 20 - Domingo - Tema: Maria, Rainha dos Apóstolos, vocação é graça de Deus. Terço às 7h30 e Missa Assunção de Nossa Senhora (Dia) às 8h00
                                Dia 21 - Segunda-feira - Tema: Maria, Rainha dos Apóstolos, vocação é missão.  Terço às 19h00 e Santa Missa às 19h30
                                Dia 22 - Terça-feira - Festa da Padroeira
                                Concentração para Procissão na Comunidade Nossa Senhora de Guadalupe (Jd. Aimoré) às 18h00
                                Missa e Coroação da Rainha dos Apóstolos às 18h30. Será um momento especial de reflexão e celebração. Contamos com a sua particição!\n
                                Para continuar recebendo nossas mensagens, responda "SIM". Caso contrário, se não desejar mais receber, responda com um "NÃO". 
                                Agradecemos por fazer parte da nossa comunidade. Desejamos muitas bênçãos, Equipe do Dízimo da Paróquia Nossa Senhora de Lourdes\n"""

                    #se desejar o envio da midia antes da mensagem de texto
                    enviar_midia(midia)
                    time.sleep(1)

                    caixa_de_msg.send_keys(mensagem)
                    time.sleep(1)

    #se desejar o envio da midia após a msg de texto                
    #                enviar_midia(midia)
    #                time.sleep(1)
                    
                    caixa_de_msg.send_keys(Keys.ENTER)
                    time.sleep(1)
                

                    # LIMPAR A CAIXA DE PESQUISA
                    caixa_de_pesquisa.click()
                    ActionChains(driver).send_keys(Keys.ESCAPE).perform()
            
                except NoSuchElementException:
                    print (f"entrou aquii no except")
                    print(f"Nome contato: {linha[1]}")
                    driver.find_element(By.XPATH, "//*[@id='pane-side']/div").click() #novo elemento 
                    time.sleep(1)

                    # LIMPAR A CAIXA DE PESQUISA
                    caixa_de_pesquisa.click()
                    ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                    time.sleep(1)
                    continue
            # Recomeçar
            time.sleep(5)
else:
  print(f"Erro ao tentar abrir o arquivo csv")

# Encerra o webdriver
driver.quit()