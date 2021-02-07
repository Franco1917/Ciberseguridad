#!/usr/bin/env python
import sys
import os
import platform

plataforma = platform.system()

if len(sys.argv) == 4:
    if plataforma == 'Linux':
        os.system(f"sed -i '1s/^/TOPSECRET\n/' {sys.argv[2]}")
        os.system(f"cat {sys.argv[1]} {sys.argv[2]} > {sys.argv[3]}")
    # elif plataforma == 'Windows':
    #     os.system(f"copy /b {sys.argv[1]} + {sys.argv[2]} {sys.argv[3]}")

elif len(sys.argv) == 2:
    os.system(f"cat {sys.argv[1]} | grep -aA99999 TOPSECRET | sed -n '2,$ p' > secretnew")
else:
    print(f"Para ocultar un archivo de texto en una imagen ejecute: {sys.argv[0]} [path_a_imagen] [path_del_archivo_de_texto] [path_archivo_de_salida] \nPara obtener el archivo de texto oculto en la imagen ejecute: {sys.argv[0]} [path_a_imagen_con_texto_oculto] [nombre del archivo ]")
    
