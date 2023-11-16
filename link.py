#!/usr/bin/env python3
import os
input=input("Insersci il percorso per creare l'indice della directory obsidian")
os.chdir(input)
files= os.listdir(input)

nome_file= input.split("/")[-1]+".md"

with open(nome_file , "w") as f:
    for file in files:
        # Se il percorso non è una directory si crea un link da usare dentro Obsidian fino al file
        if os.path.isdir(file) == False:
            path="/".join(f'{input}/{file}'.split("/")[6:])
            f.write(f'{str(files.index(file)+1)})[[{path}]]\n')
        # Se il percorso è una directory si crea un altro file dentro alla directory, e poi si crea il link da usare dentro Obsidian
        else:
            path="/".join(f'{input}/{file}'.split("/")[6:])
            f.write(f'{str(files.index(file)+1)})[[{path}/{path.split("/")[-1]}]]\n')
