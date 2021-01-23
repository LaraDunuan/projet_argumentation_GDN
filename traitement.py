# -*- coding: utf-8 -*-
#  Lara DUNUAN et Siyu WANG
#  Projet Argumentation Grand Débat National, Mai 2019 
#  Fichier d'entrée : projet_GDN_marqueur.txt
#  Fichier de sortie : pretraitement.txt

def main():
    # Read files
    print("Execution de traitement.py")
    print("reading files...")
    text = Get_file("./projet_GDN_marqueur.txt")
    text = text.rstrip()
    text1 = text.split(".")
    
    write_file(text1, "pretraitement.txt")

def Get_file(file):
    with open(file, 'r') as content_file:
        content = content_file.read()
    return content

def write_file(data, filename):
    file = open(filename,"w")
    for i in data:
        file.write(i)
        file.write("\n")
    file.close()

if __name__ == "__main__":
	main()