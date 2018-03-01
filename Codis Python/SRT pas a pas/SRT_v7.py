""" Objectiu: Generar fitxer '.SRT' partint del fitxers de paraules '.lab'."""

import os 
import sys

#Obro fitxer de lectura
fLab = open('arxiu73_words_002.lab', 'r')

ResList = [] #Llista resultant

AuxList = []*3 #Llista on es fa el processat de la subfrase

Linia = []#Llista on s'agafa cada linia del fitxer

num_subt = 0

for lin in fLab:

  Linia = lin.split(' ') #Parteixo linia en els 3 paràmetres que la formen

  if(Linia[2].isupper()): 

    if(len(AuxList) != 0): #Si llista Auxiliar és plena...

      ResList.append(AuxList)
      
      AuxList = [] #Buidar llista Auxiliar

    ResList.append(Linia)


  else:

    if(len(AuxList) == 0): #Si llista Auxiliar és buida...

      AuxList = Linia[:] #Copio contingut llista línia en Auxiliar

    else:

      if(len(AuxList[2] + Linia[2]) <= 35): #Si longitud subfrase més paraules es inferior a 35...

        AuxList[2] = AuxList[2] + Linia[2] #Juntar els strings en llista auxiliar

        AuxList[1] = Linia[1] #Agafar marca de temps final     

      else:

        ResList.append(AuxList)

        AuxList = Linia[:] #Copio contingut llista línia en Auxiliar



while num_subt < len(ResList):

  MeuString = ResList[num_subt][2].split()

  ' '.join(MeuString)

  ResList[num_subt][2] = MeuString

  print(str(num_subt+1))
  print(ResList[num_subt][0]," --> ",ResList[num_subt][1])
  print(ResList[num_subt][2])
  print('')

  num_subt += 1

fLab.close()