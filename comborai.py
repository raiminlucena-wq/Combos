import os,pip
import random
import sys
import time
import names

#os.system('clear')
time.sleep(0.1)
print ("""
 \33[96m
  ꧁🅲🅾🅼🅱🅾 🅼🅰🅺🅴🆁 & 🅼3🆄 🆂🅲🅰🅽🅽🅴🆁꧂                
           ꧁️☠️Raimin ☠️꧂       
  \33[31m
""")
time.sleep(0.1)
print ("""
 🄲🄾🄼🄱🄾 🄾🄿🅃🄸🄾🄽🅂:                      
 
 \33[0m\33[32m
1)NOMBRE:NOMBRE(Mix)

2)Nombres(Mayusculas,Minusculas)
Ejemplo:
Juan
juan

0) PARA SALIR A SCANEAR
\33[33m


""")
menu = input("Enter Option :")


		

if menu=="1":
	print ("\t\t\33[1;33m (.txt) escriba \33[36m ")
	filename = input("\nNombre su Combo  :  ")
	hwm = int(input("cuantas lineas? : "))
	i=1
	for i in range (0,hwm):
		i = 1+1
		rname = names.get_first_name()
		rlastname = names.get_last_name()
		num = random.randint(1,100000)
		all1 = "%s%s"%(rname,num)
		alln = "%s%s%s%s"%(all1,":",rname,num)
		all2 = "%s%s"%(rlastname,num)
		allf = "%s%s%s%s"%(all2,":",rlastname,num)
		all3 = "%s%s"%(rname,num)
		alln = "%s%s%s%s"%(all3,":",rname,num)
		all4 = "%s%s"%(rlastname,num)
		allf = "%s%s%s%s"%(all4,":",rlastname,num)
		all5 = "%s%s"%(rname,2022)
		alls = "%s%s%s%s"%(all5,":",rname,2022)
		all6 = "%s%s"%(rlastname,2022)
		allg = "%s%s%s%s"%(all6,":",rlastname,2022)
		all7 = "%s%s"%(rname,2023)
		alle = "%s%s%s%s"%(all7,":",rname,2023)
		all8 = "%s%s"%(rlastname,2023)
		alld = "%s%s%s%s"%(all8,":",rlastname,2023)
		all9 = "%s"%(rname)
		allt = "%s%s%s"%(all9,":",rname)
		all10 = "%s"%(rlastname)
		ally = "%s%s%s"%(all10,":",rlastname)
		all11 = "%s%s"%(rname,123)
		allp = "%s%s%s%s"%(all11,":",rname,123)
		all12 = "%s%s"%(rlastname,123)
		allj = "%s%s%s%s"%(all12,":",rlastname,123)
		all13 = "%s"%(num)
		allv = "%s%s%s"%(all13,":",num)
		print(alln)
		print(allf)
		print(alln.lower())
		print(allf.lower())
		print(alls.upper())
		print(allg.upper())
		print(alle.lower())
		print(alld.lower())
		print(allt.lower())
		print(ally.lower())
		print(allt)
		print(ally)
		print(allp.lower())
		print(allj.lower())
		print(allv)
		F ="/sdcard/combo/"+filename+".txt"
		f = open(F, "a+",encoding= "utf-8")
		f.write(alln)
		f.write("\n")
		f.write(allf)
		f.write("\n")
		f.write(alln.lower())
		f.write("\n")
		f.write(allf.lower())
		f.write("\n")
		f.write(alls.upper())
		f.write("\n")
		f.write(allg.upper())
		f.write("\n")
		f.write(alle.lower())
		f.write("\n")
		f.write(alld.lower())
		f.write("\n")
		f.write(allt.lower())
		f.write("\n")
		f.write(ally.lower())
		f.write("\n")
		f.write(allt.upper())
		f.write("\n")
		f.write(ally.upper())
		f.write("\n")
		f.write(allp.lower())
		f.write("\n")
		f.write(allj.lower())
		f.write("\n")
		f.write(allp.upper())
		f.write("\n")
		f.write(allj.upper())
		f.write("\n")
		f.write(allv)
		f.write("\n")
		f.close()
		i = 1
		
if menu=="2":
	print ("\t\t\33[1;336m (.txt) escriba \33[36m ")
	filename = input("\nNombre su Combo  : ")
	hwm = int(input("numero de lineas (x2): "))
	i=1
	for i in range (0,hwm):
		i = 1+1
		rname = names.get_first_name()
		rlastname = names.get_last_name()
		num = random.randint(0,0)
		all1 = "%s"%(rname)
		alln = "%s%s"%(all1," ",)
		all2 = "%s"%(rname)
		alln = "%s%s"%(all2," ",) 
		all3 = "%s"%(rname)
		alle = "%s%s"%(all3," ",)
		 
		
		print(alln)
		print(alln.lower())
		print(alle.upper())
		F ="/sdcard/combo/"+filename+".txt"
		f = open(F, "a+",encoding= "utf-8")
		f.write(alln)
		f.write("\n")
		f.write(alln.lower())
		f.write("\n")
		f.write(alle.upper())
		f.write("\n")

		f.close()
		i += 1



print ("\33[1;37;33m")

if menu=="99":
     x = input("\n \33[33m YA ESTAS LISTO TU NUEVO COMBO...")