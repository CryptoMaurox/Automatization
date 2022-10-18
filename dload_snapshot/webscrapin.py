from shlex import shlex
import requests
from bs4 import BeautifulSoup as b
import unidecode
import shlex, subprocess

url = 'https://polkachu.com/tendermint_snapshots/teritori/'
dload_url='https://snapshots.polkachu.com/snapshots/teritori/'

html=requests.get(url)
content=html.content
soup = b(content, "lxml")

title = soup.find("a",{"class":"link-brand"}) #busca solo el apartado de link de descarga

link = unidecode.unidecode(title.string)

print(link)
dload_comm = ('wget -O '+''+link+' '+ dload_url + link + " --inet4-only")
dload_comm_split=shlex.split(dload_comm)

print(dload_comm_split)
subprocess.call(dload_comm_split)
unzip_comm = 'lz4 -c -d /home/mauro/aprendizaje/python/teritori_226903.tar.lz4 | tar -x -C /home/mauro/pruebas/automatization'
#unzip_comm_split=shlex.split(unzip_comm)

print(unzip_comm)
subprocess.call(unzip_comm, shell=True)
