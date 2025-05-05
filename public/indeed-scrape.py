# import pyautogui as pa
import time 
# import pyperclip
import keyboard
from selenium import webdriver
import requests
from bs4 import BeautifulSoup

pagina = requests.get('https://br.indeed.com/l-londrina,-pr-vagas.html?vjk=7f7bfb525256d679')
time.sleep(8)
dados_pagina = BeautifulSoup(pagina.text, 'html.parser')

job_titles = dados_pagina.find_all('div', class_='jcs-JobTitle')

with open("saida.txt", "a", encoding="utf-8") as arquivo:
    for div in job_titles:
        texto = div.find('a').text
        link=div.find('a')['href']
        print(texto, file=arquivo)
        print(link, file=arquivo)

    

# keyboard.add_hotkey('ctrl+h', my_function)
# print("Press Ctrl+H to execute the script.")
# keyboard.wait('esc')