import requests
from bs4 import BeautifulSoup

def bible(version, book, chapter, verse=0):
  if not verse:
    page = requests.get(f"https://www.bibliaonline.com.br/{version}/{book}/{chapter}")
  else:
    page = requests.get(f"https://www.bibliaonline.com.br/{version}/{book}/{chapter}/{verse}")
  soup = BeautifulSoup(page.content, 'html.parser')
  verses = soup.find_all('span', class_='t')

  result = []
  for verse in verses:
    result.append(verse.text)
  
  return result

def chapter_amount(version, book):
  page = requests.get(f"https://www.bibliaonline.com.br/{version}/{book}")
  soup = BeautifulSoup(page.content, 'html.parser')
  verses = soup.find_all('li')
  links = []
  for verse in verses:
    links.append(verse.find("a" , recursive=False))
  amount = -1
  for link in links:
    if link["href"].startswith(f"https://www.bibliaonline.com.br/{version}/{book}"):
      amount+=1
  return amount