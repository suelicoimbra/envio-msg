from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time
import csv

# Inicialização do webdriver do Selenium
driver = webdriver.Chrome()  # Certifique-se de ter o ChromeDriver instalado e no PATH

# Verifica se o arquivo 'telefones.csv' existe
if os.path.exists('telefones.csv'):
    with open('telefones.csv', mode='r') as csvfile:
        # Passando o arquivo CSV para o leitor CSV padrão do Python
        leitor_csv = csv.reader(csvfile)
        
        # Iterando cada linha do arquivo CSV
        for indice, linha in enumerate(leitor_csv):
            if indice == 0:
                print(f"A primeira linha tem os cabeçalhos, e o primeiro campo é: {linha[0]}")
                print(f"A primeira linha tem os cabeçalhos, e o segundo campo é: {linha[1]}")
            else:
                print(linha)

# Encerra o webdriver
driver.quit()
