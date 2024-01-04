#!/usr/bin/env python3
import os
input=input("add the path to create the index of the directory obsidian")
os.chdir(input)
files= os.listdir(input)

nome_file= input.split("/")[-1]+".md"

with open(nome_file , "w") as f:
    for file in files:
        # If the path isn't a directory a link is created to use it inside Obsidian that lead to the file
        if os.path.isdir(file) == False:
            path="/".join(f'{input}/{file}'.split("/")[6:])
            f.write(f'{str(files.index(file)+1)})[[{path}]]\n')
        # If the path is a directory a new file that list all the other files inside the directory and create links that lead to the files  is created inside the directory 
        else:
            path="/".join(f'{input}/{file}'.split("/")[6:])
            f.write(f'{str(files.index(file)+1)})[[{path}/{path.split("/")[-1]}]]\n')
