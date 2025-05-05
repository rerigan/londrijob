# import pyautogui as pa
import time 
# import pyperclip
import keyboard
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import json
import re

pagina = requests.get('https://divulgavagas.com.br/vagas-de-emprego?estado=PR&cidade=Londrina')
dados_pagina = BeautifulSoup(pagina.text, 'html.parser')
vagas =[]

job_titles = dados_pagina.find_all('div', class_='vaga-titulo-text')
for div in job_titles:
    titulo = div.find('a').text.strip()
    titulo = re.sub(r'\s*\(\d+\)$', '', titulo)
    link = div.find('a')['href'].strip()
    vagas.append({
    "titulo": titulo,
    "link": link
    })
        
time.sleep(2)
pagina2 = requests.get('https://divulgavagas.com.br/vagas-de-emprego?pag=2&estado=PR&cidade=Londrina')
dados_pagina2 = BeautifulSoup(pagina2.text, 'html.parser')

job_titles2 = dados_pagina2.find_all('div', class_='vaga-titulo-text')
for div in job_titles2:
    titulo = div.find('a').text.strip()
    titulo = re.sub(r'\s*\(\d+\)$', '', titulo)
    link = div.find('a')['href'].strip()
    vagas.append({
        "titulo": titulo,
        "link": link
    })
         
with open("vagas.json", "a", encoding="utf-8") as f:
    json.dump(vagas, f, ensure_ascii=False, indent=4)

print("Arquivo vagas.json salvo com sucesso!")

# keyboard.add_hotkey('ctrl+h', my_function)
# print("Press Ctrl+H to execute the script.")
# keyboard.wait('esc')