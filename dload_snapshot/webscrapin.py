from multiprocessing.connection import deliver_challenge
import requests #Hacer peticiones a las páginas
from bs4 import BeautifulSoup as b #Poder manipular y extraer la información
import unidecode
import subprocess
from snapshots import *
from dirchains import *


array_url=[url_tori, url_meme]
array_dload=[dload_tori, dload_meme]
array_chaindir=[chaindir_tori, chaindir_meme]
cantidad = len(array_dload)
print(cantidad)
chain = 2

while chain <= cantidad:
    
    html=requests.get(array_url[chain]) # get info HTML web page
    content=html.content # save the content 
    soup = b(content, "lxml") # convert to lxml

    title = soup.find("a",{"class":"link-brand"}) # Serch only download link

    snap_name = unidecode.unidecode(title.string) # Get only snapshot name

    dload_comm = 'wget -O '+' '+'$HOME/Downloads/'+snap_name+ ' '+ array_dload[chain] + snap_name + " --inet4-only"
    print(dload_comm) #show the download snapshot command to execute
    subprocess.call(dload_comm, shell=True) #execute commnand ##Not recomended use shell=true change this in other versions


    unzip_comm = 'lz4 -c -d $HOME/Downloads/'+ snap_name+ ' | tar -x -C ' + array_chaindir[chain]
    print(unzip_comm) #Show the unzip command to excute
    subprocess.call(unzip_comm, shell=True) #Execute command ##Not recomended use shell=true change this in other versions
    chain += 1 

    if cantidad == chain: 
        print("\n successful!!")
        break
