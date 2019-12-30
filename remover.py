# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 17:42:48 2019

@author: Admin
"""

import re
import os

class Remover():
    
    def __init__(self,mypath, pattern):
        self.mypath = mypath
        self.pattern = pattern
    
    def remove_files(self):
        remover = []
        for i, filename in enumerate(os.listdir(self.mypath)):
            if bool(re.search(self.pattern, os.listdir(self.mypath)[i])):
                #os.remove(mypath + "\\"+ filename)
                print(self.mypath + "\\"+ filename)
                remover.append(self.mypath + "\\"+ filename)
            else:
                #continue
                pass
        
        len(remover)
        for i in range(len(remover)):
            os.remove(remover[i])
            
if __name__ == "__main__":
    mypath = input("Silinecek Dosyaların Yolunu Giriniz: ") #Path
    pattern = input("İçerisindeki Karakter veya Kelimeyi Giriniz: ") # Word or Character
    remover = Remover(mypath, pattern)
    remover.remove_files()
    
         

