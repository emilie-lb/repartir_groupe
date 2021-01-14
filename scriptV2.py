#!/usr/bin/env python3
import random
import json
import logging

'''Définitions'''
# Ouvrir fichier contenant noms et faire une liste les contenant
def open_file():
    with open(myfile,'r', encoding="utf-8") as i:
        liste_noms = i.readlines()
    return liste_noms

# Déf pour déterminer le nombre de groupe
def n_groupes(liste_noms, nombre_max):
    if len(liste_noms)%nombre_max == 0:
        nombre_groupes = len(liste_noms)//nombre_max
    else:
        nombre_groupes = len(liste_noms)//nombre_max +1
    return nombre_groupes

# Déf pour créer le dico vide
def dico_groupes_vide(nombre_groupes):
    dico_groupes ={}
    x=1
    while x<=nombre_groupes:
        dico_groupes["groupe"+str(x)]=[]
        x+=1
    return dico_groupes

# Déf pour attribuer les personnes à chaque groupe
def remplir_dico_groupes(nombre_max, liste_noms):
    dico_groupes = dico_groupes_vide(nombre_groupes)
    i = 1
    while i<= nombre_max: # répète nombre_max de fois
        index = 1
        for groupe in dico_groupes: #pour chaque groupe du dico groupe
            if len(liste_noms)> 0: # s'il y a des noms dans la liste de noms
                index_pioche = random.randrange(len(liste_noms)) # on pioche un nombre au hasard entre 0 et le nombre de noms dans le tableau
                nom_pioche = liste_noms[index_pioche] # on retrouve le noms correspondant au nombre pioché qui sert d'index
                dico_groupes["groupe"+str(index)].append(nom_pioche.strip()) # on introduit le nom dans le groupe
                liste_noms.remove(nom_pioche) # on supprime le nom pioché du tableau
                index +=1 # + 1 à la variable index qui permet de trouver le groupe 
        i+=1
    return dico_groupes

# enrigistrer le dico dans un fichier json
def fichier_json(dico_groupes):
    with open("data_file.json", "w", encoding="utf-8") as write_file:
        json.dump(dico_groupes, write_file)
        return(write_file)


# programme pour déterminer les membres des groupes
myfile= input("Veuillez saisir le nom de la fichier: ")
nombre_max= int(input("Saisir nombre max: "))
liste_noms = open_file()
nombre_personnes = len(liste_noms)
print("Nombre de personnes dans le fichier: ",nombre_personnes)
nombre_groupes = n_groupes(liste_noms, nombre_max)   
print("Nombre de groupes: ", nombre_groupes)
dico_groupes = remplir_dico_groupes(nombre_max, liste_noms)
print("voici le dico des groupes rempli: ", dico_groupes)
dico_json = fichier_json(dico_groupes)

#with open("test_log.txt", "w") as log_file:
    # for line in log_file.readlines():
    #     tmp = line.split("--")
    #     print("time: %s, user: %s, level: %s, message: %s" % (tmp[0], tmp[1], tmp[2], tmp[3]))

logging.debug("Voici la date et l'heure de l'execution du programme !")
logging.basicConfig(filename='log_groupe.txt',level=logging.DEBUG ,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
#logging.basicConfig(filename='test_log.txt',level=logging.DEBUG,\
#      format='%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s') 
logging.info("")
logging.warning("")