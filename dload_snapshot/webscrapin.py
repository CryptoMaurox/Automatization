from shlex import shlex
import requests #Hacer peticiones a las páginas
from bs4 import BeautifulSoup as b #Poder manipular y extraer la información
import unidecode
import shlex, subprocess

url = 'https://polkachu.com/tendermint_snapshots/teritori/'
dload_url='https://snapshots.polkachu.com/snapshots/teritori/'

html=requests.get(url) # get info HTML web page
content=html.content # save the content 
soup = b(content, "lxml") # convert to lxml

title = soup.find("a",{"class":"link-brand"}) # Serch only download link

snap_name = unidecode.unidecode(title.string) # Get only snapshot name

dload_comm = 'wget -O '+' '+'$HOME/Downloads/'+snap_name+ ' '+ dload_url + snap_name + " --inet4-only"
print(dload_comm) #show the download snapshot command to execute
subprocess.call(dload_comm, shell=True) #execute commnand ##Not recomended use shell=true change this in other versions

unzip_comm = 'lz4 -c -d $HOME/Downloads/'+ snap_name+ ' | tar -x -C $HOME/Downloads'
print(unzip_comm) #Show the unzip command to excute
subprocess.call(unzip_comm, shell=True) #Execute command ##Not recomended use shell=true change this in other versions 
