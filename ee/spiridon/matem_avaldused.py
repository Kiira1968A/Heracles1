'''
Created on 18. okt 2021

@author: spiridon
'''
1 + 2
print(1 + 2)
one = '4'
two = '26'
print(one + two)
penta = [1, 2, 3, 4, 5]
print(penta)
heksa = [1, 2, 3, 4, 5, 6]
print(heksa + penta)
penta1 = ('a', 'b', 'c', 'd', 'e')
heksa1 = ['f', 'g', 'h', 'i', 'j', 'k']
print(heksa1[3])
# heksa1 toon valja 4. elemendi , kasutan [ ] sulge , lugemine algab alati
# 0-st.
print(penta1[1])
# penta1,toon valja 1.elemendi,kasutan [ ]sulge .
print(2 * 2)
print(2 * '3')
# korrutasin arvu ja sone .
tetra = (2 * '3')
type(tetra)
print(type(tetra))
# kontrollisin ja sain vastuse , et on string tuupi sone.
print(penta * 2)
from inspect import currentframe
# rea tunnuse programmi kaivitamine ,votab teegi .
print(currentframe().f_lineno)
print("\n" + str(currentframe().f_lineno) +
      ": selle reaga kaivitan loend * arv")
# naitab - tekitab rea vahetuse ,+konventeerib arvu soneks ,(valjastab
# viite sellele failile kus oleme ,.f lineno naitab rea tunnust
print(penta * 2)
print(666 / 999)
print(6 / 3)
# jagamine , vastuseks murd arv
print(6 // 3)  # 2
print(666 // 999)  # 0
print(999 // 666)  # 1
print(666 // 333)  # 2
print(999 // 33)  # 30
print(33 * 30)  # 990
# tegelesin jagamisega , taisarvu jagamisega ja kontrollisin korrutuse labi .
print("\n" + str(currentframe().f_lineno) +
      ": selle reaga  arv/ arv")
print(666 / 999)  # 0,6666666666
print(1**3)  # 1
print(2**3)  # 8
print("\n" + str(currentframe().f_lineno) +
      ": selle reaga  arv astmes arv")
print(2**3)
# arvu astendamine
print(2**3**2)  # 512
# ilma sulgusid kasutamatta arvutab teisest otsast
print((2**3)**2)  # 64
print("\n" + str(currentframe().f_lineno) +
      ": selle reaga  jaagi arvutamine")
print(15 % 3)  # 0
print(24 % 4)
# vastus tais arv , seega vatus on , et jaak on 0
print(24 % 7)  # 3
print(23 % 5)  # 3
# 5 mahub 23 sisse 4 korda ja 5korda 4 =20ja 20st 23ni jaab ule 3 , v:3
print("\n" + str(currentframe().f_lineno) +
      ": selle reaga  umardan arvu komakoha tapsusega")
print(2)  # 2
print(2.1)  # 2
print(146.5)
# ei olnud piisavalt tahelepanelik ja ei kasutanud round kasku
print(round(146.5))  # 146
print(round(146.55))  # 147
print(round(146.50001))  # 147
print(round(146.50))  # 146
print(round(146.50, 1))  # 146,5
print(round(146.50, 0))  # 146,0
print(round(146.50, -1))  # 150,0
print(round(146.50, -2))  # 100
print(round(146.50, -3))  # 0,0
print(round(146.6))  # 147
print(round(147.5))  # 148
# from math import ceil print(ceil(100.4))
# nii ei tohi , koik kasud eraldi ridadel
# 85 rida vigane , trellid ette
from math import ceil
print(ceil(100.4))  # 101
print("\n" + str(currentframe().f_lineno) +
      ": selle reaga  umardan arvu alla")
print(2.1)  # 2,1 see on ilma kasuta- floor -mida kulvad ,seda loikad
from math import floor
print(floor(2.1))  # 2
print(floor(27.5,))
print("\n" + str(currentframe().f_lineno) +
      ": selle reaga  ruutjuur")
from math import sqrt
print(sqrt(4))#2
print(sqrt(6))#2.449489742783178
import sys
print (sys.float_info)
from math import pow 
print(pow(4,4))#256
print(pow(2,2))#4
print(pow(6,2))#36
print(2**2)#4
print(2**0,5)#1 5
print(2**0.5)#1.4142135623730951
print("\n" + str(currentframe().f_lineno) +
      ": selle reaga logaritmime ")
from math import log 
print(log(4,2))#2
print(log(6,2))#2.584962500721156
from math import log10 
print(log10(10))#1
print(log10(25))#1.3979400086720377
from math import exp
print(exp(1))#2.718281828459045
print(exp(3))#20.085536923187668
from math import  sin 
print (sin(2)) 
print (sin(3))
from math import cos 
print (cos(2))# -0.4161468365471424 
print (cos(6))#0.960170286650366
from math import tan 
print (tan(2))#-2.185039863261519
from math import asin 
from math import acos 
from math import atan 
print (asin(0.1411200080598672))
print (asin (1))# 1.5707963267948966
print (acos (1))
print (atan (1))
print(45/57)
from math import degrees 
from math import radians 
from math import pi
print (degrees (1))
print (radians (1))
print (pi)
from math import tau, e 
print (2*pi)
print (e)#2.718281828459045
print (3*e)#8.154845485377136
print (8.154845485377136/3)#2.718281828459045
print (round (2.718281828459045,2))#2.72
print (2**8)
print (sqrt(256))#16
print ("\n" + str(currentframe().f_lineno) +
      ": selle reaga  loon loendi ja kusin selle suuruse")
some_list = ["vaim", "isa", "ema", "lehm","laps"]
print(some_list.__len__())# 5 kasutasin otse 
print (len(some_list))# 5 kasutasin kaudsel
print ("Hello world!")
print ("Hello world!")




