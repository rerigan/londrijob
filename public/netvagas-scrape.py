import requests
from bs4 import BeautifulSoup
import json
import re

pagina = requests.get('https://www.netvagas.com.br/empresa/anuncios/cidade/londrina-pr/cargo/-/')
dados_pagina = BeautifulSoup(pagina.text, 'html.parser')

job_titles = dados_pagina.find_all('div', class_='advs_title')
vagas = []

for div in job_titles:
    titulo = div.find('a').text.strip()
    titulo = re.sub(r'\s*\(\d+\)$', '', titulo)
    link = div.find('a')['href'].strip()
    vagas.append({
        "titulo": titulo,
        "link": link
    })

# Salvar como JSON
with open("vagas.json", "w", encoding="utf-8") as f:
    json.dump(vagas, f, ensure_ascii=False, indent=4)

print("Arquivo vagas.json salvo com sucesso!")
