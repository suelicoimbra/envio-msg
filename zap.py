from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time
import csv

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
time.sleep(60)


#carregar a lista de numeros

telefones = []

if os.path.exists('telefones.csv'):
    with open('telefones.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            telefone = row['telefones']
            telefones.append(telefone)



#ENCOTRAR A CAIXA PESQUISA DE CONTATO
caixa_de_pesquisa = driver.find_element(By.CSS_SELECTOR, "div[title='Caixa de texto de pesquisa']")


#PERCORRER A LISTA DE TELEFONES
#ENVIAR A MENSAGEM

for telefone in telefones:
    caixa_de_pesquisa.send_keys(telefone)
    caixa_de_pesquisa.send_keys(Keys.ENTER)
    time.sleep(2)
    caixa_de_msg = driver.find_element(By.CSS_SELECTOR, "div[title='Mensagem']")
    time.sleep(1)
    caixa_de_msg.send_keys('Essas são  as noticias de hoje....')
    time.sleep(1)
    caixa_de_msg.send_keys(Keys.ENTER)


    #LIMPAR A CAIXA DE PESQUISA

    caixa_de_pesquisa.click()
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    
    #recomeçar
    time.sleep(5)
