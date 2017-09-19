# -*- coding: utf-8 -*-
import textract
import string
import re
import os
import sys
import fnmatch
from os.path import join

#Memorizzo la descrizione iniziale del test
def CopiaReport(Originale, Copia):
  f1 = Originale
  f2 = Copia
  count = 0
  while 1:
    Testo = f1.readline()
    if ((Testo == "\n") & (count == 0)):
      count += 1
      continue
    if ((Testo == "\n") & (count == 1)):
      break
    f2.write(Testo)
  f1.close()
  f2.close()
  return

#Determina quante misurazioni sono state effettuate
def NumeroMisurazioni(Originale, Copia):
  f1 = Originale
  f2 = Copia
  contatore = 0
  count = 0

  while 1:
    Testo = f1.readline()
    if (re.match("[^1]", Testo)) and (count == 0):
      continue

    if (re.match("[1]", Testo)) and (count == 0):
      count += 1
      contatore += 1

    if (re.match("[^1]", Testo)) and (count == 1):
      if Testo == "\n":
        break
      else:
        contatore += 1
        
  abc = str(contatore)
  
  f2.write(abc)
  f1.close()
  f2.close()

#Salvo in un file txt i dati delle tabelle, escluso il Report iniziale
def CopiaFile(Originale, Copia):
  f1 = Originale
  f2 = Copia
  listaNomi = []
  count = 0
  a = 0
  while 1:
    Testo = f1.readline()
    if (re.match("[^#]", Testo)) and (count == 0):
      continue

    if Testo == "\n":
      continue
    
    if (re.match("[#]", Testo)) and (count == 0):
      listaNomi.insert(a,Testo[:-1]+";")
      f2.write(listaNomi[a])
      a += 1
      count += 1
      
    if (re.match("[^#]", Testo)) and (count == 1):
      listaNomi.insert(a,Testo[:-1]+";")
      f2.write(listaNomi[a])
      a += 1
      
    if Testo == "":
      break
    
  f1.close()
  f2.close()
  return

#Inserisco i primi nomi delle colonne
def OrdinaColonne(Originale, Copia):
  f1 = Originale
  f2 = Copia
  listaColonne = []
  a=0
  indice = 0
  s = ""
  count = 0
  while 1:
    Testo = f1.readline()
    while count < 3:
      if Testo[indice] != ";":
        s = s + Testo[indice]
        indice += 1
      if Testo[indice] == ";":
        if count != 3:
          s = s + Testo[indice]
          indice += 1
          count += 1
        if count == 3:
          listaColonne.insert(a, s)
          f2.write(listaColonne[a])
          break
          indice += 1
          count += 1
    if Testo == "":
      break
  f1.close()
  f2.close()
  return

#Sistemo i dati all'interno della lista
def OrdinaRighe(Originale, Copia):
  f1 = Originale
  f2 = Copia
  listaRighe1 = []
  listaRighe2 = []
  listaRighe3 = []
  listaRighe4 = []
  listaRighe5 = []
  listaRighe6 = []
  a = 0
  indice = 0
  s = ""
  count = 0
  ok = 0
  while 1:
      Testo = f1.readline()
      while count < 6:
          if Testo[indice] != "1":
            if ok == 0:
              indice += 1
          if Testo[indice] == "1":
            s = s + Testo[indice]
            indice += 1
            ok = 1
          if Testo[indice] != "1" and ok == 1:
            s = s + Testo[indice]
            listaRighe1.insert(a, s)
            f2.write(listaRighe1[a])
            f2.write("\n")
            s = ""
            indice += 1
            count += 1
            ok = 2
          if Testo[indice] != "1" and ok == 2:
            if Testo[indice] != ";":
               s = s + Testo[indice]
               indice += 1
            if Testo[indice] == ";":
               s = s + Testo[indice]
               listaRighe2.insert(a, s)
               f2.write(listaRighe2[a])
               f2.write("\n")
               s = ""
               indice += 1
               count += 1
               ok = 3
          if Testo[indice] != "1" and ok == 3:
            if Testo[indice] != ";":
               s = s + Testo[indice]
               indice += 1
            if Testo[indice] == ";":
               s = s + Testo[indice]
               listaRighe3.insert(a, s)
               f2.write(listaRighe3[a])
               f2.write("\n")
               s = ""
               indice += 1
               count += 1
               ok = 4
          if Testo[indice] != "1" and ok == 4:
            if Testo[indice] != ";":
               s = s + Testo[indice]
               indice += 1
            if Testo[indice] == ";":
               s = s + Testo[indice]
               listaRighe4.insert(a, s)
               f2.write(listaRighe4[a])
               f2.write("\n")
               s = ""
               indice += 1
               count += 1
               ok = 5
          if Testo[indice] != "1" and ok == 5:
            if Testo[indice] != ";":
               s = s + Testo[indice]
               indice += 1
            if Testo[indice] == ";":
               s = s + Testo[indice]
               listaRighe5.insert(a, s)
               f2.write(listaRighe5[a])
               f2.write("\n")
               s = ""
               indice += 1
               count += 1
               ok = 6
          if Testo[indice] != "1" and ok == 6:
            if Testo[indice] != ";":
               s = s + Testo[indice]
               indice += 1
            if Testo[indice] == ";":
               s = s + Testo[indice]
               listaRighe6.insert(a, s)
               f2.write(listaRighe6[a])
               f2.write("\n")
               count += 1
      if Testo == "":
        break
            
  f1.close()
  f2.close()
  return

#Sistemo i dati all'interno della lista
def OrdinaRighe1(Originale, Copia):
  f1 = Originale
  f2 = Copia
  listaRighe = []
  a=0
  indice = 0
  s = ""
  count = 0
  ok = 0
  while 1:
    Testo = f1.readline()
    while count < 3:
      if Testo[indice] != "1":
        if ok == 0:
          indice += 1
      if Testo[indice] == "1":
        ok = 1
        s = s + Testo[indice]
        indice += 1
      if Testo[indice] != "1" and ok == 1:
        if Testo[indice] == ";":
          if count != 3:
            s = s + Testo[indice]
            indice += 1
            count += 1
          if count == 3:
            listaRighe.insert(a, s)
            f2.write(listaRighe[a])
        if Testo[indice] != ";":
          s = s + Testo[indice]
          indice += 1
    if Testo == "":
      break
  f1.close()
  f2.close()
  return

#Sistemo i dati all'interno della lista
def OrdinaRigheNome(Originale, Copia):
  f1 = Originale
  f2 = Copia
  listaRighe1 = []
  listaRighe2 = []
  listaRighe3 = []
  listaRighe4 = []
  listaRighe5 = []
  listaRighe6 = []
  a = 0
  indice = 0
  s = ""
  count = 0
  ok = 1
  contatore = 0
  while 1:
      Testo = f1.readline()
      while contatore < 9:
          if Testo[indice] != ";":
            indice += 1
          if Testo[indice] == ";":
            contatore += 1
            indice += 1
      while count < 6:      
          if Testo[indice] != "1" and ok == 1:
            if Testo[indice] != ";":
                s = s + Testo[indice]
                indice += 1
            if Testo[indice] == ";":
                s = s + Testo[indice]
                listaRighe1.insert(a, s)
                f2.write(listaRighe1[a])
                f2.write("\n")
                s = ""
                indice += 1
                count += 1
                ok = 2
          if Testo[indice] != "1" and ok == 2:
            if Testo[indice] != ";":
               s = s + Testo[indice]
               indice += 1
            if Testo[indice] == ";":
               s = s + Testo[indice]
               listaRighe2.insert(a, s)
               f2.write(listaRighe2[a])
               f2.write("\n")
               s = ""
               indice += 1
               count += 1
               ok = 3
          if Testo[indice] != "1" and ok == 3:
            if Testo[indice] != ";":
               s = s + Testo[indice]
               indice += 1
            if Testo[indice] == ";":
               s = s + Testo[indice]
               listaRighe3.insert(a, s)
               f2.write(listaRighe3[a])
               f2.write("\n")
               s = ""
               indice += 1
               count += 1
               ok = 4
          if Testo[indice] != "1" and ok == 4:
            if Testo[indice] != ";":
               s = s + Testo[indice]
               indice += 1
            if Testo[indice] == ";":
               s = s + Testo[indice]
               listaRighe4.insert(a, s)
               f2.write(listaRighe4[a])
               f2.write("\n")
               s = ""
               indice += 1
               count += 1
               ok = 5
          if Testo[indice] != "1" and ok == 5:
            if Testo[indice] != ";":
               s = s + Testo[indice]
               indice += 1
            if Testo[indice] == ";":
               s = s + Testo[indice]
               listaRighe5.insert(a, s)
               f2.write(listaRighe5[a])
               f2.write("\n")
               s = ""
               indice += 1
               count += 1
               ok = 6
          if Testo[indice] != "1" and ok == 6:
            if Testo[indice] != ";":
               s = s + Testo[indice]
               indice += 1
            if Testo[indice] == ";":
               s = s + Testo[indice]
               listaRighe6.insert(a, s)
               f2.write(listaRighe6[a])
               f2.write("\n")
               count += 1
      if Testo == "":
        break
            
  f1.close()
  f2.close()
  return

#Sistemo i dati all'interno della lista
def OrdinaRigheData(Originale, Copia):
  f1 = Originale
  f2 = Copia
  listaRighe1 = []
  listaRighe2 = []
  listaRighe3 = []
  listaRighe4 = []
  listaRighe5 = []
  listaRighe6 = []
  a = 0
  indice = 0
  s = ""
  count = 0
  ok = 0
  punti = 0
  while 1:
      Testo = f1.readline()
      while count < 15:
          if Testo[indice] == ";":
              count += 1
              indice += 1
          else:
              indice += 1
      while punti < 6:
          if Testo[indice] != ";" and ok == 0:
              s = s + Testo[indice]
              indice += 1
          if Testo[indice] == ";":
              s = s + Testo[indice]
              listaRighe1.insert(a, s)
              f2.write(listaRighe1[a])
              f2.write("\n")
              s = ""
              indice += 1
              punti += 1
              ok = 1
          if Testo[indice] != ";" and ok == 1:
              s = s + Testo[indice]
              indice += 1
          if Testo[indice] == ";" and ok == 1:
              s = s + Testo[indice]
              listaRighe2.insert(a, s)
              f2.write(listaRighe2[a])
              f2.write("\n")
              s = ""
              indice += 1
              punti += 1
              ok = 2
          if Testo[indice] != ";" and ok == 2:
              s = s + Testo[indice]
              indice += 1
          if Testo[indice] == ";" and ok == 2:
              s = s + Testo[indice]
              listaRighe3.insert(a, s)
              f2.write(listaRighe3[a])
              f2.write("\n")
              s = ""
              indice += 1
              punti += 1
              ok = 3
          if Testo[indice] != ";" and ok == 3:
              s = s + Testo[indice]
              indice += 1
          if Testo[indice] == ";" and ok == 3:
              s = s + Testo[indice]
              listaRighe4.insert(a, s)
              f2.write(listaRighe4[a])
              f2.write("\n")
              s = ""
              indice += 1
              punti += 1
              ok = 4
          if Testo[indice] != ";" and ok == 4:
              s = s + Testo[indice]
              indice += 1
          if Testo[indice] == ";" and ok == 4:
              s = s + Testo[indice]
              listaRighe5.insert(a, s)
              f2.write(listaRighe5[a])
              f2.write("\n")
              s = ""
              indice += 1
              punti += 1
              ok = 5
          if Testo[indice] != ";" and ok == 5:
              s = s + Testo[indice]
              indice += 1
          if Testo[indice] == ";" and ok == 5:
              s = s + Testo[indice]
              listaRighe6.insert(a, s)
              f2.write(listaRighe6[a])
              f2.write("\n")
              s = ""
              indice += 1
              punti += 1
              ok = 6
      if Testo == "":
        break

  f1.close()
  f2.close()
  return



#Aggiungo altre colonne alla tabella
def OrdinaColonneRL(Originale, Copia):
  f1 = Originale
  f2 = Copia
  listaColonne = []
  a=0
  indice = 0
  s = ""
  count = 0
  ok = 0
  virgole = 0
  num = 0
  punti = 0
  contatore = 0
  somma = 0
  conteggio = 0
  while 1:
    Testo = f1.readline()
    while count < 3:
      if Testo[indice] != "L":
        if ok == 0:
          indice += 1
      if Testo[indice] == "L":
        ok = 1
        indice += 1
      if Testo[indice] != "L" and ok == 1:
        if Testo[indice] == ";":
          count += 1
          indice += 1
        else:
          indice += 1
    while virgole != 2:
      if Testo[indice] == ";":
        if num == 1:
          s=s+Testo[indice]
          virgole += 1
        if num == 0:
          num = 1
          indice += 1
      if Testo[indice] != ";":
        s=s+Testo[indice]
        indice += 1
      if virgole == 2:
        listaColonne.insert(a, s[:-1])
        indice += 1
        s = s[:-1]
    while conteggio < 6:
      if Testo[indice] != ";":
        indice += 1
      if Testo[indice] == ";":
        conteggio += 1
        indice += 1
    while punti < 2:
      if Testo[indice] == ";":
        if contatore == 1:
          s=s+Testo[indice]
          punti += 1
        if contatore == 0:
           contatore = 1
           indice += 1
      if Testo[indice] != ";":
        s = s + Testo[indice]
        indice += 1
      if punti == 2:
        listaColonne.insert(a, s[:-1])
        f2.write(listaColonne[a])
        
    if Testo == "":
      break
  f1.close()
  f2.close()
  return

#Aggiungo altre colonne alla tabella
def OrdinaColonneDivisioni1(Originale, Copia):
  f1 = Originale
  f2 = Copia
  listaColonne = []
  a=0
  indice = 0
  s = ""
  count = 0
  ok = 0
  virgole = 0
  while 1:
    Testo = f1.readline()
    while count < 9:
      if Testo[indice] != "L":
        if ok == 0:
          indice += 1
      if Testo[indice] == "L":
        ok = 1
        indice += 1
      if Testo[indice] != "L" and ok == 1:
        if Testo[indice] == ";":
          count += 1
          indice += 1
        else:
          indice += 1
    while virgole != 4:
      if Testo[indice] == ";":
        s=s+Testo[indice]
        indice += 1
        virgole += 1
      if Testo[indice] != ";":
        s=s+Testo[indice]
        indice += 1
      if virgole == 4:
        listaColonne.insert(a, s[:-1])
        f2.write(listaColonne[a])
        
    if Testo == "":
      break
  f1.close()
  f2.close()
  return

#Aggiungo altre righe alla tabella
def OrdinaRigheRL(Originale, Copia):
  f1 = Originale
  f2 = Copia
  listaRighe1 = []
  listaRighe2 = []
  listaRighe3 = []
  listaRighe4 = []
  listaRighe5 = []
  listaRighe6 = []
  a = 0
  indice = 0
  s = ""
  count = 0
  ok = 0
  virgole = 0
  punti = 0
  contatore = 0
  somma = 0
  con = 0
  val = 0
  while 1:
    Testo = f1.readline()
    while count < 5:
      if Testo[indice] != "L":
        if ok == 0:
          indice += 1
      if Testo[indice] == "L":
        ok = 1
        indice += 1
      if Testo[indice] != "L" and ok == 1:
        if Testo[indice] == ";":
          count += 1
          indice += 1
        else:
          indice += 1
    while virgole < 6:
      if Testo[indice] != ";" and val == 0:
        s=s+Testo[indice]
        indice += 1
      if Testo[indice] == ";" and val == 0:
        s=s+Testo[indice]
        newString = s.replace(",",".")
        listaRighe1.insert(a, newString)
        indice += 1
        virgole += 1
        s = ""
        val = 1
      if Testo[indice] != ";" and val == 1:
        s=s+Testo[indice]
        indice += 1
      if Testo[indice] == ";" and val == 1:
        s=s+Testo[indice]
        newString = s.replace(",",".")
        listaRighe2.insert(a, newString)
        indice += 1
        virgole += 1
        s = ""
        val = 2
      if Testo[indice] == ";" and val == 2:
        s=s+Testo[indice]
        newString = s.replace(",",".")
        listaRighe3.insert(a, newString)
        indice += 1
        virgole += 1
        s = ""
        val = 3
      if Testo[indice] != ";" and val == 2:
        s=s+Testo[indice]
        indice += 1
      if Testo[indice] == ";" and val == 3:
        s=s+Testo[indice]
        newString = s.replace(",",".")
        listaRighe4.insert(a, newString)
        indice += 1
        virgole += 1
        s = ""
        val = 4
      if Testo[indice] != ";" and val == 3:
        s=s+Testo[indice]
        indice += 1
      if Testo[indice] == ";" and val == 4:
        s=s+Testo[indice]
        newString = s.replace(",",".")
        listaRighe5.insert(a, newString)
        indice += 1
        virgole += 1
        s = ""
        val = 5
      if Testo[indice] != ";" and val == 4:
        s=s+Testo[indice]
        indice += 1
      if Testo[indice] == ";" and val == 5:
        s=s+Testo[indice]
        newString = s.replace(",",".")
        listaRighe6.insert(a, newString)
        indice += 1
        virgole += 1
        s = ""
        val = 6
      if Testo[indice] != ";" and val == 5:
        s=s+Testo[indice]
        indice += 1
    while punti < 2:
      if Testo[indice] != ";":
        indice += 1
      if Testo[indice] == ";":
        indice += 1
        punti += 1
    while somma != 6:
      if con == 0:
        if Testo[indice] == ";":
          s=s+Testo[indice]
          newString = s.replace(",",".")
          listaRighe1.append(newString)
          indice += 1
          somma += 1
          s = ""
          con = 1
        if Testo[indice] != ";":
          s=s+Testo[indice]
          indice += 1
      if con == 1:
        if Testo[indice] == ";":
          s=s+Testo[indice]
          newString = s.replace(",",".")
          listaRighe2.append(newString)
          indice += 1
          somma += 1
          s = ""
          con = 2
        if Testo[indice] != ";":
          s=s+Testo[indice]
          indice += 1
      if con == 2:
        if Testo[indice] == ";":
          s=s+Testo[indice]
          newString = s.replace(",",".")
          listaRighe3.append(newString)
          indice += 1
          somma += 1
          s = ""
          con = 3
        if Testo[indice] != ";":
          s=s+Testo[indice]
          indice += 1
      if con == 3:
        if Testo[indice] == ";":
          s=s+Testo[indice]
          newString = s.replace(",",".")
          listaRighe4.append(newString)
          indice += 1
          somma += 1
          s = ""
          con = 4
        if Testo[indice] != ";":
          s=s+Testo[indice]
          indice += 1
      if con == 4:
        if Testo[indice] == ";":
          s=s+Testo[indice]
          newString = s.replace(",",".")
          listaRighe5.append(newString)
          indice += 1
          somma += 1
          s = ""
          con = 5
        if Testo[indice] != ";":
          s=s+Testo[indice]
          indice += 1
      if con == 5:
        if Testo[indice] == ";":
          s=s+Testo[indice]
          newString = s.replace(",",".")
          listaRighe6.append(newString)
          indice += 1
          somma += 1
          s = ""
          con = 6
        if Testo[indice] != ";":
          s=s+Testo[indice]
          indice += 1      
        
    if Testo == "":
      break
    for line in listaRighe1:
      f2.write(line)
    f2.write("\n")  
    for line in listaRighe2:
      f2.write(line)
    f2.write("\n")
    for line in listaRighe3:
      f2.write(line)
    f2.write("\n")
    for line in listaRighe4:
      f2.write(line)
    f2.write("\n")
    for line in listaRighe5:
      f2.write(line)
    f2.write("\n")
    for line in listaRighe6:
      f2.write(line)
    f2.write("\n")
  f1.close()
  f2.close()
  return

#Aggiungo altre righe alla tabella
def OrdinaRigheRL1(Originale, Copia):
  f1 = Originale
  f2 = Copia
  listaRighe = []
  a = 0
  indice = 0
  s = ""
  count = 0
  ok = 0
  virgole = 0
  punti = 0
  contatore = 0
  somma = 0
  con = 0
  while 1:
    Testo = f1.readline()
    while count < 5:
      if Testo[indice] != "L":
        if ok == 0:
          indice += 1
      if Testo[indice] == "L":
        ok = 1
        indice += 1
      if Testo[indice] != "L" and ok == 1:
        if Testo[indice] == ";":
          count += 1
          indice += 1
        else:
          indice += 1
    while virgole != 1:
      if Testo[indice] == ";":
        s=s+Testo[indice]
        virgole += 1
      if Testo[indice] != ";":
        s=s+Testo[indice]
        indice += 1
      if virgole == 1:
        listaRighe.insert(a, s)
        indice += 1
    while punti != 1:
      if Testo[indice] != ";":
        if contatore == 0 and con != 2:
          indice += 1
        if contatore == 1:
          s=s+Testo[indice]
          indice += 1
        if con == 2:
          s=s+Testo[indice]
          indice += 1
          somma = 1
      if Testo[indice] == ";":
        if contatore == 0 and somma != 1:
          con += 1
          indice += 1
        if somma == 1:
          s=s+Testo[indice]
          punti += 1
           
      if punti == 1:
        newString = s.replace(",",".")
        listaRighe.insert(a, newString)
        f2.write(listaRighe[a])
        
    if Testo == "":
      break
  f1.close()
  f2.close()
  return

#Aggiungo altre colonne alla tabella
def OrdinaColonneDivisioni(Originale, Copia):
  f1 = Originale
  f2 = Copia
  listaColonne = []
  a=0
  indice = 0
  s = ""
  count = 0
  ok = 0
  virgole = 0
  while 1:
    Testo = f1.readline()
    while count < 19:
      if Testo[indice] != "L":
        if ok == 0:
          indice += 1
      if Testo[indice] == "L":
        ok = 1
        indice += 1
      if Testo[indice] != "L" and ok == 1:
        if Testo[indice] == ";":
          count += 1
          indice += 1
        else:
          indice += 1
    while virgole != 4:
      if Testo[indice] == ";":
        s=s+Testo[indice]
        indice += 1
        virgole += 1
      if Testo[indice] != ";":
        s=s+Testo[indice]
        indice += 1
      if virgole == 4:
        listaColonne.insert(a, s[:-1])
        f2.write(listaColonne[a])
        
    if Testo == "":
      break
  f1.close()
  f2.close()
  return

#Aggiungo altre righe alla tabella
def OrdinaRigheDivisioni(Originale, Copia):
  f1 = Originale
  f2 = Copia
  listaRighe1 = []
  listaRighe2 = []
  listaRighe3 = []
  listaRighe4 = []
  listaRighe5 = []
  listaRighe6 = []
  a = 0
  indice = 0
  s = ""
  count = 0
  ok = 0
  virgole = 0
  punti = 0
  contatore = 0
  somma = 0
  con = 0
  val = 0
  totale = 0
  res = 0
  risultato = 0
  tot = 0
  while 1:
    Testo = f1.readline()
    while count < 23:
      if Testo[indice] != "L":
        if ok == 0:
          indice += 1
      if Testo[indice] == "L":
        ok = 1
        indice += 1
      if Testo[indice] != "L" and ok == 1:
        if Testo[indice] == ";":
          count += 1
          indice += 1
        else:
          indice += 1
    while virgole < 6:
      if Testo[indice] != ";" and val == 0:
        s=s+Testo[indice]
        indice += 1
      if Testo[indice] == ";" and val == 0:
        s=s+Testo[indice]
        newString = s.replace(",",".")
        listaRighe1.insert(a, newString)
        indice += 1
        virgole += 1
        s = ""
        val = 1
      if Testo[indice] != ";" and val == 1:
        s=s+Testo[indice]
        indice += 1
      if Testo[indice] == ";" and val == 1:
        s=s+Testo[indice]
        newString = s.replace(",",".")
        listaRighe2.insert(a, newString)
        indice += 1
        virgole += 1
        s = ""
        val = 2
      if Testo[indice] == ";" and val == 2:
        s=s+Testo[indice]
        newString = s.replace(",",".")
        listaRighe3.insert(a, newString)
        indice += 1
        virgole += 1
        s = ""
        val = 3
      if Testo[indice] != ";" and val == 2:
        s=s+Testo[indice]
        indice += 1
      if Testo[indice] == ";" and val == 3:
        s=s+Testo[indice]
        newString = s.replace(",",".")
        listaRighe4.insert(a, newString)
        indice += 1
        virgole += 1
        s = ""
        val = 4
      if Testo[indice] != ";" and val == 3:
        s=s+Testo[indice]
        indice += 1
      if Testo[indice] == ";" and val == 4:
        s=s+Testo[indice]
        newString = s.replace(",",".")
        listaRighe5.insert(a, newString)
        indice += 1
        virgole += 1
        s = ""
        val = 5
      if Testo[indice] != ";" and val == 4:
        s=s+Testo[indice]
        indice += 1
      if Testo[indice] == ";" and val == 5:
        s=s+Testo[indice]
        newString = s.replace(",",".")
        listaRighe6.insert(a, newString)
        indice += 1
        virgole += 1
        s = ""
        val = 6
      if Testo[indice] != ";" and val == 5:
        s=s+Testo[indice]
        indice += 1
    while totale != 6:
      if res == 0:
        if Testo[indice] == ";":
          s=s+Testo[indice]
          newString = s.replace(",",".")
          listaRighe1.append(newString)
          indice += 1
          totale += 1
          s = ""
          res = 1
        if Testo[indice] != ";":
          s=s+Testo[indice]
          indice += 1
      if res == 1:
        if Testo[indice] == ";":
          s=s+Testo[indice]
          newString = s.replace(",",".")
          listaRighe2.append(newString)
          indice += 1
          totale += 1
          s = ""
          res = 2
        if Testo[indice] != ";":
          s=s+Testo[indice]
          indice += 1
      if res == 2:
        if Testo[indice] == ";":
          s=s+Testo[indice]
          newString = s.replace(",",".")
          listaRighe3.append(newString)
          indice += 1
          totale += 1
          s = ""
          res = 3
        if Testo[indice] != ";":
          s=s+Testo[indice]
          indice += 1
      if res == 3:
        if Testo[indice] == ";":
          s=s+Testo[indice]
          newString = s.replace(",",".")
          listaRighe4.append(newString)
          indice += 1
          totale += 1
          s = ""
          res = 4
        if Testo[indice] != ";":
          s=s+Testo[indice]
          indice += 1
      if res == 4:
        if Testo[indice] == ";":
          s=s+Testo[indice]
          newString = s.replace(",",".")
          listaRighe5.append(newString)
          indice += 1
          totale += 1
          s = ""
          res = 5
        if Testo[indice] != ";":
          s=s+Testo[indice]
          indice += 1
      if res == 5:
        if Testo[indice] == ";":
          s=s+Testo[indice]
          newString = s.replace(",",".")
          listaRighe6.append(newString)
          indice += 1
          totale += 1
          s = ""
          res = 6
        if Testo[indice] != ";":
          s=s+Testo[indice]
          indice += 1
    while somma != 6:
      if con == 0:
        if Testo[indice] == ";":
          s=s+Testo[indice]
          newString = s.replace(",",".")
          listaRighe1.append(newString)
          indice += 1
          somma += 1
          s = ""
          con = 1
        if Testo[indice] != ";":
          s=s+Testo[indice]
          indice += 1
      if con == 1:
        if Testo[indice] == ";":
          s=s+Testo[indice]
          newString = s.replace(",",".")
          listaRighe2.append(newString)
          indice += 1
          somma += 1
          s = ""
          con = 2
        if Testo[indice] != ";":
          s=s+Testo[indice]
          indice += 1
      if con == 2:
        if Testo[indice] == ";":
          s=s+Testo[indice]
          newString = s.replace(",",".")
          listaRighe3.append(newString)
          indice += 1
          somma += 1
          s = ""
          con = 3
        if Testo[indice] != ";":
          s=s+Testo[indice]
          indice += 1
      if con == 3:
        if Testo[indice] == ";":
          s=s+Testo[indice]
          newString = s.replace(",",".")
          listaRighe4.append(newString)
          indice += 1
          somma += 1
          s = ""
          con = 4
        if Testo[indice] != ";":
          s=s+Testo[indice]
          indice += 1
      if con == 4:
        if Testo[indice] == ";":
          s=s+Testo[indice]
          newString = s.replace(",",".")
          listaRighe5.append(newString)
          indice += 1
          somma += 1
          s = ""
          con = 5
        if Testo[indice] != ";":
          s=s+Testo[indice]
          indice += 1
      if con == 5:
        if Testo[indice] == ";":
          s=s+Testo[indice]
          newString = s.replace(",",".")
          listaRighe6.append(newString)
          indice += 1
          somma += 1
          s = ""
          con = 6
        if Testo[indice] != ";":
          s=s+Testo[indice]
          indice += 1
    while risultato != 6:
      if tot == 0:
        if Testo[indice] == ";":
          s=s+Testo[indice]
          newString = s.replace(",",".")
          listaRighe1.append(newString)
          indice += 1
          risultato += 1
          s = ""
          tot = 1
        if Testo[indice] != ";":
          s=s+Testo[indice]
          indice += 1
      if tot == 1:
        if Testo[indice] == ";":
          s=s+Testo[indice]
          newString = s.replace(",",".")
          listaRighe2.append(newString)
          indice += 1
          risultato += 1
          s = ""
          tot = 2
        if Testo[indice] != ";":
          s=s+Testo[indice]
          indice += 1
      if tot == 2:
        if Testo[indice] == ";":
          s=s+Testo[indice]
          newString = s.replace(",",".")
          listaRighe3.append(newString)
          indice += 1
          risultato += 1
          s = ""
          tot = 3
        if Testo[indice] != ";":
          s=s+Testo[indice]
          indice += 1
      if tot == 3:
        if Testo[indice] == ";":
          s=s+Testo[indice]
          newString = s.replace(",",".")
          listaRighe4.append(newString)
          indice += 1
          risultato += 1
          s = ""
          tot = 4
        if Testo[indice] != ";":
          s=s+Testo[indice]
          indice += 1
      if tot == 4:
        if Testo[indice] == ";":
          s=s+Testo[indice]
          newString = s.replace(",",".")
          listaRighe5.append(newString)
          indice += 1
          risultato += 1
          s = ""
          tot = 5
        if Testo[indice] != ";":
          s=s+Testo[indice]
          indice += 1
      if tot == 5:
        if Testo[indice] == ";":
          s=s+Testo[indice]
          newString = s.replace(",",".")
          listaRighe6.append(newString)
          indice += 1
          risultato += 1
          s = ""
          tot = 6
        if Testo[indice] != ";":
          s=s+Testo[indice]
          indice += 1
        
    if Testo == "":
      break
    for line in listaRighe1:
      f2.write(line)
    f2.write("\n")  
    for line in listaRighe2:
      f2.write(line)
    f2.write("\n")
    for line in listaRighe3:
      f2.write(line)
    f2.write("\n")
    for line in listaRighe4:
      f2.write(line)
    f2.write("\n")
    for line in listaRighe5:
      f2.write(line)
    f2.write("\n")
    for line in listaRighe6:
      f2.write(line)
    f2.write("\n")
  f1.close()
  f2.close()
  return

#Aggiungo altre colonne alla tabella
def OrdinaRigheDivisioni1(Originale, Copia):
  f1 = Originale
  f2 = Copia
  listaRighe = []
  a=0
  indice = 0
  s = ""
  count = 0
  ok = 0
  virgole = 0
  while 1:
    Testo = f1.readline()
    while count < 13:
      if Testo[indice] != "L":
        if ok == 0:
          indice += 1
      if Testo[indice] == "L":
        ok = 1
        indice += 1
      if Testo[indice] != "L" and ok == 1:
        if Testo[indice] == ";":
          count += 1
          indice += 1
        else:
          indice += 1
    while virgole != 4:
      if Testo[indice] == ";":
        s=s+Testo[indice]
        indice += 1
        virgole += 1
      if Testo[indice] != ";":
        s=s+Testo[indice]
        indice += 1
      if virgole == 4:
        newString = s.replace(",",".")
        listaRighe.insert(a, newString[:-1])
        f2.write(listaRighe[a])
        
    if Testo == "":
      break
  f1.close()
  f2.close()
  return

#Aggiungo altre colonne alla tabella
def OrdinaColonneVLVR(Originale, Copia):
  f1 = Originale
  f2 = Copia
  listaColonne = []
  a=0
  indice = 0
  s = ""
  count = 0
  ok = 0
  virgole = 0
  num = 0
  punti = 0
  contatore = 0
  somma = 0
  conteggio = 0
  while 1:
    Testo = f1.readline()
    while count < 47:
      if Testo[indice] != "L":
        if ok == 0:
          indice += 1
      if Testo[indice] == "L":
        ok = 1
        indice += 1
      if Testo[indice] != "L" and ok == 1:
        if Testo[indice] == ";":
          count += 1
          indice += 1
        else:
          indice += 1
    while virgole != 2:
      if Testo[indice] == ";":
        if num == 1:
          s=s+Testo[indice]
          virgole += 1
        if num == 0:
          num = 1
          indice += 1
      if Testo[indice] != ";":
        s=s+Testo[indice]
        indice += 1
      if virgole == 2:
        listaColonne.insert(a, s[:-1])
        indice += 1
        s = s[:-1]
    while conteggio < 6:
      if Testo[indice] != ";":
        indice += 1
      if Testo[indice] == ";":
        conteggio += 1
        indice += 1
    while punti < 2:
      if Testo[indice] == ";":
        if contatore == 1:
          s=s+Testo[indice]
          punti += 1
        if contatore == 0:
           contatore = 1
           indice += 1
      if Testo[indice] != ";":
        s = s + Testo[indice]
        indice += 1
      if punti == 2:
        listaColonne.insert(a, s[:-1])
        f2.write(listaColonne[a])
        
    if Testo == "":
      break
  f1.close()
  f2.close()
  return

#Aggiungo altre colonne alla tabella
def OrdinaColonneVL1(Originale, Copia):
  f1 = Originale
  f2 = Copia
  listaColonne = []
  a=0
  indice = 0
  s = ""
  count = 0
  ok = 0
  virgole = 0
  num = 0
  while 1:
    Testo = f1.readline()
    while count < 17:
      if Testo[indice] != "L":
        if ok == 0:
          indice += 1
      if Testo[indice] == "L":
        ok = 1
        indice += 1
      if Testo[indice] != "L" and ok == 1:
        if Testo[indice] == ";":
          count += 1
          indice += 1
        else:
          indice += 1
    while virgole != 2:
      if Testo[indice] == ";":
        if num == 1:
          s=s+Testo[indice]
          virgole += 1
        if num == 0:
          num = 1
          indice += 1
      if Testo[indice] != ";":
        s=s+Testo[indice]
        indice += 1
      if virgole == 2:
        listaColonne.insert(a, s[:-1])
        f2.write(listaColonne[a])
        
    if Testo == "":
      break
  f1.close()
  f2.close()
  return

#Aggiungo altre righe alla tabella
def OrdinaRigheVLVR(Originale, Copia):
  f1 = Originale
  f2 = Copia
  listaRighe1 = []
  listaRighe2 = []
  listaRighe3 = []
  listaRighe4 = []
  listaRighe5 = []
  listaRighe6 = []
  a = 0
  indice = 0
  s = ""
  count = 0
  ok = 0
  virgole = 0
  punti = 0
  contatore = 0
  somma = 0
  con = 0
  val = 0
  while 1:
    Testo = f1.readline()
    while count < 49:
      if Testo[indice] != "L":
        if ok == 0:
          indice += 1
      if Testo[indice] == "L":
        ok = 1
        indice += 1
      if Testo[indice] != "L" and ok == 1:
        if Testo[indice] == ";":
          count += 1
          indice += 1
        else:
          indice += 1
    while virgole < 6:
      if Testo[indice] != ";" and val == 0:
        s=s+Testo[indice]
        indice += 1
      if Testo[indice] == ";" and val == 0:
        s=s+Testo[indice]
        newString = s.replace(",",".")
        listaRighe1.insert(a, newString)
        indice += 1
        virgole += 1
        s = ""
        val = 1
      if Testo[indice] != ";" and val == 1:
        s=s+Testo[indice]
        indice += 1
      if Testo[indice] == ";" and val == 1:
        s=s+Testo[indice]
        newString = s.replace(",",".")
        listaRighe2.insert(a, newString)
        indice += 1
        virgole += 1
        s = ""
        val = 2
      if Testo[indice] == ";" and val == 2:
        s=s+Testo[indice]
        newString = s.replace(",",".")
        listaRighe3.insert(a, newString)
        indice += 1
        virgole += 1
        s = ""
        val = 3
      if Testo[indice] != ";" and val == 2:
        s=s+Testo[indice]
        indice += 1
      if Testo[indice] == ";" and val == 3:
        s=s+Testo[indice]
        newString = s.replace(",",".")
        listaRighe4.insert(a, newString)
        indice += 1
        virgole += 1
        s = ""
        val = 4
      if Testo[indice] != ";" and val == 3:
        s=s+Testo[indice]
        indice += 1
      if Testo[indice] == ";" and val == 4:
        s=s+Testo[indice]
        newString = s.replace(",",".")
        listaRighe5.insert(a, newString)
        indice += 1
        virgole += 1
        s = ""
        val = 5
      if Testo[indice] != ";" and val == 4:
        s=s+Testo[indice]
        indice += 1
      if Testo[indice] == ";" and val == 5:
        s=s+Testo[indice]
        newString = s.replace(",",".")
        listaRighe6.insert(a, newString)
        indice += 1
        virgole += 1
        s = ""
        val = 6
      if Testo[indice] != ";" and val == 5:
        s=s+Testo[indice]
        indice += 1
    while punti < 2:
      if Testo[indice] != ";":
        indice += 1
      if Testo[indice] == ";":
        indice += 1
        punti += 1
    while somma != 6:
      if con == 0:
        if Testo[indice] == ";":
          s=s+Testo[indice]
          newString = s.replace(",",".")
          listaRighe1.append(newString)
          indice += 1
          somma += 1
          s = ""
          con = 1
        if Testo[indice] != ";":
          s=s+Testo[indice]
          indice += 1
      if con == 1:
        if Testo[indice] == ";":
          s=s+Testo[indice]
          newString = s.replace(",",".")
          listaRighe2.append(newString)
          indice += 1
          somma += 1
          s = ""
          con = 2
        if Testo[indice] != ";":
          s=s+Testo[indice]
          indice += 1
      if con == 2:
        if Testo[indice] == ";":
          s=s+Testo[indice]
          newString = s.replace(",",".")
          listaRighe3.append(newString)
          indice += 1
          somma += 1
          s = ""
          con = 3
        if Testo[indice] != ";":
          s=s+Testo[indice]
          indice += 1
      if con == 3:
        if Testo[indice] == ";":
          s=s+Testo[indice]
          newString = s.replace(",",".")
          listaRighe4.append(newString)
          indice += 1
          somma += 1
          s = ""
          con = 4
        if Testo[indice] != ";":
          s=s+Testo[indice]
          indice += 1
      if con == 4:
        if Testo[indice] == ";":
          s=s+Testo[indice]
          newString = s.replace(",",".")
          listaRighe5.append(newString)
          indice += 1
          somma += 1
          s = ""
          con = 5
        if Testo[indice] != ";":
          s=s+Testo[indice]
          indice += 1
      if con == 5:
        if Testo[indice] == ";":
          s=s+Testo[indice]
          newString = s.replace(",",".")
          listaRighe6.append(newString)
          indice += 1
          somma += 1
          s = ""
          con = 6
        if Testo[indice] != ";":
          s=s+Testo[indice]
          indice += 1      
        
    if Testo == "":
      break
    for line in listaRighe1:
      f2.write(line)
    f2.write("\n")  
    for line in listaRighe2:
      f2.write(line)
    f2.write("\n")
    for line in listaRighe3:
      f2.write(line)
    f2.write("\n")
    for line in listaRighe4:
      f2.write(line)
    f2.write("\n")
    for line in listaRighe5:
      f2.write(line)
    f2.write("\n")
    for line in listaRighe6:
      f2.write(line)
    f2.write("\n")
  f1.close()
  f2.close()
  return

#Aggiungo altre righe alla tabella
def OrdinaRigheVL1(Originale, Copia):
  f1 = Originale
  f2 = Copia
  listaRighe = []
  a = 0
  indice = 0
  s = ""
  count = 0
  ok = 0
  virgole = 0
  while 1:
    Testo = f1.readline()
    while count < 19:
      if Testo[indice] != "L":
        if ok == 0:
          indice += 1
      if Testo[indice] == "L":
        ok = 1
        indice += 1
      if Testo[indice] != "L" and ok == 1:
        if Testo[indice] == ";":
          count += 1
          indice += 1
        else:
          indice += 1
    while virgole != 1:
      if Testo[indice] == ";":
        s=s+Testo[indice]
        virgole += 1
      if Testo[indice] != ";":
        s=s+Testo[indice]
        indice += 1
      if virgole == 1:
        newString = s.replace(",",".")
        listaRighe.insert(a, newString)
        f2.write(listaRighe[a])
        
    if Testo == "":
      break
  f1.close()
  f2.close()
  return

#Aggiungo altre colonne alla tabella
def OrdinaUltimeColonne(Originale, Copia):
  f1 = Originale
  f2 = Copia
  listaColonne = []
  a=0
  indice = 0
  s = ""
  count = 0
  ok = 0
  virgole = 0
  while 1:
    Testo = f1.readline()
    while count < 32:
      if Testo[indice] != "G":
        if ok == 0:
          indice += 1
      if Testo[indice] == "G":
        ok = 1
        indice += 1
      if Testo[indice] != "G" and ok == 1:
        if Testo[indice] == ";":
          count += 1
          indice += 1
        else:
          indice += 1
    while virgole != 1:
      if Testo[indice] == ";":
        s=s+Testo[indice]
        virgole += 1
      if Testo[indice] != ";":
        s=s+Testo[indice]
        indice += 1
      if virgole == 1:
        listaColonne.insert(a, s)
        f2.write(listaColonne[a])
        indice += 1
        
    if Testo == "":
      break
  f1.close()
  f2.close()
  return

#Aggiungo altre colonne alla tabella
def OrdinaUltimeColonne1(Originale, Copia):
  f1 = Originale
  f2 = Copia
  listaColonne = []
  a=0
  indice = 0
  s = ""
  count = 0
  ok = 0
  virgole = 0
  num = 0
  punti = 0
  contatore = 0
  somma = 0
  while 1:
    Testo = f1.readline()
    while count < 13:
      if Testo[indice] != "G":
        if ok == 0:
          indice += 1
      if Testo[indice] == "G":
        ok = 1
        indice += 1
      if Testo[indice] != "G" and ok == 1:
        if Testo[indice] == ";":
          count += 1
          indice += 1
        else:
          indice += 1
    while virgole != 2:
      if Testo[indice] == ";":
        if num == 1:
          s=s+Testo[indice]
          virgole += 1
        if num == 0:
          num = 1
          indice += 1
      if Testo[indice] != ";":
        s=s+Testo[indice]
        indice += 1
      if virgole == 2:
        listaColonne.insert(a, s[:-1])
        indice += 1
        s = s[:-1]
    while punti != 2:
      if Testo[indice] != ";":
        if contatore == 0:
          indice += 1
        if contatore == 1:
          s=s+Testo[indice]
          indice += 1
      if Testo[indice] == ";":
        if contatore == 1:
          s=s+Testo[indice]
          punti += 1
        if contatore == 0:
          contatore = 1
          indice += 1   
      if punti == 2:
        listaColonne.insert(a, s[:-1])
        f2.write(listaColonne[a])
        
    if Testo == "":
      break
  f1.close()
  f2.close()
  return

#Aggiungo altre colonne alla tabella
def OrdinaUltimeRighe(Originale, Copia):
  f1 = Originale
  f2 = Copia
  listaRighe1 = []
  listaRighe2 = []
  listaRighe3 = []
  listaRighe4 = []
  listaRighe5 = []
  listaRighe6 = []
  a=0
  indice = 0
  s = ""
  count = 0
  ok = 0
  virgole = 0
  somma = 0
  con = 0
  while 1:
    Testo = f1.readline()
    while count < 33:
      if Testo[indice] != "G":
        if ok == 0:
          indice += 1
      if Testo[indice] == "G":
        ok = 1
        indice += 1
      if Testo[indice] != "G" and ok == 1:
        if Testo[indice] == ";":
          count += 1
          indice += 1
        else:
          indice += 1
    while somma != 6:
      if con == 0:
        if Testo[indice] == ";":
          s=s+Testo[indice]
          newString = s.replace(",",".")
          listaRighe1.append(newString)
          indice += 1
          somma += 1
          s = ""
          con = 1
        if Testo[indice] != ";":
          s=s+Testo[indice]
          indice += 1
      if con == 1:
        if Testo[indice] == ";":
          s=s+Testo[indice]
          newString = s.replace(",",".")
          listaRighe2.append(newString)
          indice += 1
          somma += 1
          s = ""
          con = 2
        if Testo[indice] != ";":
          s=s+Testo[indice]
          indice += 1
      if con == 2:
        if Testo[indice] == ";":
          s=s+Testo[indice]
          newString = s.replace(",",".")
          listaRighe3.append(newString)
          indice += 1
          somma += 1
          s = ""
          con = 3
        if Testo[indice] != ";":
          s=s+Testo[indice]
          indice += 1
      if con == 3:
        if Testo[indice] == ";":
          s=s+Testo[indice]
          newString = s.replace(",",".")
          listaRighe4.append(newString)
          indice += 1
          somma += 1
          s = ""
          con = 4
        if Testo[indice] != ";":
          s=s+Testo[indice]
          indice += 1
      if con == 4:
        if Testo[indice] == ";":
          s=s+Testo[indice]
          newString = s.replace(",",".")
          listaRighe5.append(newString)
          indice += 1
          somma += 1
          s = ""
          con = 5
        if Testo[indice] != ";":
          s=s+Testo[indice]
          indice += 1
      if con == 5:
        if Testo[indice] == ";":
          s=s+Testo[indice]
          newString = s.replace(",",".")
          listaRighe6.append(newString)
          indice += 1
          somma += 1
          s = ""
          con = 6
        if Testo[indice] != ";":
          s=s+Testo[indice]
          indice += 1      
        
    if Testo == "":
      break
    for line in listaRighe1:
      f2.write(line)
    f2.write("\n")  
    for line in listaRighe2:
      f2.write(line)
    f2.write("\n")
    for line in listaRighe3:
      f2.write(line)
    f2.write("\n")
    for line in listaRighe4:
      f2.write(line)
    f2.write("\n")
    for line in listaRighe5:
      f2.write(line)
    f2.write("\n")
    for line in listaRighe6:
      f2.write(line)
    f2.write("\n")
        
    if Testo == "":
      break
  f1.close()
  f2.close()
  return

#Aggiungo altre righe alla tabella
def OrdinaUltimeRighe1(Originale, Copia):
  f1 = Originale
  f2 = Copia
  listaRighe = []
  a = 0
  indice = 0
  s = ""
  count = 0
  ok = 0
  virgole = 0
  punti = 0
  contatore = 0
  somma = 0
  con = 0
  while 1:
    Testo = f1.readline()
    while count < 15:
      if Testo[indice] != "G":
        if ok == 0:
          indice += 1
      if Testo[indice] == "G":
        ok = 1
        indice += 1
      if Testo[indice] != "G" and ok == 1:
        if Testo[indice] == ";":
          count += 1
          indice += 1
        else:
          indice += 1
    while virgole != 1:
      if Testo[indice] == ";":
        s=s+Testo[indice]
        virgole += 1
      if Testo[indice] != ";":
        s=s+Testo[indice]
        indice += 1
      if virgole == 1:
        listaRighe.insert(a, s)
    while punti != 1:
      if Testo[indice] != ";":
        if contatore == 0 and con != 2:
          indice += 1
        if contatore == 1:
          s=s+Testo[indice]
          indice += 1
        if con == 2:
          s=s+Testo[indice]
          indice += 1
          somma = 1
      if Testo[indice] == ";":
        if contatore == 0 and somma != 1:
          con += 1
          indice += 1
        if somma == 1:
          s=s+Testo[indice]
          punti += 1
           
      if punti == 1:
        newString = s.replace(",",".")
        listaRighe.insert(a, newString)
        f2.write(listaRighe[a])
        
    if Testo == "":
      break
  f1.close()
  f2.close()
  return


print "Inizio ricerca e conversione."
#Devo mettermi in attesa dei PDF e analizzarli uno per uno
#Come punto di partenza metto la cartella con i PDF dei pazienti e devo fare match con i file .pdf
rootPath = '/home/bottaid/Scrivania/Kinetic/Pazienti/'
pattern = '*.pdf'
print 'Modello :', pattern

files = os.listdir(rootPath)
print 'File    :', files
print 'Corrispondenze :', fnmatch.filter(files, pattern)

for root, dirs, files in os.walk(rootPath):
    print "Directory Pazienti: ", dirs
    for files in dirs:
        print "Filename:", files
        for obj in filename:
            print "File nelle cartelle: ", obj
            for filename in fnmatch.filter(files, pattern):
                print "Filtri: ", fnmatch.filter(files, pattern)
                newPath = os.path.join(rootPath, filename)
                newPath1 = os.path.join(rootPath, "Scheda.txt")
                f1 = open(newPath, "r")
                f2 = open(newPath1, "w")
                text = textract.process(newPath)
                f2.write(text)
                f1.close()
                f2.close()

                newPath2 = os.path.join(rootPath, "Misurazioni.txt")
                f3 = open(newPath1, "r")
                f4 = open(newPath2, "w")

                NumeroMisurazioni(f3, f4)
                f3.close()
                f4.close()

                newPath3 = os.path.join(rootPath, "Report.txt")
                f3 = open(newPath1, "r")
                f5 = open(newPath3, "w")
                CopiaReport(f3, f5)
                f3.close()
                f5.close()                       

                newPath4 = os.path.join(rootPath, "Dati.txt")
                f3 = open(newPath1, "r")
                f5 = open(newPath4, "w")
                CopiaFile(f3, f5)
                f3.close()
                f5.close()

                fmis = open(newPath2, "r")
                if fmis.read() == "1":
                  f6 = open(newPath4, "r")
                  newPath5 = os.path.join(rootPath, "OrdinaColonne.txt")
                  f7 = open(newPath5, "w")
                  OrdinaColonne(f6, f7)
                  f6.close()
                  f7.close()

                  f6 = open(newPath4, "r")
                  newPath6 = os.path.join(rootPath, "OrdinaRighe.txt")
                  f7 = open(newPath6, "w")
                  OrdinaRighe1(f6, f7)
                  f6.close()
                  f7.close()

                  f6 = open(newPath4, "r")
                  newPath7 = os.path.join(rootPath, "OrdinaColonneRL.txt")
                  f7 = open(newPath7, "w")
                  OrdinaColonneRL(f6, f7)
                  f6.close()
                  f7.close()

                  f6 = open(newPath4, "r")
                  newPath8 = os.path.join(rootPath, "OrdinaRigheRL.txt")
                  f7 = open(newPath8, "w")
                  OrdinaRigheRL1(f6, f7)
                  f6.close()
                  f7.close()

                  f6 = open(newPath4, "r")
                  newPath9 = os.path.join(rootPath, "OrdinaColonneDivisioni.txt")
                  f7 = open(newPath9, "w")
                  OrdinaColonneDivisioni1(f6, f7)
                  f6.close()
                  f7.close()

                  f6 = open(newPath4, "r")
                  newPath10 = os.path.join(rootPath, "OrdinaRigheDivisioni.txt")
                  f7 = open(newPath10, "w")
                  OrdinaRigheDivisioni1(f6, f7)
                  f6.close()
                  f7.close()

                  f6 = open(newPath4, "r")
                  newPath11 = os.path.join(rootPath, "OrdinaColonneVL.txt")
                  f7 = open(newPath11, "w")
                  OrdinaColonneVL1(f6, f7)
                  f6.close()
                  f7.close()

                  f6 = open(newPath4, "r")
                  newPath12 = os.path.join(rootPath, "OrdinaRigheVL.txt")
                  f7 = open(newPath12, "w")
                  OrdinaRigheVL1(f6, f7)
                  f6.close()
                  f7.close()

                  f6 = open(newPath4, "r")
                  newPath13 = os.path.join(rootPath, "OrdinaUltimeColonne.txt")
                  f7 = open(newPath13, "w")
                  OrdinaUltimeColonne1(f6, f7)
                  f6.close()
                  f7.close()

                  f6 = open(newPath4, "r")
                  newPath14 = os.path.join(rootPath, "OrdinaUltimeRighe.txt")
                  f7 = open(newPath14, "w")
                  OrdinaUltimeRighe1(f6, f7)
                  f6.close()
                  f7.close()

                  newPath20 = os.path.join(rootPath, "SchedaFinale.csv")
                  f = open(newPath20, "w")
                  f1 = open(newPath5, "r")
                  f2 = open(newPath6, "r")
                  f3 = open(newPath7, "r")
                  f4 = open(newPath8, "r")
                  f5 = open(newPath3, "r")
                  f6 = open(newPath9, "r")
                  f7 = open(newPath10, "r")
                  f8 = open(newPath11, "r")
                  f9 = open(newPath12, "r")
                  f10 = open(newPath13, "r")
                  f11 = open(newPath14, "r")

                  for line in f5.readlines():
                      f.write(line)
                  f.write("\n")
                  f.write(f1.readline())
                  f.write(f3.readline())
                  f.write(f6.readline())
                  f.write(f8.readline())
                  f.write(f10.readline())
                  f.write("\n")
                  f.write(f2.readline())
                  f.write(f4.readline())
                  f.write(f7.readline())
                  f.write(f9.readline())
                  f.write(f11.readline())

                  fmis.close()
                  f.close()

                fmis = open(newPath2, "r")
                if fmis.read() == "6":
                  f6 = open(newPath4, "r")
                  newPath5 = os.path.join(rootPath, "OrdinaColonne.txt")
                  f7 = open(newPath5, "w")
                  OrdinaColonne(f6, f7)
                  f6.close()
                  f7.close()

                  f6 = open(newPath4, "r")
                  newPath6 = os.path.join(rootPath, "OrdinaRighe.txt")
                  f7 = open(newPath6, "w")
                  OrdinaRighe(f6, f7)
                  f6.close()
                  f7.close()

                  f6 = open(newPath4, "r")
                  newPath7 = os.path.join(rootPath, "OrdinaRigheNome.txt")
                  f7 = open(newPath7, "w")
                  OrdinaRigheNome(f6, f7)
                  f6.close()
                  f7.close()

                  f6 = open(newPath4, "r")
                  newPath8 = os.path.join(rootPath, "OrdinaRigheData.txt")
                  f7 = open(newPath8, "w")
                  OrdinaRigheData(f6, f7)
                  f6.close()
                  f7.close()
                
                  f6 = open(newPath4, "r")
                  newPath9 = os.path.join(rootPath, "OrdinaColonneRL.txt")
                  f7 = open(newPath9, "w")
                  OrdinaColonneRL(f6, f7)
                  f6.close()
                  f7.close()

                  f6 = open(newPath4, "r")
                  newPath10 = os.path.join(rootPath, "OrdinaRigheRL.txt")
                  f7 = open(newPath10, "w")
                  OrdinaRigheRL(f6, f7)
                  f6.close()
                  f7.close()

                  f6 = open(newPath4, "r")
                  newPath11 = os.path.join(rootPath, "OrdinaColonneDivisioni.txt")
                  f7 = open(newPath11, "w")
                  OrdinaColonneDivisioni(f6, f7)
                  f6.close()
                  f7.close()

                  f6 = open(newPath4, "r")
                  newPath12 = os.path.join(rootPath, "OrdinaRigheDivisioni.txt")
                  f7 = open(newPath12, "w")
                  OrdinaRigheDivisioni(f6, f7)
                  f6.close()
                  f7.close()

                  f6 = open(newPath4, "r")
                  newPath13 = os.path.join(rootPath, "OrdinaColonneVLVR.txt")
                  f7 = open(newPath13, "w")
                  OrdinaColonneVLVR(f6, f7)
                  f6.close()
                  f7.close()

                  f6 = open(newPath4, "r")
                  newPath14 = os.path.join(rootPath, "OrdinaRigheVLVR.txt")
                  f7 = open(newPath14, "w")
                  OrdinaRigheVLVR(f6, f7)
                  f6.close()
                  f7.close()

                  f6 = open(newPath4, "r")
                  newPath15 = os.path.join(rootPath, "OrdinaUltimeColonne.txt")
                  f7 = open(newPath15, "w")
                  OrdinaUltimeColonne(f6, f7)
                  f6.close()
                  f7.close()

                  f6 = open(newPath4, "r")
                  newPath16 = os.path.join(rootPath, "OrdinaUltimeRighe.txt")
                  f7 = open(newPath16, "w")
                  OrdinaUltimeRighe(f6, f7)
                  f6.close()
                  f7.close()
                  f5.close() 

                  #Inserisco i contenuti delle righe della tabella
                  newPath17 = os.path.join(rootPath, "ProvaRighe.txt")
                  f = open(newPath17, "w")
                  f1 = open(newPath6, "r")
                  f2 = open(newPath7, "r")
                  f3 = open(newPath8, "r")
                  f4 = open(newPath10, "r")
                  f5 = open(newPath12, "r")
                  f6 = open(newPath14, "r")
                  f7 = open(newPath16, "r")

                  f.write(f1.readline()[:-1]+f2.readline()[:-1]+f3.readline()[:-1]+f4.readline()[:-1]+f5.readline()[:-1]+f6.readline()[:-1]+f7.readline())
                  f.write(f1.readline()[:-1]+f2.readline()[:-1]+f3.readline()[:-1]+f4.readline()[:-1]+f5.readline()[:-1]+f6.readline()[:-1]+f7.readline())
                  f.write(f1.readline()[:-1]+f2.readline()[:-1]+f3.readline()[:-1]+f4.readline()[:-1]+f5.readline()[:-1]+f6.readline()[:-1]+f7.readline())
                  f.write(f1.readline()[:-1]+f2.readline()[:-1]+f3.readline()[:-1]+f4.readline()[:-1]+f5.readline()[:-1]+f6.readline()[:-1]+f7.readline())
                  f.write(f1.readline()[:-1]+f2.readline()[:-1]+f3.readline()[:-1]+f4.readline()[:-1]+f5.readline()[:-1]+f6.readline()[:-1]+f7.readline())
                  f.write(f1.readline()[:-1]+f2.readline()[:-1]+f3.readline()[:-1]+f4.readline()[:-1]+f5.readline()[:-1]+f6.readline()[:-1]+f7.readline())

                  fmis.close()
                  f.close()

                  #Inserisco le colonne
                  newPath18 = os.path.join(rootPath, "ProvaColonne.txt")
                  f = open(newPath18, "w")
                  f1 = open(newPath5, "r")
                  f2 = open(newPath9, "r")
                  f3 = open(newPath11, "r")
                  f4 = open(newPath13, "r")
                  f5 = open(newPath15, "r")

                  f.write(f1.readline()+f2.readline()+f3.readline()+f4.readline()+f5.readline())

                  f.close()

                  #Inserimento di TUTTO il contenuto nel file .csv del paziente (in questo caso DiMartino.csv)
                  newPath20 = os.path.join(rootPath, "SchedaFinale.csv")
                  f = open(newPath20, "w")
                  f1 = open(newPath18, "r")
                  f2 = open(newPath17, "r")
                  f3 = open(newPath3, "r")

                  for line in f3.readlines():
                    f.write(line)
                  f.write("\n")

                  f.write(f1.readline())
                  f.write("\n")

                  for line in f2.readlines():
                      f.write(line)
                  f.close()

print "Files convertiti."

