# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 18:46:44 2022

@author: Pinta
@version: v0.1 

"""  

import os
import json

def json_creator(jspath):
    collection_name = input("Insert the colletction name: ")
    descrizione = input("Insert a little description: ")
    ipfs = input("Copy the ipfs string without /: ")
    Jspath = "./"+str(jspath)
    check = input("Insert YES if you want to specify a custom number range (else press ENTER)")
    if not check:    
        for i in range(0,len(os.listdir(Jspath))):
            assigner(descrizione, ipfs, collection_name, i, Jspath)
    else:
        index1 = input("Insert start range number: ")
        index2 = input("Insert end range number: ")
        for i in range(index1, index2):
            assigner(descrizione, ipfs, collection_name, i, Jspath)

def renamer(path):
    Path = "./"+str(path)
    
    filelist = os.listdir(Path)
    for index, file in enumerate(filelist):
        os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index), '.png'])))
        
        
def assigner(descr,ipfs, collection_name,index,jspath):
    #You can add metadata to the sample of the dictionary, but you don't have to change the sample
    #Cambiare il formato, mettere in automatico
    dictionary = {
        "name": str(collection_name),
        "description": str(descr),
        "image": "ipfs://"+str(ipfs)+"/"+str(index)+".png"
    }

    json_object = json.dumps(dictionary, indent = 4)
    with open("./"+str(jspath)+"/"+str(index)+".json", "w") as outfile:
        outfile.write(json_object)
    
            

    