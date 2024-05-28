#!/usr/bin/env python3

"""
Dicio-Py: Script para buscar o significado de palavras no dicionário online Dicio.
Versão: 1.0
Autor: Jeiel Lima Miranda.
Data: 26 de maio de 2024
Fork: https://github.com/ludovici-philippus/dicio-py

Descrição:
Este script recebe uma palavra como argumento de linha de comando e busca seu significado no site dicio.com.br.
O significado é formatado e exibido no terminal com cores para facilitar a leitura.

Uso:
python3 ./dicio-py.py [PALAVRA]

Dependências:
- Nenhuma dependência externa necessária. O script utiliza apenas bibliotecas padrão do Python 3.
"""

from dicio import main
import sys
import re
import os
from unicodedata import normalize
from urllib.request import urlopen

BASE_URL = 'https://www.dicio.com.br/'
COLORS = {
    'RED': "\033[1;31m",
    'WHITE': "\033[1m",
    'YELLOW': "\033[1;33m",
    'BLUE': "\033[1;34m",
    'MAGENTA': "\033[1;35m",
    'END': "\033[m",
    'ITALIC': '\033[3m'
}

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def colorize(text, color):
    return f"{COLORS[color.upper()]}{text}{COLORS['END']}"

def print_with_color(text: str, color: str):
    print(colorize(text, color))

def get_content_of_tag(html, tag, close_tag):
    tag_index = html.find(tag)
    start_index = tag_index + len(tag)
    end_index = html[start_index:].find(close_tag) + start_index
    return html[start_index:end_index]

def format_html(html):
    etymologies = html.split('<span class="cl">')
    etymologies.pop(0)
    formatted_text = ""
    for etymology in etymologies:
        meanings = etymology.split('</span>')
        formatted_text += f"\n- {colorize(meanings[0], 'MAGENTA')}\n\n"
        meanings.pop(0)
        for meaning in meanings:
            meaning = meaning.strip()
            if meaning.startswith('<span class="etim">'):
                formatted_meaning = meaning.replace('<span class="etim">', COLORS['WHITE'])
                formatted_meaning = formatted_meaning.replace('<i>', COLORS['ITALIC'])
                formatted_meaning = formatted_meaning.replace('</i>', COLORS['END'])
                formatted_meaning = formatted_meaning.replace('<br />', '')
                formatted_meaning = formatted_meaning.replace('<span>', '- ')
                formatted_text += f"{formatted_meaning}{COLORS['END']}"                    
            elif meaning.startswith('<span><span class="tag">'):
                formatted_meaning = meaning.replace('<span class="tag">', COLORS['YELLOW'])
                formatted_meaning = formatted_meaning.replace('<span>', '- ')
                formatted_text += f" {formatted_meaning}{COLORS['END']}"
            else:
                formatted_meaning = meaning.replace('<span>', '- ')
                TAG_PATTERN = re.compile(r'<.*?>')
                formatted_meaning = TAG_PATTERN.sub('', formatted_meaning)
                formatted_text += f" {formatted_meaning}{COLORS['END']}\n"
    return formatted_text

def print_results(word, html_meaning):
    print_with_color(f"Significado de {COLORS['BLUE']}{word.upper()}{COLORS['END']}", 'WHITE')
    print(format_html(html_meaning))

def main():
    if len(sys.argv) < 2:
        print_with_color("ERRO! Você precisa prover uma palavra", 'RED')
        print("Uso: python3 ./dicio-py.py [PALAVRA]")
        exit()

    clear_terminal()  # Limpa o terminal antes de cada execução

    word = sys.argv[1].lower()
    try:
        normalized_word = normalize('NFKD', word).encode('ASCII', 'ignore').decode('ASCII')
        page_word = urlopen(f"{BASE_URL}{normalized_word}")
    except:
        print_with_color("A palavra que você pesquisou não foi encontrada", 'RED')
        exit()

    html = page_word.read().decode('utf-8')
    html_meaning = get_content_of_tag(html, '<p class="significado textonovo">', '</p>')

    print_results(word, html_meaning)

if __name__ == "__main__":
    main()
